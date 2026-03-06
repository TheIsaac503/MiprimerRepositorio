Algoritmo Positivo_o_menor_a_100
	Definir numer Como Entero;
	
	Escribir "Bienvenido quieres saber si tu numero es positivo o menor a 100";
	
	Repetir
		
	Escribir "Ingrese un número:";
	Leer numer;
	
	Si numer > 0 Y numer < 100 Entonces
		Escribir "Su numero cumple con las condiciones por lo cual es"; 
		Escribir Verdadero;
	SiNo
		si numer < 0 Entonces
			Escribir "Este numero es negativo por lo cual es:";
		FinSi
		si numer >100 Entonces
			Escribir "Aunque es positivo, no cumple con ser menor que 100  por lo cual es:";
		FinSi
		Escribir Falso;
	FinSi
Hasta Que numer > 0 Y numer < 100
	
FinAlgoritmo