Algoritmo Numero_Valido
	Definir numer Como Entero;
	Escribir "Ingrese un número entre 1 y 10:";
	Leer numer;
	
	Mientras numer < 1 O numer > 10 Hacer
		
		si numer < 0 Entonces
			Escribir "Número inválido:";
			Escribir "Casi lo tienes solo debes ser mas positivo";
		FinSi
		si numer > 10 Entonces
			Escribir "Número inválido";
			Escribir "Estubistes tan cerca que lo unico que te falto fue " numer " - " numer " y sumarle por ejemplo " 10;
		FinSi
		si numer = 0 Entonces
			Escribir "vuelve a intentarlo";
		FinSi
		Escribir "Ingrese un número entre 1 y 10:";
		Leer numer;
	FinMientras
	
	Escribir "Número válido:", numer;
	
FinAlgoritmo