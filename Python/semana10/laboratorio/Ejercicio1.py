##  Crear una función que reciba un texto y un número. Según el número:
# Convertir todo el texto a mayúsculas
# Convertir todo el texto a minúsculas
# Colocar la primera letra en mayúscula


texto = input("Escribe un texto: ")
numero = int(input("Elige una opción (1, 2 o 3): "))

if numero == 1:
    print(texto.upper())

if numero == 2:
    print(texto.lower())

if numero == 3:
    print(texto.capitalize())
