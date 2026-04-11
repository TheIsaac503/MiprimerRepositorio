# Ejercicio 5
# 1. Inicia con la cadena "pYTHON".
# 2. Invierte las mayusculas por minusculas y las minusculas por mayusculas.
# 3. Alinea este nuevo texto hacia la izquierda en un espacio de
# 15 caracteres, rellenando los espacios vacios con asteriscos ("*").


texto = "pYTHON"
textoinvertido = texto.swapcase()
textofinal = textoinvertido.ljust(15, "*")

print(textofinal)
