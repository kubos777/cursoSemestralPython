### IMPLEMENTACIÓN DE LA SENTENCIA FOR Y LA FUNCIÓN RANGE() PARA ###
### REPETIR UN BLOQUE DE CÓDIGO UN NÚMERO DETERMINADO DE VECES.  ###


# PROGRAMA QUE IMPRIME LOS NÚMEROS IMPARES ENTRE 0 Y 20 UTILIZANDO UN CICLO FOR, RANGE() Y CONTINUE.
for numero in range(0,21): 	# Por cada número en un rango entre el 0 y el 20
	if numero % 2 == 0:		# Si dicho numero es un número par...
		continue 			# ...nos brincamos un ciclo utilizando continue.
	print(numero)			# Se imprime el valor actual del número.

#NOTAS:
# Recordemos que la función range() nos genera un iterable desde su primer argumento hasta
# el número que le pasemos como segundo argumento menos 1. 
# Ej. range(0,3) = [0,1,2].