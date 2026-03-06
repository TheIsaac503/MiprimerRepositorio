Algoritmo Numeros_Pares
	Definir N, i, contador Como Entero;
	Definir continuar Como Logico;
	
	
	
	contador = 0;
	continuar = Falso;
	
	  Repetir
		Escribir "Ingrese la cantidad de números pares que desea ver:";
		Leer N;

	 si N >= 50 Entonces
		Escribir "Son muchos numeros";
	FinSi
	
	 Escribir " ¿No te parese un poco excesivo? (Verdadero/Falso)";
	 Leer continuar;
     Hasta Que no continuar = Verdadero;
     Escribir "Mala eleccion";
		Para i = 1 Hasta N*2 Hacer
			Si i MOD 2 = 0 Entonces
				Escribir i;
				contador = contador + 1;
			FinSi
		FinPara
		Escribir "sabia eleccion";
   
	
FinAlgoritmo