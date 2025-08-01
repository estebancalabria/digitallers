import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Hola Mundo con Tkinter")
ventana.geometry("800x600")

# Crear etiqueta con el texto
etiqueta = tk.Label(ventana, text="Hola Mundo", font=("Arial", 24))
etiqueta.pack(pady=20)

# Ejecutar el loop de la ventana
ventana.mainloop()