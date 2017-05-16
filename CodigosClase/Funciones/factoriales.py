###########
# Funciones
###########

#Con una función iterativa hacemos uso de las estructuras de control (ciclos)
def factorialIter(n):
	acum=1
	if n==1 or n==0:
		return 1
	else:
		for num in range(1,n+1):
			acum=acum*num
			#acum*=num #Sintaxis reducida para la linea de arriba
		return acum

print("El factorial de %d es %d" %(0,factorialIter(0)))
print("El factorial de %d es %d" %(1,factorialIter(1)))
print("El factorial de %d es %d" %(2,factorialIter(2)))
print("El factorial de %d es %d" %(3,factorialIter(3)))
print("El factorial de %d es %d" %(4,factorialIter(4)))
print("El factorial de %d es %d" %(10,factorialIter(10)))

def factorialRec(n):
	if n<2:
		return 1
	return n*factorialRec(n-1)

print("El factorial de %d es %d" %(0,factorialRec(0)))
print("El factorial de %d es %d" %(1,factorialRec(1)))
print("El factorial de %d es %d" %(2,factorialRec(2)))
print("El factorial de %d es %d" %(3,factorialRec(3)))
print("El factorial de %d es %d" %(4,factorialRec(4)))
print("El factorial de %d es %d" %(10,factorialRec(10)))
#Hay que tener cuidado con el limite de recursiones que maneja python
print("El factorial de %d es %d" %(998,factorialRec(998)))
#Se puede consultar con el metodo sys.getrecursionlimit()

#Debemos tener cuidado también con las llamadas recursivas dobles, ya que se acaban
#el stack de llamadas el doble de rápido
def fibo(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibo(n-1)+fibo(n-2)
		
print("El fibonacci de %d es %d" %(0,fibo(0)))
print("El fibonacci de %d es %d" %(1,fibo(1)))
print("El fibonacci de %d es %d" %(2,fibo(2)))
print("El fibonacci de %d es %d" %(3,fibo(3)))
print("El fibonacci de %d es %d" %(10,fibo(10)))
print("El fibonacci de %d es %d" %(500,fibo(500)))










































