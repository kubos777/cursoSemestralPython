##############
# Diccionarios
##############

diccionario={1:"uno",2:"dos",3:"Tres"}
print("Tipo de dato:",type(diccionario))
print("Accediendo mediante la llave ",diccionario[1])
diccionario[4]="cuatro"
print(diccionario)
#Cuando se usa una llave existente se modifica su valor 
diccionario[4]="four"
print(diccionario)
#La lista no se puede usar como llave
#diccionario[[1,2,4]]="numeros"
calificaciones={
	"alan":9,
	"juan":7,
	"paco":5
}
print("Calificacion de alan: ",calificaciones["alan"])
print("Calificacion de alan: ",calificaciones.get("alan"))
#Usar una llave inexistente arrojará un error de KeyError
#print("Calificacion de pedro: ",calificaciones["pedro"])
#Usando la función get podemos dar un valor por default
#Este valor no se agrega al diccionario
print("Calificacion de pedro: ",calificaciones.get("pedro",0))
#Esto causara un KeyError
print(calificaciones["pedro"])
#para agregar un valor al diccionario
calificaciones.update({"pedro":6})
print(calificaciones["pedro"])
#o la modficacion de un valor existente
calificaciones.update({"juan":8})
print(calificaciones["juan"])


#Para iterar usamos los metodos keys() o values() que nos regesan iteradores
valores=calificaciones.values()
llaves=calificaciones.keys()
#Podemos hacer uso para la búsqueda 
if("alan" in calificaciones.keys()):
	print("La calificacion es: ",calificaciones["alan"])

print("Iteracion: ")
for llave in diccionario.keys():
	print("LLave:",llave,"Valor",diccionario[llave])


