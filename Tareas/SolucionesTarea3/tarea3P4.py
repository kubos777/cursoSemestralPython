#################################################################################################
# Tarea 3 , Problema 1
# Escriba un programa de Python para construir el patrón siguiente, usando un bucle anidado.
#  * 
#  >>
#  * * * 
#  >>>>>>>> 
#  >>>>>>>> 
#  >>>>>>>> 
#  * * * 
#  >>
#  *
#################################################################################################
contador=0
for elemento in ["*",">>","***"]:
	print(elemento)
	if contador>=2:
		for i in range(3):
			print(">>>>>>>>")
			if contador>=4:
				print("***",">>","*",sep="\n")
			contador+=1	
	contador+=1

