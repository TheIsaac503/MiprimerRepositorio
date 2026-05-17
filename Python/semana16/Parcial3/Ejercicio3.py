# Ejercicio 3:.
# Un sensor industrial envía lecturas de temperatura. Debes programar
#  la lógica que decida qué alertas disparar según los valores
# recibidos.
# Solicita al usuario 5 lecturas de temperatura (números enteros) y
# almacenarlas en una lista.
# Itera la lista con un for y utiliza la estructura match-case para
# evaluar:
# Caso 0: Mostrar "Alerta: Punto de Congelación".
# Caso 100: Mostrar "Alerta: Punto de Ebullición".
# Caso por defecto (_): Usa un Operador Ternario interno para imprimir "Estado: Estable" si la temperatura está entre 10 y 30 grados i, "Estado: Crítico" si está fuera de ese rango.


guion = "="
print(guion.center(30, "="))
leer = "Se leeran 5 temperaturas"
print(leer.center(30, "="))
print(guion.center(30, "="))

temperaturas = []

for i in range(5):

    if i is 0:
        dato = int(input("Primera lectura: "))
        temperaturas.append(dato)
    elif i is 1:
        dato = int(input("Segunda lectura: "))
        temperaturas.append(dato)
    elif i is 2:
        dato = int(input("Tercera lectura: "))
        temperaturas.append(dato)
    elif i is 3:
        dato = int(input("Cuarta lectura: "))
        temperaturas.append(dato)
    elif i is 4:
        dato = int(input("Quinta lectura: "))
        temperaturas.append(dato)

print(guion.center(30, "="))
print(guion.center(30, "="))

for temp in temperaturas:
    match temp:
        case 0:
            print("Alerta: Punto de Congelacion")

        case 100:
            print("Alerta: Punto de Ebullicion")

        case _:
            estado = "Estado: Estable" if 10 <= temp <= 30 else "Estado: Critico"
            print(estado)
