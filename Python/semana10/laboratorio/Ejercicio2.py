# Crear una función que reciba una palabra y un número,
# y muestre el resultado en pantalla aplicando la transformación correspondiente (1, 2 o 3).

palabra = input("dime una palabra: ")
numero = int(
    input(
        "eleige 1 para todo mayusculas, 2 para todo minusculas y 3 para mayuscula en la primera letra: "
    )
)

if numero == 1:
    print(palabra.upper())
if numero == 2:
    print(palabra.lower())
if numero == 3:
    print(palabra.capitalize())
