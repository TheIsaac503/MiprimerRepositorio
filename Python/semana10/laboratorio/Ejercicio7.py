texto = input("Escribe un texto: ")
seleccion = input(
    "Dale un orden a tu texto escribiendo los numeros (1,2,3) separado por espacios: "
)
lista_numeros = list(map(int, seleccion.split()))


def transformar(texto, lista_numeros):
    resultado = texto

    for numero in lista_numeros:
        if numero == 1:
            resultado = resultado.upper()
        elif numero == 2:
            resultado = resultado.lower()
        elif numero == 3:
            resultado = resultado.capitalize()
        else:
            print("Opción inválida")

    return resultado


resultado_final = transformar(texto, lista_numeros)

print("Resultado final:", resultado_final)
