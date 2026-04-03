# Solicite al usuario una frase y reemplace todas las apariciones de la palabra
# "Python" por "Programación" utilizando el método replace().

# Solicitar frase
frase = input("Dime una frase:")

# si en la frase hay alguna palabra "Python"
if "Python" in frase:
    intercambio = frase.replace("Python", "Programación")
print(intercambio)
