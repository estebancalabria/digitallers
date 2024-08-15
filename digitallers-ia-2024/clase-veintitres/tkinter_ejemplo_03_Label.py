import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana con Label")
ventana.geometry("300x200")

label = tk.Label(ventana, text="Hola, mundo!", font=("Arial Bold", 20))
label.pack(pady=20)


ventana.mainloop()

# This is the same as tkinter_ejemplo_1.py, but with a different import statement.