# Cree un programa que solicite un nombre completo
# y lo separe en palabras utilizando el método split().
# Luego muestre cada palabra en una línea diferente.

# Solicitar nombre
nombre = input("Ingrese su nombre completo: ")

# Separar en palabras
palabras = nombre.split()

# Cada palabra en una línea diferente
for palabra in palabras:
    print(palabra)
