import customtkinter as ctk
import tkinter.messagebox as messagebox
import json
import os
import subprocess
import sys


try:
   import vip
   import uzytkownik
except ImportError:
   pass


class LoginSystem(ctk.CTk):
   def __init__(self):
       super().__init__()


       self.title("Siłownia")
       self.geometry("400x500")
       ctk.set_appearance_mode("dark")


       self.users_file = "czlonkowie.json"
       self.setup_ui()


   def setup_ui(self):
       self.frame = ctk.CTkFrame(self, corner_radius=15)
       self.frame.pack(pady=40, padx=40, fill="both", expand=True)


       self.label = ctk.CTkLabel(self.frame, text="LOGOWANIE", font=("Arial", 24, "bold"))
       self.label.pack(pady=30)


       self.entry_login = ctk.CTkEntry(self.frame, placeholder_text="Login", width=200)
       self.entry_login.pack(pady=10)


       self.entry_pass = ctk.CTkEntry(self.frame, placeholder_text="Hasło", show="*", width=200)
       self.entry_pass.pack(pady=10)


       self.btn_login = ctk.CTkButton(self.frame, text="Zaloguj", command=self.handle_login)
       self.btn_login.pack(pady=20)


   def load_users(self):
       if os.path.exists(self.users_file):
           with open(self.users_file, "r", encoding="utf-8") as f:
               return json.load(f)
       return []


   def handle_login(self):
       login = self.entry_login.get()
       haslo = self.entry_pass.get()
       users = self.load_users()


       user_found = None
       for user in users:
           if user.get("login") == login and user.get("haslo") == haslo:
               user_found = user
               break


       if user_found:
           self.redirect_user(user_found)
       else:
           messagebox.showerror("Błąd", "Nieprawidłowy login lub hasło!")


   def redirect_user(self, user_data):
       role = user_data.get("rola")
       imie = user_data.get("imie")
      
       messagebox.showinfo("Sukces", f"Zalogowano jako {imie} ({role})")
      
       self.withdraw()


       if role == "admin":
           if os.path.exists("admin_panel.py"):
               subprocess.run([sys.executable, "admin_panel.py"])
           else:
               messagebox.showerror("Błąd", "Nie znaleziono pliku admin_panel.py!")
           self.show_login()
          
       elif role == "vip":
           try:
               vip.open_window(user_data, logout_callback=self.show_login)
           except NameError:
               messagebox.showerror("Błąd", "Moduł VIP nie został wczytany.")
               self.show_login()
       else:
           try:
               uzytkownik.open_window(user_data, logout_callback=self.show_login)
           except NameError:
               messagebox.showerror("Błąd", "Moduł użytkownika nie został wczytany.")
               self.show_login()


   def show_login(self):
       self.deiconify()
       self.entry_login.delete(0, 'end')
       self.entry_pass.delete(0, 'end')


if __name__ == "__main__":
   app = LoginSystem()
   app.mainloop()

