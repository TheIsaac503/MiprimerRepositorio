# Ejercicio 3:
# Ingresa una nota del 0 al 10 y muestra:
# 9-10: Excelente
# 7-8: Bueno
# 6: Aprobado
# 0-5: Reprobado

nota = float(input("Clasifiquemos tu nota: "))

if 9 <= nota <= 10:
    print("Exelente")
elif 7 <= nota <= 8:
    print("Bueno")
elif nota == 6:
    print("Bueno")
elif 0 <= nota <= 5:
    print("Reprobado")
else:
    print("No te puedo quitar puntos")
