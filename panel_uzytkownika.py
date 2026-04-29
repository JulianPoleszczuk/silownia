import customtkinter as ctk
root = ctk.CTk()
root.geometry("1024x768")
root.title("Siłownia Sahur")
nazwa  = ctk.CTkLabel(
    root,
    text="Siłownia Sahur",
    font = ("Arial", 28, "bold"),
).pack(pady=20)
kafelek_ankieta = ctk.CTkFrame(
    root,
    width=240,
    height=130,
    corner_radius=18,
    fg_color = "transparent",
    border_width=2,
    border_color = "#2D7DFF",
)
kafelek_ankieta.place(relx=0.88, rely=0.18, anchor="center")
ctk.CTkLabel(
    root,
    text="Czy byłeś dzisiaj na siłowni?",
    font=("Segoe UI", 18),
    text_color="white"
).place(relx=0.88, rely=0.14, anchor="center")
root.mainloop()