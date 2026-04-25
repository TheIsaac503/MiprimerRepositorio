# Ejercicio 6:
# Pide un número del 1 al 7 y muestra el día de la semana
# correspondiente. Si no está en el rango, muestra un mensaje de
# error.

dia = int(input("Dime un numero del 1 al 7: "))


if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Lunes")
elif dia == 3:
    print("Martes")
elif dia == 4:
    print("Miercoles")
elif dia == 5:
    print("Jueves")
elif dia == 6:
    print("Viernes")
elif dia == 7:
    print("Sabado")
elif dia < 1 or dia > 7:
    print("Error")
