import customtkinter as ctk
import json
import os
from CTkTable import CTkTable
PLIK_JSON = "czlonkowie.json"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
def wczytaj_dane():
    if os.path.exists(PLIK_JSON):
        with open(PLIK_JSON, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return []
    return []
def zapisz_dane(lista):
    with open(PLIK_JSON, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)
def dodaj_osobe_json(nowy):
    lista = wczytaj_dane()
    lista.append(nowy)
    zapisz_dane(lista)
root = ctk.CTk()
root.geometry("1280x720")
root.title("Menadżer Członkostwa w Siłowni")
root.configure(fg_color="#07111F")
def lista_osob():
    global frame_tabela, tabela
    osoby = wczytaj_dane()
    dane = [["Imię", "Nazwisko", "Rola", "Status"]]
    for osoba in osoby:
        dane.append([
            osoba["imie"],
            osoba["nazwisko"],
            osoba["rola"],
            osoba["status"]
        ])

    try:
        frame_tabela.destroy()
    except:
        pass
    frame_tabela = ctk.CTkFrame(
        root,
        width=820,
        height=420,
        corner_radius=18,
        fg_color="#111827"
    )
    frame_tabela.place(relx=0.43, rely=0.52, anchor="center")
    scroll = ctk.CTkScrollableFrame(
        frame_tabela,
        width=780,
        height=380,
        fg_color="transparent"
    )
    scroll.place(relx=0.5, rely=0.5, anchor="center")

    tabela = CTkTable(
        master=scroll,
        values=dane
    )
    tabela.pack()
def okno_dodawania():
    win = ctk.CTkToplevel(root)
    win.geometry("400x420")
    win.title("Dodaj osobę")
    win.configure(fg_color="#111827")

    ctk.CTkLabel(
        win,
        text="Dodaj nowego użytkownika",
        font=("Segoe UI", 24, "bold")
    ).pack(pady=20)

    entry_imie = ctk.CTkEntry(win, width=250, placeholder_text="Imię")
    entry_imie.pack(pady=10)

    entry_nazwisko = ctk.CTkEntry(win, width=250, placeholder_text="Nazwisko")
    entry_nazwisko.pack(pady=10)

    combo_rola = ctk.CTkComboBox(
        win,
        width=250,
        values=["Admin", "Trener", "Klient"]
    )
    combo_rola.pack(pady=10)
    combo_rola.set("Klient")
    def zapisz():
        imie = entry_imie.get()
        nazwisko = entry_nazwisko.get()
        rola = combo_rola.get()
        if imie and nazwisko:
            nowy = {
                "imie": imie,
                "nazwisko": nazwisko,
                "rola": rola,
                "status": "Aktywny"
            }

            dodaj_osobe_json(nowy)
            lista_osob()
            licznik()
            win.destroy()

    ctk.CTkButton(
        win,
        text="Zapisz",
        width=220,
        height=42,
        corner_radius=12,
        fg_color="#2D7DFF",
        hover_color="#1F6DF2",
        command=zapisz
    ).pack(pady=25)
def okno_usuwania():
    win = ctk.CTkToplevel(root)
    win.geometry("400x350")
    win.title("Usuń osobę")
    win.configure(fg_color="#111827")

    ctk.CTkLabel(
        win,
        text="Usuń użytkownika",
        font=("Segoe UI", 24, "bold")
    ).pack(pady=20)
    entry_imie = ctk.CTkEntry(win, width=250, placeholder_text="Imię")
    entry_imie.pack(pady=10)
    entry_nazwisko = ctk.CTkEntry(win, width=250, placeholder_text="Nazwisko")
    entry_nazwisko.pack(pady=10)
    def usun():
        imie = entry_imie.get()
        nazwisko = entry_nazwisko.get()
        lista = wczytaj_dane()
        nowa_lista = [
            osoba for osoba in lista
            if not (
                osoba["imie"].lower() == imie.lower()
                and osoba["nazwisko"].lower() == nazwisko.lower()
            )
        ]

        zapisz_dane(nowa_lista)
        lista_osob()
        licznik()
        win.destroy()
    ctk.CTkButton(
        win,
        text="Usuń",
        width=220,
        height=42,
        corner_radius=12,
        fg_color="#FF3B3B",
        hover_color="#D82E2E",
        command=usun
    ).pack(pady=25)
def wyloguj():
    root.destroy()
def licznik():
    ile_osob_licznik.configure(text=str(len(wczytaj_dane())))
ctk.CTkLabel(
    root,
    text="Panel Admina",
    font=("Segoe UI", 38, "bold"),
    text_color="white"
).place(relx=0.5, rely=0.07, anchor="center")

#przycisk do dodawania ludzi
ctk.CTkButton(
    root,
    text="Dodaj osobę",
    width=220,
    height=42,
    corner_radius=12,
    fg_color="#2D7DFF",
    hover_color="#1F6DF2",
    font=("Segoe UI", 16, "bold"),
    command=okno_dodawania
).place(relx=0.34, rely=0.18, anchor="center")
#przycisk od usuwania osoby
ctk.CTkButton(
    root,
    text="Usuń osobę",
    width=220,
    height=42,
    corner_radius=12,
    fg_color="#2D7DFF",
    hover_color="#1F6DF2",
    font=("Segoe UI", 16, "bold"),
    command=okno_usuwania
).place(relx=0.52, rely=0.18, anchor="center")

#wylogowywanie się
ctk.CTkButton(
    root,
    text="Wyloguj",
    width=130,
    height=38,
    corner_radius=10,
    fg_color="transparent",
    border_width=2,
    border_color="#FF3B3B",
    text_color="#FF3B3B",
    hover_color="#301010",
    font=("Segoe UI", 14, "bold"),
    command=wyloguj
).place(relx=0.06, rely=0.95, anchor="center")
#statystyki
kafelek = ctk.CTkFrame(
    root,
    width=240,
    height=130,
    corner_radius=18,

    fg_color="transparent",
    border_width=2,
    border_color="#2D7DFF"
)
kafelek.place(relx=0.88, rely=0.18, anchor="center")

ctk.CTkLabel(
    kafelek,
    text="Wszyscy członkowie",
    font=("Segoe UI", 18),
    text_color="white"
).place(relx=0.5, rely=0.30, anchor="center")
ile_osob_licznik = ctk.CTkLabel(
    kafelek,
    text="",
    font=("Segoe UI", 34, "bold"),
    text_color="#2D7DFF"
)
licznik()
ile_osob_licznik.place(relx=0.5, rely=0.68, anchor="center")
lista_osob()
root.mainloop()