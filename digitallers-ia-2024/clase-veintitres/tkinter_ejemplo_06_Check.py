import tkinter as tk
from tkinter import messagebox


ventana = tk.Tk()
ventana.title("Ventana con Caja de texto")
ventana.geometry("400x300")

label = tk.Label(ventana, text="Ingrese su nombre!", font=("Arial Bold", 20))
label.pack(pady=20)

entrada = tk.Entry(ventana, width=20)
entrada.pack(pady=20)

def boton_presionado():
    if entrada.get():
        messagebox.showinfo("Mensaje", "Hola, " + entrada.get())        
    else:
        messagebox.showerror("Error", "No ha ingresado ningun nombre")

    if checkedVar.get():
        ventana.destroy()

boton = tk.Button(ventana, text="Presioname", command=boton_presionado)
boton.pack(pady=20)

checkedVar = tk.BooleanVar()
check = tk.Checkbutton(ventana, text="Salir luego de mostrar el mensaje", variable=checkedVar)
check.pack(pady=20)

ventana.mainloop()