########
# Tuplas
########

tupla=(1,"hola",True)
tupla2=(2,"a",[1,2,3])
tuplavacia=()
tuplaSingleton=(1,)#Tupla de un elemento, se tiene que poner la coma
#Ya que si no python lo toma como una expresión aritmética, solo seria un entero
print("Tipo de dato: ",type(tupla))
print("Indexacion: ",tupla[0])
print("Indexacion negativa: ",tupla[-1])
print("Tamaño: ",len(tupla))
print("Concatenación: ",tupla+tupla2)
print("Repetición: ",tupla*4)
print("Busqueda: ","a" in ("a","b","c"))
print("Iteracion: ")
for elemento in tupla:
	print("Elemento: ",elemento)

#asignacion por item no permitida porque es inmutable 
#tupla[0]=3 #Error
#Se puede modificar el elemento dentro de la tupla ya que la lista si permite la operación
tupla2[2][2]=4
print(tupla2)
#Asignación normal 
a,b=0,1
print(a,b)
#Empaquetamiento
tupla=1,2,3,4,5
print(tupla)
#Desempaquetamiento
a,b,c,d,e=tupla
print(a,b,c,d,e)
#a,b,c,d=tupla
#Esto causaría un error porque le faltan parametros para poder desempaquetar
tupla4= (1,3),"hola"
print(tupla4)
#En x se guarda la tupla (1,3) y en y la cadena "hola"
x,y=tupla4
print(x)
print(y)
