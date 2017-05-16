#################################################################################################
# Tarea 3 , Problema 1
# Escriba un programa Python para contar el número de números pares e impares de una serie de números. 
# Números de muestra : números = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Salida esperado :
# Número de números pares: 5
# Número de números impares: 4
#################################################################################################

numeros=(1, 2, 3, 4, 5, 6, 7, 8, 9)
pares=0
impares=0
for n in numeros:
	if n % 2 == 0:
		pares+=1
	else:
		impares+=1
print("Número de números pares: ",pares)
print("Número de números impares: ",impares)


