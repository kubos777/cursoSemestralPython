##################
#  Tipos numericos
##################

miNumero = 0
a = 10
b = -15
c = 2.5
d = 10j
e = 2j
print("Tipo de dato de a: ",type(a))
print("Tipo de dato de b: ",type(b))
print("Tipo de dato de c: ",type(c))
print("Tipo de dato de d: ",type(d))

print("a+b=",a+b)
print("a-b=",a-b)
print("a*c=",a*c)
print("a/b=",a/b)
print("a+d=",a+d)
print("d+e=",d+e)
print("j*j",1j*1j)

#El tamaño maximo de un entero es: 2^63-1 o 2^31-1 dependiendo de la arquitectura
#Se puede consutar en la constante sys.maxint 
#>>> sys.maxint 
#9223372036854775807

#enteroLargo=42L #Esta sintaxis solo es para python 2
#Sigue siendo un entero, pero ocupa más espacio en memoria
#Son como los long de C, cuando un entero crece más de su tamaño python 
#lo transforma en long para evitar el overflow  Ej:

#Python 2.7.5 (default, May 12 2013, 12:00:47)
#[GCC 4.8.0 20130502 (prerelease)] on linux2
#Type "help", "copyright", "credits" or "license" for more information.
#>>> import sys
#>>> print sys.maxint
#9223372036854775807
#>>> a = sys.maxint
#>>> print type(a)
#<type 'int'>
#>>> a +=1
#>>> print a
#9223372036854775808
#>>> print type(a)
#<type 'long'>

#En python 3 todos los enteros son long y sys.maxint ahora es sys.maxsize
#Revisar el siguiente enlace para más información: https://www.python.org/dev/peps/pep-0237/


#Para manejar otras bases se usa la siguiente notación:
octal=0o122
hexadecimal=0x9ff
binario=0b1111
#Hace las conversiones a decimal cuando los imprimimos
print("Octal %o = Decimal %d" %(octal,octal)) #82
print("Hexadecimal %x = Decimal %d" %(hexadecimal,hexadecimal)) #2589
print("Binario",bin(binario),"= Decimal %d" %(binario)) #15 

