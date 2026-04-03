# Solicite al usuario una frase y muestre si la frase empieza con la palabra "Hola".
# Puede utilizar el método startswith().

# Solicita frase
frase = input("Dime una frase: ")

# agrega una condicion de si la frase lleva "bella"
if "bella" in frase:

    # si la frase comienza con hola y lleva bella
    if frase.startswith("hola"):
        print("Hola amig@. Si, Muy bella")
    # si la frase no comienza con hola pero si tiene la palabra bella
    else:
        print("Si, Muy bella")

else:  # si la frase no inicia con hola y no lleva bella
    if frase.startswith("hola"):
        print("Buen escrito")
    else:
        print("Buen escrito")
