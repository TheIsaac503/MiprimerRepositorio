Proceso Sumar
	// Solicitar al usuario
	// que ingrese dos números enteros
	// y mostrar la suma de ambos.
	Definir NumeroEntrada1, NumeroEntrada2, Total Como Entero;
	Escribir 'Ingrese un numero para sumar ';
	Leer NumeroEntrada1;
	Escribir 'Ingrese un numero para sumar ';
	Leer NumeroEntrada2;
	// Las condicones logicas son las que nos va a decir si es verdadero o falso
	// and
	// or
	// not >
	Si NumeroEntrada1>0;
		Total = NumeroEntrada1 + NumeroEntrada2;
	FinSi
	Escribir ' El total de la suma es ', total;
FinProceso
