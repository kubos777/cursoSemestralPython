#################################################################################################
# Tarea 3 , Problema 1
# Escriba un programa Python para adivinar un número entre 1 y 9. 
# Nota: Se le pide al usuario que ingrese una conjetura. Si el usuario se equivoca, entonces
# el mensaje aparece de nuevo hasta que la suposición es correcta, con una conjetura exitosa, 
# el usuario obtendrá un mensaje de "bien adivinado" y el programa saldrá.
#################################################################################################
from random import randint
numAleatorio=randint(1,9)
while True:
	adivina=int(input("Adivina el número: "))
	if (numAleatorio==adivina):
		print("Bien adivinado")
		break
	else:
		print("Intenta otra vez!")
