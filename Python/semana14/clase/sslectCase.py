# simular un juego
# ingresar una cantidad par de numeros
# debo emparejarlas con un texto
# debo dar un numero de intentos definido para el usuario
# prepara el buble y el select case

import random  # esto es para generar numeros aleatorios

# Salvar el numero random en una variable
numero = random.randint(1, 10)
print(numero)

for i in range(numero):
    print("Intento", i)
    print("===============")


def definirTargetas(numero):
    if numero % 2 == 0 and numero > 4:
        return numero
    else:
        return numero + 1


def asignarValoresAlasTargetas(numeroValidad):
    i = 0
    llenarTargetas = []
    temporal = ""
    while i <= numeroValidad:
        temporal = input("Ingrese un texto para la targeta " + str(i) + ": ")
        llenarTargetas.append(temporal)


import random  # esto es para generar numeros aleatorios

# Salvar el numero random en una variable
numero = random.randint(1, 10)
# print(numero)


def definirTargetas(numero):
    if numero % 2 == 0 and numero > 4:
        return numero
    else:
        return numero + 1


def asignarValoresAlasTargetas(numeroValidad):
    i = 0
    llenarTargetas = []
    temporal = ""
    while i <= numeroValidad:
        temporal = input("Ingrese un texto para la targeta " + str(i) + ": ")
        llenarTargetas.append(temporal)
