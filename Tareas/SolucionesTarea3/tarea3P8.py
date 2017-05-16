#################################################################################################
# Tarea 3 , Problema 1
# Escriba un programa de Python que imprima todos los números de 0 a 6 excepto 3 y 6.
# Nota: Utilice la instrucción 'continue'.
# Resultado esperado: 0 1 2 4 5
#################################################################################################

for n in range(0,7):
	if n == 3 or n == 6:
		continue
	else:
		print(n,"",end="")


