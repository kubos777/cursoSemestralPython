### IMPLEMENTACIÓN DE UN SWITCH-CASE UTILIZANDO LO VISTO HASTA AHORA. ###

# PROGRAMA QUE SIMULA UN PEQUEÑO MENÚ DE OPCIONES.
opciones = {1:"Caso 1", # Creamos un diccionario con 3 llaves de tipo entero,
			2:"Caso 2",	# cada una con un valor de tipo cadena.
			3:"Salir"}
llaves = list(opciones.keys())	# Generamos una lista con las llaves del diccionario
llaves.sort()					# Ordenamos la lista de llaves.
	
while True:					# Creamos un ciclo infinito.
	print("Menú:")		
	for llave in llaves:	# Por cada llave en la lista de llaves...
		print("\t%s - %s" % (llave, opciones[llave]))	# ...imprimimos cada llave y su valor.
	seleccion = int(input("Selecciona un caso: "))		# Solicitamos al usuario que ingrese
														# el valor de una de las llaves.
	if seleccion in llaves:			# Si la selección está en la lista de llaves...
		print(opciones[seleccion])	# ...imprimimos la opción correspondiente en el diccionario.
		if seleccion == 3:			# ...si la selección es un 3 (salir)...
			break					# ...salimos del ciclo infinito utilizando un "break".
	else:							# Si la selección no está en la lista de llaves...
		print("(Default) Ingresa una opción válida")	# ...se notifica al usuario. 

