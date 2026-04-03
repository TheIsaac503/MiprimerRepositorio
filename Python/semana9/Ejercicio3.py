# Solicite al usuario una frase y muestre cuántas letras tiene la frase sin contar los espacios.
# Puede utilizar el método replace() para eliminar los espacios.

# Solisitar frase
frase = input("Dime una frase: ")

# Eliminar los espacios
frase_sin_espacios = frase.replace(" ", "")

# Contar los caracteres
cantidad = len(frase_sin_espacios)

print("Frase sin espacios:", frase_sin_espacios)
print("Cantidad de letras (sin espacios):", cantidad)
