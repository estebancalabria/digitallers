import tkinter as tk
#from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Ventana con Caja de texto")
ventana.geometry("400x300")

botonSuperior = tk.Button(ventana, text="Boton Superior", bg="lightblue")
botonSuperior.pack(side=tk.TOP, fill=tk.X)

botonSegundo = tk.Button(ventana, text="Boton Superior", bg="lightgreen")
botonSegundo.pack(side=tk.TOP, fill=tk.X)

botonAbajo = tk.Button(ventana, text="Boton Superior", bg="pink")
botonAbajo.pack(side=tk.BOTTOM, fill=tk.X)


ventana.mainloop()