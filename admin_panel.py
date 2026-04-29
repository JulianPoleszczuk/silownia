import customtkinter as ctk
import json
import os
CZLONKOWIE = "czlonkowie.json"
def zapisywanie(nowy):
    if os.path.exists(CZLONKOWIE):
        with open(CZLONKOWIE, "r") as f:
            try:
                lista = json.load(f)
            except:
                lista = []
    else:
        lista = []
    lista.append(nowy)
    with open(CZLONKOWIE, "w") as f:
        json.dump(lista, f, indent=4)
def okno_dodawania():
    win = ctk.CTkToplevel(root)
    win.title("Dodaj osobę")
    win.geometry("300x200")

    label1 = ctk.CTkLabel(win, text="Imię")
    label1.pack(pady=5)
    entry_imie = ctk.CTkEntry(win)
    entry_imie.pack(pady=5)
    label2 = ctk.CTkLabel(win, text="Nazwisko")
    label2.pack(pady=5)
    entry_nazwisko = ctk.CTkEntry(win)
    entry_nazwisko.pack(pady=5)
    def zapisz():
        imie = entry_imie.get()
        nazwisko = entry_nazwisko.get()

        if imie and nazwisko:
            dane = {
                "imie": imie,
                "nazwisko": nazwisko,
                "status": "Aktywny"
            }
            zapisywanie(dane)
            win.destroy()
    btn = ctk.CTkButton(win, text="Zapisz", command=zapisz)
    btn.pack(pady=10)
def okno_usuwania():
    win = ctk.CTkToplevel(root)
    win.title("Usuń osobę")
    win.geometry("300x200")

    label1 = ctk.CTkLabel(win, text="Imię")
    label1.pack(pady=5)

    entry_imie = ctk.CTkEntry(win)
    entry_imie.pack(pady=5)

    label2 = ctk.CTkLabel(win, text="Nazwisko")
    label2.pack(pady=5)

    entry_nazwisko = ctk.CTkEntry(win)
    entry_nazwisko.pack(pady=5)

    btn = ctk.CTkButton(win, text="Usuń")
    btn.pack(pady=10)
root = ctk.CTk()
root.title("Menadżer Członkostwa w Siłowni")
root.geometry("1024x768")
tekst = ctk.CTkLabel(root, text="Panel Admina")
tekst.pack(pady=30)

przycisk_dodaj = ctk.CTkButton(root, text="Dodaj osobę", command=okno_dodawania)
przycisk_dodaj.pack(pady=10)

przycisk_usun = ctk.CTkButton(root, text="Usuń osobę", command=okno_usuwania)
przycisk_usun.pack(pady=10)

root.mainloop()