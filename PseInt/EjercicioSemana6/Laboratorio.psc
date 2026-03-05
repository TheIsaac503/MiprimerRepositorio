Algoritmo Sumar_Hasta_Numero_Impar
	
	Definir numero Como Entero;
	Definir total Como Entero;
	
	total = 0;
	
	Repetir
		Escribir "Ingrese un numero:";
		Leer numero;
		
		total = total + numero;
		
		Escribir "Total acumulado: ", total;
		
	Hasta Que numero MOD 2 <> 0
	
	Escribir "Se ingreso un numero impar.";
	Escribir "Total final: ", total;
	
FinAlgoritmo