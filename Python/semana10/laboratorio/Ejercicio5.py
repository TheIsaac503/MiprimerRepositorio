texto = input("Escribe un texto: ")
numero = int(input("Elige un munero del 1 al 3: "))


def transformar(texto, numero):
    if numero == 1:
        print(texto.upper())
    elif numero == 2:
        print(texto.lower())
    elif numero == 3:
        print(texto.capitalize())
    else:
        print("Opción inválida")


transformar(texto, numero)
