# Crear una función que reciba una lista de palabras y un número.
# La función debe transformar cada palabra
# de la lista según la opción seleccionada (1, 2 o 3).

texto = input("Escribe un texto: ")
numero = int(input("Elige un munero del 1 al 3: "))


def transformar_texto(lista, numero):
    for palabra in lista:
        if numero == 1:
            print(palabra.upper())
        elif numero == 2:
            print(palabra.lower())
        elif numero == 3:
            print(palabra.capitalize())


lista_palabras = texto.split()
transformar_texto(lista_palabras, numero)
