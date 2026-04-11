# si tenemos una variante
# clima = "caliente"

# numeroComprar = False
# numer2 = 50
# entrada = input("Como esta el ambiente? ")
# print("el clima es: ", entrada)

# if entrada == "frio":
# print("comprar cafesito")
# elif entrada == "caliente":
# print("comprar una soda fria")


# if numeroComprar == False:
# print("debes de trabajar para comprar un terreno para tus nietos")
# else:
# print("debes cuidar tus rodillas")

# and -> dos true
# or  ->  si tenemos un solo true

# if numer2 > 24 and numer2 < 30:
# print("El numero es mayor a 24 y menor a 30")
# elif numer2 > 30 and numer2 < 35:
# print("El numero es mayor a 30")
# elif numer2 > 35:
# print("El numero es mayor a 35 cliente vip")
# else:
# print("El numero es menor a 24")

# verifica un camino si este camino no esta deduce una opcion por decto

if edadNumero.type() == int:
    if edadNumero >= 18 and edadNumero < 25:
        print("Eres mayor de edad")
    if edadNumero >= 25 and edadNumero < 40:
        print("Eres un adulto joven")
    if edadNumero >= 40 and edadNumero < 80:
        print("Eres un adulto")
    if edadNumero >= 100:
        print("Marciano")
    else:
        print("no encontrado")
