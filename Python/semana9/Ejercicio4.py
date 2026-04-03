# Cree un programa que solicite un correo electrónico
# y verifique si contiene el símbolo @.
# Si lo contiene, muestre el mensaje: "El correo parece válido".
# Si no lo contiene, muestre el mensaje: "El correo no es válido".

# Solicitar correo
correo = input("Dime tu correo: ")

# Si contiene el @
if "@" in correo:
    print("Correo valido")
# Si no contiene el @
else:
    print("Correo invalido")
