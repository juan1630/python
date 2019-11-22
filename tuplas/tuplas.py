# Una tupla es una lista que no se puede inmutar o modificar

# Se pueden extraer prociones de las lista
# No se pueden hacer busquedas, solo comprbar si el elementos esta dentro de la tupla
# Una tupla se ejecuta más rápido y ocupa menos espacio en memoria
# Formartean cadenas y utliar como clave en un diccionario

miTupla = ("Juan", "Katia", "Ivan", 24, "Juan")
miLista2 = ["Carlos", "Arutro"]

miLista = list(miTupla)
# convierte la tupla a una lista 

miTupla2 = tuple(miLista2)
# convierte la lista a una tupla

print(miTupla)
print (miTupla[0])
print (miTupla[1])
print(miLista)
print (miTupla2)

# Lo mismo que en las listas 
print("Juan" in miTupla ) 


# cuenta las veces que salen en la tupla

print( miTupla.count("Juan") )


# length mide la longitud de la tupla
print( len(miTupla) )


miTupla3 = "una", "tupla", "sin", "parentesis"
print(miTupla3)

# Desmepaquedo de la tupla

uno, dia, mes, anio = miTupla3

print(uno)
print(dia)
print(mes)
print(anio)

# En las ultimas versiones del python si se puede usar el metodo index
