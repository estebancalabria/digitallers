import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana con Label")
ventana.geometry("640x480")

def salir():
    ventana.quit()
boton = tk.Button(ventana, text="Salir", command=salir)
boton.pack(side=tk.BOTTOM, expand=True, fill='both')

texto = tk.Text(ventana)
texto.pack(expand=True, fill='both')


ventana.mainloop()

