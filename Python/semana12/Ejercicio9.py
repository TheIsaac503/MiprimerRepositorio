# Ejercicio 9:
# Solicita un año y determina si es bisiesto.

año = int(input("Ingresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Año bisiesto")
else:
    print("No es bisiesto")
