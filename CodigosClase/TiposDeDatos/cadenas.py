# -*- coding: utf-8 -*-
# La linea anterior sirve para indicar la codificación del archivo y poder usar carácteres como "ñ" o "á"
#########
# Cadenas
#########

cadena="hola"
cadena2=' mundo'
cadenaLarga="""Esta es una 
cadena larga
o cadenota a secas
"""
cadenaVacia=""
cadenaCruda=r"hola\n\t\r" #los carácteres especiales sí se imprimen 
cadenaUnicode=u"ñ|óíáíú" #para python2, en python 3 todas las cadenas son unicode
print("Tipo de dato: ",type(cadena))
print("Indexacion: ",cadena[0])
print("Indexacion negativa: ",cadena[-1])
print("Tamaño: ",len(cadena))
print("Concatenación: ",cadena+cadena2)
print("Repetición: ",cadena*4)
#asignacion por item no permitida por que son inmutables
#cadena[0]="H"
cadena="H"+cadena[1:4]
print(cadena)
print(cadenaCruda)
print(cadenaUnicode)
cadena3="alan"
#Operaciones con cadenas
print("Busqueda: ","Hola" in cadena)
print("Formateo de cadena: %s , %d" % (cadena, 4)) 
#Lista de identificadores: https://docs.python.org/3.4/library/string.html#format-specification-mini-language
print("Capitalización: ",cadena3.capitalize())
print("Mayúsculas: ",cadena3.upper())
print("Minúsculas: ",cadena3.lower())
print("Split de cadenas: ","hola hola hola".split())#se le puede pasar un parametro como separador






















