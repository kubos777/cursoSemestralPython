### IMPLEMENTACIONES DE LA SENTENCIA ELIF PARA VALIDAR MÚLTIPLES CONDICIONES. ### 


# PROGRAMA QUE SOLICITA UN NÚMERO AL USUARIO Y DA CARACTERÍSTICAS SOBRE ÉL.
numero = int(input("Ingresa un número menor a 10")) # Se solicita un número menor a 10 al usuario
													# y se almacena en la variable "numero".

if numero < 10:							# Si el número es menor a 10 verificamos...
	if numero == 4 or numero == 9:			# ...si el número es un 4 o un 9
		print(numero, "tiene raiz exacta.")	# imprimimos que el número tiene raiz exacta.
	elif numero % 2 == 0:					# ...si el número es par
		print(numero, "es par.")			# imprimimos que el número es par.
	elif numero == 1 or numero == 3 or numero == 5 or numero == 7:	# ...si el número es 1 o 3 o 5 o 7
		print(numero, "es primo.")			# imprimimos que el número es primo.
	else:									# ...si no es ninguno de los casos anteriores
		print(numero, "es negativo.")		# imprimimos que el número es negativo.
else:									# Si el número no es menor a 10 ...
	print("¡Dijimos que menor a 10!")	# ...sólo imprimimos que el número no es menor que 10.



# PROGRAMA QUE CALCULA EL IMC A PARTIR DEL PESO Y ESTATURA Y DICE EL ESTADO DE LA PERSONA.
import math		# Importamos un módulo con múltiples funciones matemáticas.
estatura = float(input("Ingresa tu estatura en metros: "))	# Solicitamos una estatura al usuario,
															# convertimos la entrada a float
															# y la almacenamos.

peso = float(input("Ingresa tu peso en kg: ")) 	# Solicitamos un peso al usuario, convertimos
												# la entrada a float y la almacenamos.

imc = peso/pow(estatura, 2)	# Calculamos el IMC y lo almacenamos en la variable "imc".
							# Con la función "pow()" elevamos un número a una potencia.
							# Para utilizarla, debemos importar el módulo "math".

if imc < 18.5:				# Si el imc es menor a 18.5...
	print("Desnutrición.")	# ...imprimimos el estado que corresponde.
elif imc < 25:				# Si no es menor a 18.5, verificamos si el imc es menor a 25...
	print("Peso normal.")	# ...e imprimimos el estado que corresponde.
elif imc < 30:				# Si no es menor a 25, verificamos si el imc es menor a 30...
	print("Sobrepeso.")		# ...e imprimimos el estado que corresponde.
elif imc >= 30:				# Si no es menor a 30, verificamos si el imc es mayor o igual a 30...
	print("Obesidad.")		# ...e imprimimos el estado correspondiente.

#NOTAS:
# Dependiendo de nuestra forma de resolver el problema, podemos omitir la sentencia "else" o "elif",
# sin embargo, el "if" nunca se debe omitir si queremos hacer comparaciones.
