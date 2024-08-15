#Autor Ezzequiel Ojeda :)
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")  # Tamaño inicial de la ventana

# Variables de entrada
input_text = tk.StringVar()
expression = ""

# Función para actualizar la expresión
def press(key):
    global expression
    expression += str(key)
    input_text.set(expression)

# Función para evaluar la expresión
def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Función para limpiar la entrada
def clear():
    global expression
    expression = ""
    input_text.set("")

# Configurar las filas y columnas para que se expandan
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)
    ventana.grid_rowconfigure(i, weight=1)

# Entrada de texto deshabilitada para escribir con teclado
entry = tk.Entry(ventana, textvariable=input_text, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, state='readonly')
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Crear los botones y organizarlos en una cuadrícula
button_texts = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in button_texts:
    boton = tk.Button(ventana, text=text, font=('Arial', 18), command=lambda t=text: press(t) if t != '=' else equal())
    boton.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Botón Clear
clear_button = tk.Button(ventana, text='C', font=('Arial', 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Configurar la fila adicional para que se expanda
ventana.grid_rowconfigure(5, weight=1)

# Iniciar el bucle de la interfaz
ventana.mainloop()
