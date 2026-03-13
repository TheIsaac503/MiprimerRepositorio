# las comillas triples son las que se encargan de hacer
# Cadenas de texto largas sin mdoficar el formato.
# texto corto
cancion = (
    "solecito"
    "No sabes cuánto me haces falta"
    "Desde que te fuiste tengo frío"
    "Extraño tu calor por las mañanas"
    "Solecito"
    "Dame un rayito antes que te vayas"
    "Pa' guardarlo con mucho cariño"
    "Que te quedes siempre en mi alma"
    "Te lo pido"
    "¿Cuántas veces necesito repetirte que te necesito?"
    "Si te apagas, mi universo se apaga contigo"
    "Y los planetas de mi sistema se mueven sin sentido"
    "Todo colapsa, todo explota y se pierde en el vacío"
    "Y recuerdo cuando todo era lindo"
    "Cuando el sol aun brillaba y tu estabas conmigo"
    "Enamorados navegando en el espacio alegremente"
    "Dos estrellas destinadas a extrañarse para siempre"
)


# textos largos ''' o """
cancion1 = """Solecito
No sabes cuánto me haces falta
Desde que te fuiste tengo frío
Extraño tu calor por las mañanas
Solecito
Dame un rayito antes que te vayas
Pa' guardarlo con mucho cariño
Que te quedes siempre en mi alma
Te lo pido
¿Cuántas veces necesito repetirte que te necesito?
Si te apagas, mi universo se apaga contigo
Y los planetas de mi sistema se mueven sin sentido
Todo colapsa, todo explota y se pierde en el vacío
Y recuerdo cuando todo era lindo
Cuando el sol aun brillaba y tu estabas conmigo
Enamorados navegando en el espacio alegremente
Dos estrellas destinadas a extrañarse para siempre """


## computadora -> que variable queres imprimir
## print()
# void -> no devuelve nada
# odjeto -> devuelve un tipo de dato

## realizar una wiki tambien puede darle doble clic
##

#
cancion_Mayusculas = cancion.upper()
print(cancion_Mayusculas)


cancion_minusculas = cancion.lower()
print(cancion_minusculas)

## tiene que ingresar 100 nombres en mayuscula
mensaje = "hOlA kACe progRMando o qUe HaCe"
## Capitalize a que la primera letra de cada palabra sea mayuscula
mensajeCorrecto = mensaje.capitalize()
print(mensajeCorrecto)

## Las flipantess aventuras de el gato con bolson magico y alfredo
titulo = "Las flipantess aventuras de el gato con bolson magico y alfredo"
tituloCorrecto = titulo.title()
# print(tituloCorrecto)

## swapCase() permite cambiar entre mayusculas y minusculas
swapCaseTitulo = tituloCorrecto.swapcase()
print(swapCaseTitulo)

numero = "512"
solo_letras = "El chico del apartamentos "
Coro = "piribiribanban"

quieroSoloLetras = numero.isalpha()
print(quieroSoloLetras)
