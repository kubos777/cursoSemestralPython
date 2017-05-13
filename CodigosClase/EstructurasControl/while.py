### IMPLEMENTACIÓN DE LAS SENTENCIAS WHILE Y DO WHILE PARA EJECUTAR ### 
### UNA SERIE DE INSTRUCCIONES MIENTRAS SE CUMPLA ALGUNA CONDICIÓN. ###


# PROGRAMA QUE IMPRIME LOS NÚMEROS PARES ENTRE 0 Y 20 UTILIZANDO UN CICLO WHILE.
numero = 0					# Declaramos una variable número que inicialmente vale 0.
while numero < 20:			# Mientras la variable número sea menor a 20...
	numero = numero + 2		# ...incrementamos en 2 la variable número...
	print(numero)			# ...e imprimimos el valor del número.

# PROGRAMA QUE IMPRIME LOS NÚMEROS PARES ENTRE 0 Y 20 UTILIZANDO UNA IMPLEMENTACIÓN
# DEL CICLO "DO WHILE" Y LAS SENTENCIAS BREAK Y CONTINUE.
while True:					# Creamos un ciclo infinito. Dentro de él:
	numero = numero + 1		# Incrementamos en uno el valor del número.
	if numero % 2 == 1:		# Si el número es impar...
		continue 			# ...ignoramos el resto de las sentencias y 
							# nos saltamos un ciclo con la sentencia "continue".
	print(numero)			# Imprimimos el valor del número (si se entra al if anterior,
							# ésta y el resto de las sentencias serán ignoradas por un ciclo.)
	if numero == 20:		# Si el número ya llegó a 20...
		break 				# ...utilizamos la sentencia "break" para romper el ciclo infinito.