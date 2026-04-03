# Solicite al usuario una frase y muestre la primera
# y la última letra de la frase.

# Solicitar frase
frase = input("Ingrese una frase: ")

# Obtener primera y última letra
primera = frase[0]  # el 0 ubica la primera letra
ultima = frase[-1]  # el -1 ubica la ultima letra
Letras = primera + ultima.replace(" ", "")  # une las letras

print("Primera letra:", primera)
print("Última letra:", ultima)
print("Primera y ultima letra juntas:", Letras)
