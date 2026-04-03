# Crear una función que reciba un texto y un número,
# transforme el texto según la opción y luego devuelva la cantidad de caracteres del resultado.

texto = input("Escribe un texto: ")
numero = int(input("Elige un munero del 1 al 3: "))


def transformar(texto, numero):
    if numero == 1:
        resultado = texto.upper()
    elif numero == 2:
        resultado = texto.lower()
    elif numero == 3:
        resultado = texto.capitalize()
    else:
        print("Opción inválida")
        return 0

    print("Texto transformado:", resultado)
    return len(resultado)


cantidad = transformar(texto, numero)

print("Cantidad de caracteres:", cantidad)
