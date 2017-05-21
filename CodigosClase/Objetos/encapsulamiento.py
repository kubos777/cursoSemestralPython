


#################
# Encapsulamiento
#################

class Animal:
	def __init__(self,nombre,especie,tipo):
		self.nombre=nombre    #publico
		self._especie=especie #protejido
		self.__tipo=tipo      #privado

	def setEspecie(self,especie):
		self._especie=especie

	def getEspecie(self):
		return self._especie

	def setTipo(self,tipo):
		self.__tipo=tipo

	def getTipo(self):
		return self.__tipo

animal=Animal("Lucho","Canino","Mamifero")
print("Nombre:",animal.nombre)
print("Especie:",animal._especie)
animal.setEspecie("Canidae")
animal.setTipo("Carnivoro")
print("Especie:",animal._especie)
#print("Tipo",animal.getTipo())
print("Tipo",animal._Animal__tipo)


