### IMPLEMENTACIÓN DE LA SENTENCIA IF / ELSE PARA VALIDAR UNA CONDICIÓN. ###

# PROGRAMA QUE DICE SI UN NÚMERO INGRESADO POR EL USUARIO ES PAR O IMPAR.
numero = int(input("Ingresa un número: "))	# Se ingresa un número desde teclado con la función "input()".
											# El número ingresado es convertido a entero mediante la función "int()".
											# El número, ya convertido, se almacena en una variable "numero".

residuo = numero % 2	# Calculamos el residuo de dividir el número ingresado entre dos.
						# El resultado se almacena en una variable "residuo".

if residuo == 0: 				# Si el residuo es 0...
	print(numero,"es par.")		# ...imprimimos que el número ingresado es par.
else:							# En caso contrario (residuo diferente de 0)...
	print(numero,"es impar")	# ...imprimimos que el número ingresado es impar.