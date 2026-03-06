Algoritmo Mayor_Y_Menor
	Definir numer1, numer2 Como Entero;
	
	Escribir "Ingrese el primer número:";
	Leer numer1;
	
	Escribir "Ingrese el segundo número:";
	Leer numer2;
	
	Si numer1 > numer2 Entonces
		Escribir "El primer número mayor es: ", numer1;
		Escribir "El segundo número menor es: ", numer2;
	SiNo
		Si numer2 > numer1 Entonces
			Escribir "El segundo número mayor es: ", numer2;
			Escribir "El el primer número menor es: ", numer1;
		SiNo
			Escribir "Los dos números son iguales";
		FinSi
	FinSi
	
FinAlgoritmo