Proceso division_dos_numeros
    Definir num1, num2 Como Real;
    Definir resultado Como Real;
    
    Escribir "Ingrese el primer número:";
    Leer num1;
    
    Escribir "Ingrese el segundo número:";
    Leer num2;
    
    Si num2 <> 0 Entonces
        resultado = num1 / num2;
        Escribir "La división es: ", resultado;
    Sino
        Escribir "Error: No se puede dividir por cero.";
    FinSi
FinProceso
