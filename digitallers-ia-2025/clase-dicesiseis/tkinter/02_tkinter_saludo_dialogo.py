import tkinter as tk
from tkinter import messagebox

def saludar():
    messagebox.showinfo("Saludo", "Hola Terricola")

# Ventana principal
root = tk.Tk()
root.title("Demo")
root.geometry("800x600")
root.resizable(False, False)

# Botón
btn = tk.Button(root, text="Presióname", command=saludar, font=("Arial", 16))
btn.pack(expand=True)

root.mainloop()