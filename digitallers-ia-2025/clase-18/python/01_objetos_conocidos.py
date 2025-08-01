


#Ejemplo. Con variables separadas
fecha_anio = 2023
fecha_mes = 10
fecha_dia = 5
print("Variables independientes sin relacionarse:")
print(fecha_anio)  # Acceso al año
print(fecha_mes)  # Acceso al mes
print(fecha_dia)  # Acceso al día
#Aca las variables son independientes, no se relacionan entre si
#Se me pueden perdir, olvidar e ir cada una por separado

from datetime import date

#Ejemplo. Con un objeto conocido
fecha = date(2023, 10, 5)  # Creación de un objeto fecha mediante su constructor
print("Variables relacionadas a un objeto conocido:")
print(fecha.year)  # Acceso al año
print(fecha.month)  # Acceso al mes
print(fecha.day)  # Acceso al día