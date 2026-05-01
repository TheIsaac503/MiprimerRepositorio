# Juego de carreras: for vueltas, if ganador, while repetir,
# select case pista.

repetir = "SI"


while repetir.upper() == "SI":
    relleno = "="
    print(relleno.center(30, "="))
    bien = "Bienvenido a Carreritas"
    print(bien.center(30, " "))
    relleno = "="
    print(relleno.center(30, "="))

    while True:
        print("Selecciona un Carro: ")
        print("1. Verde")
        print("2. Rojo")
        print("3. Azul")
        print("4. Celeste")
        print("5. Morado")
        carro = input("Elige el color de tu carro: ")
        carro = carro.strip().capitalize()

        if carro == "1" or carro == "Verde":
            relleno = "="
            print(relleno.center(30, "="))
            color = "Carro Verde"
            print(color.center(30, " "))
            relleno = "="
            print(relleno.center(30, "="))
            break
        elif carro == "2" or carro == "Rojo":
            relleno = "="
            print(relleno.center(30, "="))
            color = "Carro Rojo"
            print(color.center(30, " "))
            relleno = "="
            print(relleno.center(30, "="))
            break
        elif carro == "3" or carro == "Azul":
            relleno = "="
            print(relleno.center(30, "="))
            color = "Carro Azul"
            print(color.center(30, " "))
            relleno = "="
            print(relleno.center(30, "="))
            break
        elif carro == "4" or carro == "Celeste":
            relleno = "="
            print(relleno.center(30, "="))
            color = "Carro Celeste"
            print(color.center(30, " "))
            relleno = "="
            print(relleno.center(30, "="))
            break
        elif carro == "5" or carro == "Morado":
            relleno = "="
            print(relleno.center(30, "="))
            color = "Carro Morado"
            print(color.center(30, " "))
            relleno = "="
            print(relleno.center(30, "="))
            break
        else:
            nel = "Opción no válida"
            print(nel.center(30, " "))

    while True:
        print("Selecciona la pista: ")
        print("1. Ciudad")
        print("2. Desierto")
        print("3. Montaña")
        print("4. Pantano")
        print("5. Nieve")
        pista = input("Pista: ")
        pista = pista.strip().capitalize()

        match pista:
            case "1" | "Ciudad":
                relleno = "="
                print(relleno.center(30, "="))
                paisaje = "Ciudad"
                print(paisaje.center(30, " "))
                print(relleno.center(30, "="))
                break

            case "2" | "Desierto" | "Decierto":
                relleno = "="
                print(relleno.center(30, "="))
                paisaje = "Desierto"
                print(paisaje.center(30, " "))
                print(relleno.center(30, "="))
                break

            case "3" | "Montaña" | "Montana":
                relleno = "="
                print(relleno.center(30, "="))
                paisaje = "Montaña"
                print(paisaje.center(30, " "))
                print(relleno.center(30, "="))
                break

            case "4" | "Pantano":
                relleno = "="
                print(relleno.center(30, "="))
                paisaje = "Pantano"
                print(paisaje.center(30, " "))
                print(relleno.center(30, "="))
                break

            case "5" | "Nieve":
                relleno = "="
                print(relleno.center(30, "="))
                paisaje = "Nieve"
                print(paisaje.center(30, " "))
                print(relleno.center(30, "="))
                break

            case _:
                relleno = "="
                print(relleno.center(30, "="))
                print("Opción no válida".center(30, " "))
                print(relleno.center(30, "="))

    while True:
        vueltas = int(input("Del 1 al 7 ¿Cauntas vueltas quieres que hagan? "))
        if vueltas < 8:
            relleno = "="
            print(relleno.center(30, "="))
            margen = "Estas en el margen"
            print(margen.center(30, " "))
            relleno = "="
            print(relleno.center(30, "="))
            break
        else:
            relleno = "="
            print(relleno.center(30, "="))
            margen = "Estas fuera del margen"
            print(margen.center(30, " "))
            relleno = "="
            print(relleno.center(30, "="))

    import random

    if pista == "1" or pista == "Ciudad":
        carro = (
            "Carro Verde",
            "Carro Rojo",
            "Carro Azul",
            "Carro Celeste",
            "Carro Morado",
        )
        probabilidades = (0.2, 0.1, 0.2, 0.2, 0.3)

    elif pista == "2" or pista == "Desierto":
        carro = (
            "Carro Verde",
            "Carro Rojo",
            "Carro Azul",
            "Carro Celeste",
            "Carro Morado",
        )
        probabilidades = (0.2, 0.2, 0.2, 0.3, 0.1)

    elif pista == "3" or pista == "Montaña":
        carro = (
            "Carro Verde",
            "Carro Rojo",
            "Carro Azul",
            "Carro Celeste",
            "Carro Morado",
        )
        probabilidades = (0.2, 0.2, 0.3, 0.2, 0.1)

    elif pista == "4" or pista == "Pantano":
        carro = (
            "Carro Verde",
            "Carro Rojo",
            "Carro Azul",
            "Carro Celeste",
            "Carro Morado",
        )
        probabilidades = (0.3, 0.1, 0.2, 0.2, 0.2)
    elif pista == "5" or pista == "Nieve":
        carro = (
            "Carro Verde",
            "Carro Rojo",
            "Carro Azul",
            "Carro Celeste",
            "Carro Morado",
        )
        probabilidades = (0.2, 0.3, 0.1, 0.2, 0.2)
    else:
        print("Pista no válida")

    for i in range(1, vueltas + 1):
        print(f"Vuelta {i}")

    ganador = random.choices(carro, weights=probabilidades)[0]

    if color == ganador:

        relleno = "="
        print(relleno.center(30, "="))
        feli = "Felicidades Ganastes"
        print(feli.center(30, " "))
        relleno = "="
        print(relleno.center(30, "="))
    else:
        relleno = "="
    print(relleno.center(30, "="))
    nofeli = "Perdistes"
    print(nofeli.center(30, " "))
    elgama = "El Ganador es: " + ganador
    print(elgama.center(30, " "))
    relleno = "="
    print(relleno.center(30, "="))

    repetir = input("¿Deseas repetir la carrera? (SI/NO): ")

print("Juego terminado")
