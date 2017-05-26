#*-* coding:utf-8*.*
class Persona3:
	#Definimos el constructor
	def __init__(self,nombre1,apellido1,edad1,estatura1,dinero):
		self.nombre=nombre1
		self.apellido=apellido1
		self.edad=edad1
		self.estatura=estatura1
		self.dinero=dinero
		print("Hola soy ",self.nombre," ",self.apellido,",tengo",self.edad,"años y mido ",self.estatura)	
		print("Tengo $ ",self.dinero,"en mi cuenta")
		#Termina el constructor
		#Definimos métodos de la clase
	def comer(self,comida):
		print("Hola soy ",self.nombre,"y estoy comiendo: ",comida)
	def informarSaldo(self):
		print("Soy ",self.nombre,"y actualmente tengo $ ",self.dinero," pesitos en mi cuenta.")
	def prestarDinero(self,monto,destinatario):
		self.informarSaldo()
		destinatario.informarSaldo()

		self.dinero=self.dinero-monto
		destinatario.dinero=destinatario.dinero+monto
		self.informarSaldo()
		destinatario.informarSaldo()
		#Función de la clase
	def regalarDinero(donacion,donador,destinatario):
		donador.informarSaldo()
		destinatario.informarSaldo()

		donador.dinero=donador.dinero-donacion
		destinatario.dinero=destinatario.dinero+donacion

		donador.informarSaldo()
		destinatario.informarSaldo()


ricardo=Persona3("Ricardo","Singer",20,1.80,1000)
jorge=Persona3("Jorge","Chávez",21,1.70,5)

print(ricardo.edad)


print(jorge.dinero)
jorge.informarSaldo()
jorge.comer(", nada porque no tengo dinero")

ricardo.prestarDinero(500,jorge)
print("------------------------------------")
Persona3.regalarDinero(200,ricardo,jorge)
