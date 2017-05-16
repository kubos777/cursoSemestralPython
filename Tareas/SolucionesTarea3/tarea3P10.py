#################################################################################################
# Tarea 3 , Problema 1
# Escriba un programa de Python que solicite una cadena al usuario e imprima la misma cadena omitiendo todas sus vocales.
# EJEMPLO: Entrada: "¡Hola, mundo!" - Salida: "¡Hl, mnd!"
#################################################################################################

cadena=input("Escriba la cadena a la cual remover las vocales: ")
sinVocales=""
for c in cadena:
	if c not in ["a","e","i","o","u"]:
		sinVocales+=c
print("La cadena sin vocales es: ",sinVocales)
#En una línea B|
#print("La cadena sin vocales es: ",''.join(c for c in cadena if  c not in 'aeiou'))







