# Solicite al usuario una frase y verifique si la frase termina con un punto ".".
# Puede utilizar el método endswith().

# Solicita una frase
frase = input("Dime una frase: ")

if frase.endswith("."):
    print("La frase termina con '.'")

else:
    print("La frase no termino con '.'")
