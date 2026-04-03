texto = input("Escribe un texto: ")

print("MENÚ")
print("1. MAYÚSCULAS")
print("2. minúsculas")
print("3. Primera letra en mayúscula")

numero = int(input("Elige una opción (1, 2 o 3): "))


def transformar(texto, numero):
    if numero == 1:
        return texto.upper()
    elif numero == 2:
        return texto.lower()
    elif numero == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


resultado = transformar(texto, numero)

print("Resultado:", resultado)
