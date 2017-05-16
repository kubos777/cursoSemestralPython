#################################################################################################
# Tarea 3 , Problema 1
# Escriba un programa Python para encontrar los números que son divisibles por 7 y múltiplos de 5, 
# entre 1500 y 2700 (ambos incluidos). 
#################################################################################################

for numero in range(1500,2701,5):
	if numero % 7 == 0:
		print("> ",numero)



