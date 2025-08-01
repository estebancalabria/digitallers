import tkinter as tk
from tkinter import messagebox

def saludar():
    nombre = entrada.get().strip()
    if nombre:
        mensaje = f"Saludo, {nombre}"
    else:
        mensaje = "Saludo, persona sin nombre"
    messagebox.showinfo("Saludo", mensaje)

# Ventana principal
root = tk.Tk()
root.title("Saludo personalizado")
root.geometry("800x600")
root.resizable(False, False)

# Marco para centrar verticalmente
marco = tk.Frame(root)
marco.pack(expand=True)

# Etiqueta + cuadro de texto
tk.Label(marco, text="Nombre:", font=("Arial", 14)).pack(pady=5)
entrada = tk.Entry(marco, font=("Arial", 14), width=30)
entrada.pack(pady=5)

# Botón
btn = tk.Button(marco, text="Saludar", command=saludar, font=("Arial", 14))
btn.pack(pady=15)

root.mainloop()