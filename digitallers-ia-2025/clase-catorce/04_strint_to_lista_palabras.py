#Dame una funcion que reciba un string con un texto y devuelva una lista de palabras, separando por espacios.
# Luego mostrar la lista de palabras y contar cuantas palabras hay en la lista.
def string_a_palabras(texto):
    return texto.split()

texto = "haciendo los ejercicios"
lista_palabras = string_a_palabras(texto)
    
# Mostramos la lista de palabras
print("Lista de palabras:", lista_palabras)
    
# Contamos cuántas palabras hay
cantidad = len(lista_palabras)
print("Cantidad de palabras en la lista:", cantidad)