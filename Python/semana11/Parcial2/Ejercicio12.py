# Ejercicio 12
# 1. Toma el nombre de archivo "Sunombre.txt".
# 2. Remueve el sufijo ".txt" y posteriormente remueve el prefijo "ING. ".
# 3. Toma el texto que quede limpio, convertido a minúsculas.

nombre = "ING. Isaac.txt"
print("Veamos el proceso de:", nombre)

nombrenosufijo = nombre.removesuffix(".txt")
nombrenoprefijo = nombre.removeprefix("ING. ")
limpio = nombre.removeprefix("ING. ").removesuffix(".txt").lower()

print("Quitamos el sufijo:", nombrenosufijo)
print("Aqui el prefijo:", nombrenoprefijo)
print("Lo dejamos en limpio y minusculas:", limpio)
