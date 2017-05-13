###########
# Conjuntos
###########


conjunto={1,2,2,3,4,5}
print("Tipo de dato: ",type(conjunto))
print(conjunto)

conjunto2=set([1,"A","B",2,1])
print(conjunto2) 
print("Tipo de dato: ",type(cadena))
print("Indexacion: ",cadena[0]) 
print("Indexacion negativa: ",cadena[-1])
print("Tamaño: ",len(cadena))
print("Concatenación: ",cadena+cadena2)
print("Repetición: ",cadena*4)

#Operaciones con conjuntos
print("Diferencia: ",conjunto-conjunto2)
print("Diferencia simetrica: ",conjunto^conjunto2)
print("Union: ",conjunto|conjunto2)
print("Interseccion: ",conjunto&conjunto2)
print("And: ",conjunto and conjunto2)
print("Or: ",conjunto or conjunto2)

conjunto=list(conjunto)
print(conjunto[0])