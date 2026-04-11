# Ejercicio 1
# 1. Declara una variable con la cadena "  elefante  ".
# 2. Utiliza el método correspondiente para eliminar los espacios en blanco a ambos extremos de la palabra.
# 3. Cuenta y muestra cuántas veces se repite la letra "e" en el texto ya limpio.

texto = "  elefante  "
textolimpio = texto.strip()

cantidad = textolimpio.count("e")

print("Texto limpio:", textolimpio)
print("Cantidad de 'e':", cantidad)
