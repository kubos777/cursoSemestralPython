# -*- coding: utf-8 -*-
"""
def soy_una_funcion():
	Aquí dentro va el código que deseamos que realice la función 
	Para llamar a una función, solamente basta poner el nombre:
	así:  
soy_una_funcion()
"""		
def hola():
	print("Hola amigos del curso de python, soy una función!")

hola()	


def regresa():
	return "Soy el valor de retorno o regreso :3"

valor_regreso=regresa()

print(valor_regreso)

#Cuando una función regresa un valor, este puede ser asignado
#a una variable

def suma(a,b):
	return a+b

resultado= suma(2,3)
print(resultado)
print(suma(8,9))

