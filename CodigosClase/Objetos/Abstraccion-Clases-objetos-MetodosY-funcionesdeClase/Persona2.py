#*-* coding:utf-8*.*
class Persona2:
	#Definimos el constructor
	#Esto se va a ejecutar cada instancia, es decir, 
	#cada que se  cree un objeto
	def __init__(self):
		print("Se ha creado una persona, y se imprime este mensaje")
	#Creamos unos cuantos métodos
	def saludar(self):
		print("Hola soy una persona")
	def comer(self):
		print("Estoy comiendo, no molestar")
	def estudiar(self):
		print("Estoy aprendiendo POO")
#Hacemos instancias de la clase Persona
#Cada objeto tiene lo que tiene dentro el constructor
daniel=Persona2()
jorge=Persona2()
ricardo=Persona2()

daniel.comer()
jorge.saludar()
ricardo.estudiar()