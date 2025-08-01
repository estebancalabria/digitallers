import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Hola Mundo")
root.geometry("800x600")          # Tamaño fijo 800x600
root.resizable(False, False)      # Opcional: evita que el usuario redimensione

# Crear la etiqueta con el texto
label = tk.Label(root, text="¡Hola, mundo!", font=("Arial", 24))
label.pack(expand=True)           # Centra vertical y horizontalmente

# Bucle principal
root.mainloop()