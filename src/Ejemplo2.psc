Algoritmo  Ejemplo2
	Definir cajero, CuentaDeAhorro,numeroDeCuenta, cantidadSaliente, saldo, preguntar Como Entero;
	CuentaDeAhorro = 1000;
	numeroDeCuenta = 12345;
	
	Escribir " bienvenido";
	Escribir " Actividad que desea realizar";
	Escribir " 1 para consultar";
	Escribir " 2 para extraer dinero de la cuenta de ahorro";
	
	Escribir " Escriba el numero de cuenta al operar";
	Leer preguntar; // yo no quiero ser un uno mejor busco otra chamba
	
	si preguntar == 1;
		Escribir " Escriba el numero de cuenta a operar";
		Leer preguntar; // es valor den numero de cuentas
		
		si preguntar == numeroDeCuenta
			Escribir " Su saldo es " CuentaDeAhorro;
		FinSi
	FinSi
	
	si preguntar == 2;
		Escribir " Escriba el numero de cuenta a operar";
		Leer preguntar; // es valor den numero de cuentas
		si preguntar == numeroDeCuenta
			Escribir " Escriva el monto a extraer";
			Leer preguntar;
			
			si preguntar <= CuentaDeAhorro
				saldo = CuentaDeAhorro - preguntar;
				Escribir  "procesando";
				Escribir "Su saldo actual es de ";
			FinSi
		FinSi
	FinSi
	// or o puedes llevar panes con cafe o chocolate
	// and puedes llevar carne y jamon
	// not mejor no
	
	
	// no puede comenzar con
	// numero
	// signos a manenos que sea _
	// no debe llevar espacio 
	// si es una calse siempre inicia con Mayusculas
	// es evitar el codigo espaguetic
	
FinAlgoritmo

