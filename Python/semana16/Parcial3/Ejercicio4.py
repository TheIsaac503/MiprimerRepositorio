# Ejercicio 4:
# Un script debe auditar una secuencia de 50 registros, pero debe ignorar
# registros corruptos y detenerse si detecta una amenaza de seguridad.
# Crea un bucle que recorra un rango de 1 a 50.
# Filtro de Omisión: Si el número es múltiplo de 3
# (simulando un registro corrupto),
# utiliza la sentencia continua para saltarlo sin imprimir nada.
# Protocolo de Parada: Si el número es igual a 42
# (simulando una brecha de seguridad),
# utiliza break para detener todo el proceso inmediatamente.
# Para todos los demás casos, imprime: "Procesando registro ID: [número]".

relle = "="
canti = "Registro de id maxima capacidad 50"

print(relle.center(36, "="))
print(canti.center(36, "="))

for numero in range(1, 51):

    if numero % 3 == 0:
        continue
    elif numero == 43:
        bre = "Brecha de seguridad detectada"
        pro = "Proceso detenido"
        print(bre.center(36, "="))
        print(pro.center(36, "="))

    if numero == 43:
        break

    print(f"Procesando registro ID: {numero}")
