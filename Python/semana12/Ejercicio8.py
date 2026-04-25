# Ejercicio 8:
# Pide tres lados de un triángulo y determina si es equilátero,
# isósceles o escaleno.

print("Identifiquemos el triangulo")

lado1 = float(input("Ingresa el lado 1: "))
lado2 = float(input("Ingresa el lado 2: "))
lado3 = float(input("Ingresa el lado 3: "))

if lado1 == lado2 == lado3:
    print("Equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isosceles")
else:
    print("Escaleno")
