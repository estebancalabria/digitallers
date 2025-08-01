# Quiero 4 Funciones que hagan lo siguiente:
# 1 Sumar dos números
# 2 Restar dos números
# 3 Multiplicar dos número
# 4 Dividir dos números
# Quiero que muestre por pantalla el resultado de las siguientes operaciones:
# 1 + 2  >>que haga print "1 + 2 = 3"
# 5 - 3  >>que haga print "5 - 3 = 2"
# 4 * 2  >>que haga print "4 * 2 = 8"
# 8 / 2  >>que haga print "8 / 2 = 4"

#num1 y num2 son los parámetros de las funciones, que representan los números a operar.
def sumar (num1, num2):
    return num1 + num2
  
def restar (num1, num2):
    return num1 - num2  

#Tradicionalmeint no se especifica el tipo de datos de los parámetros y el retorno
def multiplicar (num1, num2):
    return num1 * num2

#Type hints para indicar el tipo de datos de los parámetros y el retorno
def dividir(num1: float, num2: float) -> float:
    if num2 == 0:
        raise ValueError("No se puede dividir por cero.")
    return num1 / num2

print("1 + 2 = ", sumar(1, 2))
print("5 - 3 = ", restar(5, 3))
print("4 * 2 = ", multiplicar(4, 2), "devuelve", type(multiplicar(4, 2)))
print("8 / 2 = ", dividir(8, 2), "devuelve", type(dividir(8, 2)))
