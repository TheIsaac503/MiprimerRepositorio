# Ejercicio 8
# 1. Define un bloque de texto de 3 lineas usando comillas triples
# (puedes usar un fragmento del poema de la guia).
# 2. Cuenta cuantas veces aparece la letra "a" en todo el bloque
# de texto.
# 3. Divide el bloque de texto por sus saltos de linea (splitlines)
#  para convertirlo en una lista de oraciones independientes.

poema = """Es porque un pajarito de la montaña ha hecho
en el hueco de un árbol, su nido matinal,
que el árbol amanece con música en el pecho,
como que si tuviera corazón musical."""

cantidad = poema.count("a")
print("El total de A que hay es de", cantidad)
lineas = poema.splitlines()
print(lineas)
