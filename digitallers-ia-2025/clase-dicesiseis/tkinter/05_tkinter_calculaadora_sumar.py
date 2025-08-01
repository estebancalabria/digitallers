import tkinter as tk
from functools import partial


def sumar(campos, resultado):
    """Recibe una tupla con los dos Entry y el Entry resultado."""
    try:
        a = float(campos[0].get())
        b = float(campos[1].get())
        resultado.config(state="normal")
        resultado.delete(0, tk.END)
        resultado.insert(0, str(a + b))
        resultado.config(state="disabled")
    except ValueError:
        resultado.config(state="normal")
        resultado.delete(0, tk.END)
        resultado.insert(0, "Error")
        resultado.config(state="disabled")


# Ventana
root = tk.Tk()
root.title("Calculadora")
root.geometry("800x600")
root.resizable(False, False)

# Marco centrado
marco = tk.Frame(root)
marco.pack(expand=True)

# Título
tk.Label(marco, text="Calculadora", font=("Arial", 18)).pack(pady=10)

# Campos de entrada
entrada1 = tk.Entry(marco, font=("Arial", 14), width=15)
entrada2 = tk.Entry(marco, font=("Arial", 14), width=15)
entrada1.pack(pady=5)
entrada2.pack(pady=5)

# Botón +
btn = tk.Button(
    marco,
    text="+",
    font=("Arial", 14),
    command=partial(sumar, (entrada1, entrada2), None)
)
btn.pack(pady=10)

# Campo resultado (deshabilitado)
resultado = tk.Entry(marco, font=("Arial", 14), width=15, state="disabled")
resultado.pack(pady=5)

# Actualizar referencia al resultado
btn.config(command=partial(sumar, (entrada1, entrada2), resultado))

root.mainloop()