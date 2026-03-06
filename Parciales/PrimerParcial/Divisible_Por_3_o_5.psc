Algoritmo Divisible_Por_3_o_5
	Definir numer Como Entero;
	
	Repetir
		
		Escribir "Ingrese un número:";
		Leer numer;
		
	Si numer MOD 3 = 0 O numer MOD 5 = 0 Entonces
		Escribir Verdadero;
	SiNo
		Escribir Falso;
	FinSi
    Hasta Que numer MOD 3 = 0 O numer MOD 5 = 0
FinAlgoritmo