import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

root = ctk.CTk()
root.geometry("700x400")
root.title("Lista członków")

# ---- tabela ----
tabela = ttk.Treeview(root, columns=("imie", "nazwisko", "rola", "status"), show="headings")

# nagłówki
tabela.heading("imie", text="Imię")
tabela.heading("nazwisko", text="Nazwisko")
tabela.heading("rola", text="Rola")
tabela.heading("status", text="Status")

# szerokość kolumn
tabela.column("imie", width=120)
tabela.column("nazwisko", width=150)
tabela.column("rola", width=120)
tabela.column("status", width=120)

tabela.pack(fill="both", expand=True, padx=20, pady=20)

# ---- dane testowe ----
tabela.insert("", "end", values=("Jan", "Kowalski", "Admin", "Aktywny"))
tabela.insert("", "end", values=("Anna", "Nowak", "Trener", "Aktywny"))
tabela.insert("", "end", values=("Piotr", "Wiśniewski", "Klient", "Nieaktywny"))

root.mainloop()