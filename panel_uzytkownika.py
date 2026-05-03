import customtkinter as ctk
import json
import os
def zapisz_wybor():
    wartosc = wybor_var.get()
    if wartosc == 1:
        odpowiedz = "Tak"
    else:
        odpowiedz = "Nie"
    nowy_wpis = {"czy_byl_na_silowni": odpowiedz}
    nazwa_pliku = "wynik_ankiety.json"
    if os.path.exists(nazwa_pliku) and os.path.getsize(nazwa_pliku) > 0:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            try:
                historia = json.load(plik)
            except:
                historia = []
    else:
        historia = []
    historia.append(nowy_wpis)
    with open(nazwa_pliku, "w", encoding="utf-8") as plik:
        json.dump(historia, plik, indent=4, ensure_ascii=False)
def zmiana_motywu():
    tryb = ctk.get_appearance_mode()
    if tryb == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")

root = ctk.CTk()
root.geometry("1024x768")
root.title("Siłownia Sahur")
nazwa = ctk.CTkLabel(root, text="Siłownia Sahur", font=("Arial", 28, "bold"))
nazwa.pack(pady=20)
kafelek_ankieta = ctk.CTkFrame(
    root, width=240,
    height=130,
    corner_radius=18,
    fg_color="transparent",
    border_width=2,
    border_color="#2D7DFF"
)
kafelek_ankieta.place(relx=0.88, rely=0.18, anchor="center")
ctk.CTkLabel(
    kafelek_ankieta, text="Czy byłeś dzisiaj na siłowni?",
    font=("Segoe UI", 15),
).place(relx=0.5, rely=0.25, anchor="center")
wybor_var = ctk.IntVar(value=0)
przycisk_tak = ctk.CTkRadioButton(
    kafelek_ankieta,
    text="Tak",
    variable=wybor_var,
    value=1,
    command=zapisz_wybor,
    width=80
)
przycisk_tak.place(relx=0.25, rely=0.65, anchor="center")
przycisk_nie = ctk.CTkRadioButton(
    kafelek_ankieta,
    text="Nie",
    variable=wybor_var,
    value=2,
    command=zapisz_wybor,
    width=80
)
przycisk_nie.place(relx=0.75, rely=0.65, anchor="center")
zmiana_koloru = ctk.CTkButton(
    root,
    text="Zmień motyw",
    command=zmiana_motywu
)
zmiana_koloru.place(relx=0.10, rely=0.95, anchor="center")
root.mainloop()