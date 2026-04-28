
import customtkinter as ctk
# from CustomTkinterMessagebox import *
import json
import os
CZLONKOWIE = "czlonkowie.json"
def zapisywanie(nowy):
    if os.path.exists(CZLONKOWIE):
        with open(CZLONKOWIE, "r") as f:
            try:
                lista_czlonkow = json.load(f)
            except json.JSONDecodeError:
                lista_czlonkow = []
    else:
        lista_czlonkow = []
    lista_czlonkow.append(nowy)
    with open(CZLONKOWIE, "w") as f:
        json.dump(lista_czlonkow, f, indent=4)
def dodawanie_osob():
    imie = entry_imie.get()
    nazwisko = entry_nazwisko.get()
    if imie and nazwisko:
        dane_czlonka = {
            "imie": imie,
            "nazwisko": nazwisko,
            "status": "Aktywny"
        }
        zapisywanie(dane_czlonka)
        entry_imie.delete(0, ctk.END)
        entry_nazwisko.delete(0, ctk.END)
root = ctk.CTk()
root.title("Menadżer Członkostwa w Siłowni")
root.geometry("400x400")
entry_imie = ctk.CTkEntry(root,placeholder_text="imie")
entry_imie.grid(row=0, column=1)
entry_nazwisko = ctk.CTkEntry(root,placeholder_text="nazwisko")
entry_nazwisko.grid(row=1, column=1)
wyslij = (ctk.CTkButton(root, text="Dodaj", command=dodawanie_osob))
wyslij.grid(row=2, column=1)
root.mainloop()

