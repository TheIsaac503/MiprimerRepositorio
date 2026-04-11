# Ejercicio 4
# . Toma la palabra "CANTANDO".
# 2. Convierte toda la cadena a letras minusculas.
# 3. Elimina el sufijo "ando" de la palabra resultante y
# encuentra en que indice (posicion) quedo la letra "t".

texto = "CANTANDO"

textominus = texto.lower()
textosinsufijo = textominus.replace("ando", "")
indicet = textosinsufijo.find("t")

print("Texto final:", textosinsufijo)
print("Índice de 't':", indicet)
