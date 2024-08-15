import tkinter as tk
from tkinter import messagebox

def boton_presionado():
    messagebox.showinfo("Mensaje", "El boton ha sido presionado")

ventana = tk.Tk()
ventana.title("Ventana con Label y Boton")
ventana.geometry("400x300")

label = tk.Label(ventana, text="Hola, mundo!", font=("Arial Bold", 20))
label.pack(pady=20)

boton = tk.Button(ventana, text="Presioname", command=boton_presionado)
boton.pack(pady=20)

ventana.mainloop()

# This is the same as tkinter_ejemplo_1.py, but with a different import statement.