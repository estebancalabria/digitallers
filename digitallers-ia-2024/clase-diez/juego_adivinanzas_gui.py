import tkinter as tk
import random

class JuegoAdivinanza:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Adivinanza")

        self.numero_secreto = random.randint(1, 100)
        self.intentos = 6
        self.adivino = False

        self.etiqueta_bienvenida = tk.Label(root, text="Bienvenido al juego de adivinanza!")
        self.etiqueta_bienvenida.pack()

        self.etiqueta_instrucciones = tk.Label(root, text="He pensado en un número entre 1 y 100. Tienes 6 intentos para adivinarlo.")
        self.etiqueta_instrucciones.pack()

        self.etiqueta_intentos = tk.Label(root, text=f"Te quedan {self.intentos} intentos.")
        self.etiqueta_intentos.pack()

        self.entrada_numero = tk.Entry(root)
        self.entrada_numero.pack()

        self.boton_adivinar = tk.Button(root, text="Adivinar", command=self.verificar_adivinanza)
        self.boton_adivinar.pack()

        self.etiqueta_resultado = tk.Label(root, text="")
        self.etiqueta_resultado.pack()

    def verificar_adivinanza(self):
        if not self.adivino and self.intentos > 0:
            adivinanza = self.entrada_numero.get()
            try:
                adivinanza = int(adivinanza)
                self.intentos -= 1
                self.etiqueta_intentos.config(text=f"Te quedan {self.intentos} intentos.")

                if adivinanza == self.numero_secreto:
                    self.etiqueta_resultado.config(text=f"¡Felicidades! Has adivinado el número {self.numero_secreto}.", fg="green")
                    self.adivino = True
                    self.boton_adivinar.config(state=tk.DISABLED)
                elif adivinanza < self.numero_secreto:
                    self.etiqueta_resultado.config(text="El número secreto es mayor.", fg="red")
                else:
                    self.etiqueta_resultado.config(text="El número secreto es menor.", fg="red")

                if not self.adivino and self.intentos == 0:
                    self.etiqueta_resultado.config(text=f"Game Over. El número secreto era {self.numero_secreto}.", fg="red")
                    self.boton_adivinar.config(state=tk.DISABLED)

            except ValueError:
                self.etiqueta_resultado.config(text="Por favor, ingresa un número válido.", fg="red")

# Crear la ventana principal
root = tk.Tk()
juego = JuegoAdivinanza(root)
root.mainloop()
