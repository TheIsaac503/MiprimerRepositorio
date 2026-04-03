# Solicitar al usuario un texto y un número.
# Enviar esos datos a una función que aplique la transformación según la opción elegida.
texto = input("Escribe un texto: ")
numero = int(input("Elige un munero del 1 al 3: "))


def transformar(texto, numero):
    if numero == 1:
        print(texto.upper())
    elif numero == 2:
        print(texto.lower())
    elif numero == 3:
        print(texto.capitalize())


transformar(texto, numero)
