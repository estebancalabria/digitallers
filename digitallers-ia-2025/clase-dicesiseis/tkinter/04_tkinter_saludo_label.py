import tkinter as tk
from functools import partial

def saludar(txt_nombre, lbl_saludo):
    nombre = txt_nombre.get().strip()
    if nombre:
        texto = f"Saludo, {nombre}"
    else:
        texto = "Saludo, persona sin nombre"
    lbl_saludo.config(text=texto)

# Ventana principal
root = tk.Tk()
root.title("Saludo en ventana")
root.geometry("800x600")
root.resizable(False, False)

# Marco para centrar verticalmente
marco = tk.Frame(root)
marco.pack(expand=True)

# Etiqueta + cuadro de texto
tk.Label(marco, text="Nombre:", font=("Arial", 14)).pack(pady=5)
entrada = tk.Entry(marco, font=("Arial", 14), width=30)
entrada.pack(pady=5)

# Label donde aparecerá el saludo
etiqueta_saludo = tk.Label(marco, text="", font=("Arial", 16))
etiqueta_saludo.pack(pady=10)

# Botón
btn = tk.Button(marco, text="Saludar", command=partial(saludar, entrada, etiqueta_saludo), font=("Arial", 14))
btn.pack(pady=15)

root.mainloop()