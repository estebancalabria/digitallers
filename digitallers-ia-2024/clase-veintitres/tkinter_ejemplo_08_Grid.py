import tkinter as tk
#from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Ventana con Caja de texto")
ventana.geometry("400x300")
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)

botonSuperior = tk.Button(ventana, text="Boton Superior", bg="lightblue")
botonSuperior.grid(row=0, column=0, sticky="nsew")

botonSegundo = tk.Button(ventana, text="Boton Superior", bg="lightgreen")#
#sticky="nsew": Este argumento indica que el widget debe expandirse en las direcciones norte (N), sur (S),
# este (E) y oeste (W), lo que significa que el botón ocupará todo el espacio disponible en su celda, 
# tanto en ancho como en alto.
botonSegundo.grid(row=0, column=1, sticky="nsew")

botonAbajo = tk.Button(ventana, text="Boton Superior", bg="pink")
botonAbajo.grid(row=1, column=0, columnspan=2, sticky="nsew")


ventana.mainloop()