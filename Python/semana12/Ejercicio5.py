# Ejercicio 5:
# Solicita dos números y una operación (+, -, *, /) y realiza el
# cálculo usando if, elif y else.

print("Dime dos numeros y que operacion quieres hacer.")

numero1 = float(input("Primer numero: "))
operecion = input("Que operacion quieres hacer(+, -, * o /): ")
numero2 = float(input("Segundo numero: "))
print("Tu operacion es:", numero1, operecion, numero2)

if operecion == "+":
    print("Respuesta:", numero1 + numero2)
elif operecion == "-":
    print("respuesta:", numero1 - numero2)
elif operecion == "*":
    print("respuesta:", numero1 * numero2)
elif operecion == "/":
    if numero2 != 0:
        print("Respuesta:", numero1 / numero2)
    else:
        print("No se puede dividir entre 0")
else:
    print("Operacion no identificada")
