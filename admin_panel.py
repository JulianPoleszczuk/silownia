import customtkinter as ctk
import json
import os
from CTkTable import CTkTable

CZLONKOWIE = "czlonkowie.json"

#wczytywanie pliku json
def wczytaj_dane():
    if os.path.exists(CZLONKOWIE):
        with open(CZLONKOWIE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return []
    return []
def zapisz_dane(lista):
    with open(CZLONKOWIE, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)
def dodaj_osobe_json(nowy):
    lista = wczytaj_dane()
    lista.append(nowy)
    zapisz_dane(lista)
# tworzenie tabeli wszystkich czlonkow

def lista_osob():
    global tabela

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
        tabela.destroy()
    except:
        pass

    tabela = CTkTable(
        master=root,
        values=dane
    )
    tabela.pack(pady=30)
#okno dodawanie osob do json
def okno_dodawania():
    win = ctk.CTkToplevel(root)
    win.title("Dodaj osobę")
    win.geometry("350x350")

    ctk.CTkLabel(win, text="Imię").pack(pady=5)
    entry_imie = ctk.CTkEntry(win)
    entry_imie.pack(pady=5)

    ctk.CTkLabel(win, text="Nazwisko").pack(pady=5)
    entry_nazwisko = ctk.CTkEntry(win)
    entry_nazwisko.pack(pady=5)

    ctk.CTkLabel(win, text="Rola").pack(pady=5)
    combo_rola = ctk.CTkComboBox(
        win,
        values=["Admin", "Trener", "Klient"]
    )
    combo_rola.pack(pady=5)
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
            win.destroy()
    ctk.CTkButton(
        win,
        text="Zapisz",
        command=zapisz
    ).pack(pady=20)
def okno_usuwania():
    win = ctk.CTkToplevel(root)
    win.title("Usuń osobę")
    win.geometry("350x250")
    ctk.CTkLabel(win, text="Imię").pack(pady=5)
    entry_imie = ctk.CTkEntry(win)
    entry_imie.pack(pady=5)
    ctk.CTkLabel(win, text="Nazwisko").pack(pady=5)
    entry_nazwisko = ctk.CTkEntry(win)
    entry_nazwisko.pack(pady=5)
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
        win.destroy()

    ctk.CTkButton(
        win,
        text="Usuń",
        command=usun
    ).pack(pady=20)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Menadżer Członkostwa w Siłowni")
root.geometry("1024x768")

ctk.CTkLabel(
    root,
    text="Panel Admina",
    font=("Arial", 28, "bold")
).pack(pady=20)

ctk.CTkButton(
    root,
    text="Dodaj osobę",
    width=200,
    command=okno_dodawania
).pack(pady=10)

ctk.CTkButton(
    root,
    text="Usuń osobę",
    width=200,
    command=okno_usuwania
).pack(pady=10)

lista_osob()

root.mainloop()