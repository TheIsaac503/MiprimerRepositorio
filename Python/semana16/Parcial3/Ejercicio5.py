# Ejercicio 5:
# Para cumplir con la normativa de privacidad, debes transformar
#  los nombres de los usuarios, invirtiendo su orden y formateando
#  la estructura de las letras.
# Pide al usuario su nombre completo (Nombre y Apellido).
# Conviértelo en una lista usando .split() y utiliza Slicing
# con paso negativo[::-1]) para que el apellido aparezca antes
#  que el nombre en una nueva lista.
# Implementa un for anidado:
# El primer bucle recorrerá las palabras de la lista invertida.
# El segundo bucle recorrerá cada letra de esa palabra.
# Imprime las letras de cada palabra separadas por un punto
# (ejemplo: S.o.r.t.o), creando una separación clara entre el
#  apellido y el nombre.

relle = "="
relle1 = " "

print(relle.center(65, "="))
print(relle.center(65, "="))
nombre = input("Ingrese su nombre completo: ")
print(relle.center(65, "="))
datos = nombre.title().split()

print("Tecnica del programador, cuarta postura. Dato Invetido")

print(relle.center(65, "="))
nombres = datos[:2]
apellidos = datos[2:]
resultado = apellidos + nombres

texto = " ".join(resultado)

for letra in texto:
    print(letra, end=".")

print()

print(relle.center(65, "="))
print(relle.center(65, "="))
