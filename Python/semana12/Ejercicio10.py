# Ejercicio 10:
# Pide usuario y contraseña. Si ambos coinciden con valores
# predefinidos, muestra "Acceso permitido", de lo contrario
# "Acceso denegado".

Usuario = "TheIsaac503"
contra = 12345678

print("Bienvenido tienes tres intentos")

for i in range(3):
    entrar = input("Usuario: ")
    contra1 = int(input("Contraseña: "))

    if entrar == Usuario and contra1 == contra:
        print("Bienvenido TheIsaac503")
    else:
        print("Usuario no encontrado")
else:
    print("Acceso denegado")
