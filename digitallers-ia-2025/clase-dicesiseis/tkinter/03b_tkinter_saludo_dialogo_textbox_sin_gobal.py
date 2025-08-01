import tkinter as tk
from tkinter import messagebox
from functools import partial

# Ojo aca. Las funciones no deben tener acceso a variables globales
# Solo deberian acceder a variables locales o pasadas como parametros
def saludar(label_nombre):
    nombre = label_nombre.get().strip()
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
#Esto se hace para evitar el uso de variables globales con el parametro partial
btn = tk.Button(marco, text="Saludar", command=partial(saludar, entrada), font=("Arial", 14))
btn.pack(pady=15)

root.mainloop()