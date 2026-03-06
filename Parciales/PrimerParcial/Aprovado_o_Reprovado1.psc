Algoritmo Aprovado_o_Reprovado
	Definir nota Como Entero;
	
	Escribir "Ingrese la nota del estudiante (0 a 10): ";
	Leer nota;
	
	Si nota >= 0 Y nota <= 10 Entonces
		
		Si nota >= 6 Entonces
			Escribir "Aprobado";
		SiNo
			Si nota <= 4 Entonces
				Escribir "Reprobado";
			SiNo
				Escribir "Recuperación";
			FinSi
		FinSi
		
	SiNo
		Escribir "Nota inválida";
	FinSi
	
FinAlgoritmo