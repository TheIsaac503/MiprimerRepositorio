# Ejercicio 7:
# Solicita el monto de una compra y aplica:
# Más de 100: 20% de descuento
# Entre 50 y 100: 10% de descuento
# Menos de 50: sin descuento

monto = float(input("El total de compra fue: $"))

descuento1 = monto * 20 / 100
descuento2 = monto * 10 / 100

if monto > 100:
    print("Su total apagar es: ", monto - descuento1, "Con descuento del 20%")
elif monto >= 50 or monto <= 100:
    print("Su total apagar es: ", monto - descuento2, "Con descuento del 10%")
elif monto < 50:
    print(monto, "Sin descuento")
