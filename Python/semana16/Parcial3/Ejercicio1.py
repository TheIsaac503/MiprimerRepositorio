# Ejercicio 1
# Se trabaja para una empresa de envíos. Recibes códigos de rastreo
# con el formato AÑO-CATEGORÍA-PAÍS (ejemplo: 2024-TECNOLOGIA-ES).
# Tu tarea es automatizar la clasificación de estos paquetes siguiendo
#  estas instrucciones:
# Solicita al usuario una etiqueta de rastreo mediante input().
# ( escriba en la consola )
# Realiza una validación de seguridad: si la entrada está vacía
# ("") o es None, el programa debe informar el error y finalizar.
# Utilizando Slicing, extrae la sección central (la categoría) y
# muéstrala en pantalla.
# Aplica el Operador Ternario para imprimir: "Ruta Local" si el
# código termina en las siglas de tu país (ejemplo: "SV"), o "Ruta
# Internacional" en cualquier otro caso.

guion = "="
guia1 = "Dime el codigo de etiqueta en su correcta forma"
guia2 = "Ejemplo: 2024-TECNOLOGIA-ES"
print(guion.center(47, "="))
print(guia1.center(47, "="))
print(guia2.center(47, "="))
print(guion.center(47, "="))
codigoR = input("Ingrese la etiqueta: ")

codigoRa = codigoR.upper().replace(" ", "-")

if codigoRa == "" or codigoRa == None:
    print(guion.center(40, "="))
    print("Etiqueta inválida")
    print(guion.center(40, "="))
else:
    division = codigoRa.split("-")

    if len(division) != 3:
        print(guion.center(40, "="))
        print("Formato incorrecto")
        print(guion.center(40, "="))
    else:
        seccion = division[1]
        print(guion.center(40, "="))
        print("Tu categoría es:", seccion)

        mensaje = (
            "Ruta local"
            if codigoRa.endswith(
                "SV",
            )
            else "Ruta internacional"
        )
        print(mensaje)
        print(guion.center(40, "="))
