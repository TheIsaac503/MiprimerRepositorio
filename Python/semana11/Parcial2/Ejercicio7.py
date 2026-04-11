# Ejercicio 7
# 1. Toma el texto numérico "42".
# 2. Rellenalo con ceros a la izquierda hasta que alcance una
# longitud total de 5 caracteres.
# 3. Verifica mediante un método booleano si esa nueva cadena
# generada termina con el número "2".

numero = "42"
nuevo = numero.zfill(5)
resultado = nuevo.endswith("2")

print(nuevo)
print(resultado)
