# Ejercicio 2:
# Las empresas pierden dinero por errores de redondeo al usar float.
# Se te ha pedido crear un terminal de cobro seguro que garantice
# precisión bancaria.
# Crea un bucle while que solicite precios de productos de forma indefinida.
# Implementa una estructura try-except específica para ValueError.
# Si el usuario ingresa texto en lugar de un número, muestra un
# mensaje de advertencia y permite que el bucle continúe sin cerrar
#  el programa.
# Utiliza la clase Decimal (del módulo decimal) para procesar los
# montos con precisión.
# El sistema debe cerrarse solo cuando el usuario ingrese el número
# 0. Al finalizar, muestra el total acumulado usando un f-string.  f””

guion = "="
print(guion.center(54, "="))
inf = "Ingrese el precio del producto o 0 para salir"
print(inf.center(54, "="))
print(guion.center(54, "="))

from decimal import Decimal

total = 0

while True:
    try:
        precio = float(input("Precio del producto: "))
        monto = Decimal(precio)
        total += monto

        if precio == 0:
            break

    except ValueError:
        print("Entrada no valida. Debe ingresar un numero.")


print(guion.center(54, "="))
print(f"Total acumulado: ${total}")
print(guion.center(54, "="))
