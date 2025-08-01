#import calculadora #Ahora asi no funciona, tengo que importar la clase Calculadora
from calculadora import Calculadora  # Importando la clase Calculadora directamente

# Pruebas de las funciones
print("Suma:", Calculadora.sumar(10, 5))
print("Resta:", Calculadora.restar(10, 5))
print("Multiplicación:", Calculadora.multiplicar(10, 5))
print("División:", Calculadora.dividir(10, 5))