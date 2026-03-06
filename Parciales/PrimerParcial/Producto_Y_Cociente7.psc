Algoritmo Producto_Y_Cociente
	Definir numer1, numer2, producto, cociente Como Real;
	
	Escribir "Ingrese el primer número:";
	Leer numer1;
	
	Escribir "Ingrese el segundo número:";
	Leer numer2;
	
	producto = numer1 * numer2;
	cociente = numer1 / numer2;
	
	Si numer2 <> 0 Entonces
		Escribir "El producto es: ", producto;
		Escribir "El cociente es: ", cociente;
	SiNo
		Escribir "El producto es: ", producto;
		Escribir "No se puede dividir entre cero";
	FinSi
	
FinAlgoritmo