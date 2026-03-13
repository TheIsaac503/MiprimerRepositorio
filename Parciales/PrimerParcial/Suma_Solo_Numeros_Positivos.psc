Algoritmo Suma_Solo_Numeros_Positivos
	Definir numer, suma Como Entero;
	
	suma = 0;
	
	Repetir
		Escribir "Ingrese un número: ";
		Leer numer;
		
		Si numer >= 0 Entonces
			suma = suma + numer;
		FinSi
		si numer = 0 Entonces
			Escribir "Elige un numero que no sea ", numer, " Por Favor";
		FinSi
		si numer < 0 Entonces
			Escribir "Pudimos seguir, pero desidiste pasarte al lado negativo con " , numer;
		FinSi
		
	Hasta Que numer < 0
	
	Escribir "La suma de los números positivos es: ", suma;
	
FinAlgoritmo