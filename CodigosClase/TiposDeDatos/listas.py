########
# Listas
########

lista=["hola",4,10.5,True]
lista2=["a",10,[1,2,3]]

print("Tipo de dato: ",type(lista))
print("Indexacion: ",lista[0])
print("Indexacion negativa: ",lista[-1])
print("Tamaño: ",len(lista))
print("Concatenación: ",lista+lista2)
print("Repetición: ",lista*4)
#asignacion por item permitida por que son mutables
lista[0]="H"
print(lista[0])
print("Busqueda: ","H" in lista)
print("Elemento en una sublista: ",lista2[2][0])
print("Iteracion: ")
lista=["A","B","C","D"]
lista2=[0,1,2,3,4,5,6]
listaVacia=[]
for elemento in lista:
	print("Elemento: ",elemento)
print("Slicing: ",lista[1:3])
print("Slicing con salto: ",lista2[::2])
print("Invertir una lista: ",lista2[::-1])
#operaciones
lista.append("E")
print(lista)
lista.insert(0,"Z")
print(lista)
#Elimina el ultimo elemento y lo regrsa
utlimoElemento=lista.pop()
print(utlimoElemento)
primerElemento=lista.pop(0)
print(primerElemento)
print(lista)
#Elimina el elemento del indice y no lo regresa
del lista[-1]
print(lista)
#quita la primera ocurrencia
letraA=lista.remove("A")
print(lista)
lista3=["a","s","k","b","Z","p"] 
#Todos los elementos tienen que ser del mismo tipo
#Error -> print(max([1,2,3,10,"a"]))
print("Máximo de una lista:",max([1,2,3,10]))
print("Mínimo de una lista:",min([1,2,3,10]))
#Ordenamiento
lista3.sort()
print(lista3)
lista3.reverse()
print(lista3)
print("Indice de un elemento: ",lista3.index("k"))

#Mucho cuidado con las referencias a los objetos mutables
a=[1,2,3,4,5]
b=a #no es una copia
#si hacemos esto
a.reverse()
print(a)
print(b)
#Demostrando que es la misma referencia en memoria
print(a is b)#es lo mismo que id(a)==id(b)
#Para una copia de un objeto mutable podemos usar el modulo copy
import copy
c=copy.copy(a)
print(a)
print(c)
a.reverse()
#Otras opciones es hacer un slice de inico a fin nuevalista=lista[:]
#o devolver con el bulit in nuevalista=list(lista)




















