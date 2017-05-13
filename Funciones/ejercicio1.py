# -*- coding: utf-8 -*-

def datos():
	datos=[]
	nombre=str(input("Ingresa tu nombre: "))
	datos.append(nombre)
	apMat=str(input("Ingresa tu apellido paterno: "))
	datos.append(apMat)
	apPat=str(input("Ingresa tu apellido materno: "))
	datos.append(apPat)
	direc=str(input("Ingresa tu dirección: "))
	datos.append(direc)
	numTel=int(input("Ingresa tu número de teléfono: "))
	datos.append(numTel)
	numCel=int(input("Ingresa tu número de celular: "))
	datos.append(numCel)
	numCta=int(input("Ingresa tu número de cuenta: "))
	datos.append(numCta)
	return datos

datos_recibidos=datos()
print(datos_recibidos)

def formato(lista):
	print("Datos sin formato: ",lista)
	print("Datos con formato: ")

	for i in lista:
		print(lista.index(i),i)

formato(datos_recibidos)





