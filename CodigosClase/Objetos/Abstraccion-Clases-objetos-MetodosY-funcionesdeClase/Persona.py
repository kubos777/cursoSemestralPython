#*-* coding:utf-8*.*
class Persona:
	#Atributos de la clase, en este caso Persona
	edad=22
	saludo="Hola"

	#Vamos a crear un método que salude
	#Self hace referencia al objeto
	def saludar(self):
		print("%s, soy una persona"%self.saludo)
	#Las clases pueden tener funciones tambien
	def unaFuncion():
		print("Esto es una funcion de clase")
#Instanciar o crear un objeto de la clase
ricardo=Persona()
#Podemos acceder a los atributos de la clase por
#medio del operador "." (punto)
print(ricardo.edad)
print("Ricardo dice: ",ricardo.saludo)

ricardo.saludar()
Persona.unaFuncion()
print(Persona.edad)











