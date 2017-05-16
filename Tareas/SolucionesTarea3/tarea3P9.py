#################################################################################################
# Tarea 3 , Problema 1
# Escriba un programa de Python que calcule el factorial de un número.
# Ejemplo: Factorial de 5 = 5 x 4 x 3 x 2 x 1 = 120
# NOTA: Factorial de 0 = 1.
#################################################################################################

n=int(input("Escriba el número a cual calcularle el factorial: "))
fact=1

if n<2 and n>=0:
	print("El factorial de %d es %d" % (n,1))
else:
	for i in range(1,n+1):
		fact*=i
	print("El factorial de %d es %d" % (n,fact))



