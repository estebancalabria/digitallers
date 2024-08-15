# Ejercicio
# Crear una cuadricula de 3x3 con botones en cada celda. Cada boton debe un numero del 1 al 9.
# Usar el metodo grid() para organizar los botones en la cuadricula.
# Usar dos for anidados`    

import tkinter as tk
ventana = tk.Tk()
ventana.title("Cuadrícula 3x3 con Botones")
ventana.geometry("300x300")

for i in range(3):
    ventana.grid_rowconfigure(i, weight=1)
    ventana.grid_columnconfigure(i, weight=1)

numero = 1
for fila in range(3):
    for columna in range(3):
        boton = tk.Button(ventana, text=str(numero), width=10, height=3)
        boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")
        numero += 1

ventana.mainloop()