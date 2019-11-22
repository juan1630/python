miLista = ["Juan", "Katia", "Pirata", "Ivan", 5, True, 68.5]

# Se puede imprimir de está forma la lista 
print(miLista)

# O de esta otra forma 
print(miLista[:]) 

#Ambas son correctas
print(miLista[2])

# Se accede al indice
# Si se accede a un indice que no se encuentre dará una excepción, ya que no existe 
#print(miLista[9])


print(miLista[-2])

# Procion de la lista 


print(miLista[0:2])

#Imprime los del indice 0 al indice 2, se excluyen los demas valores de la lista

print(miLista[:2])

#Esta es otra forma de imprimir una procion de la lista, desde el elemento 0 que lo obvia


print(miLista[:1])
# Accede a los ultimos dos indices


#   PARA AGREGAR LOS ELEMENTOS A LA ISTA SE USA LA FUNCIO APPEND SE AGREGA AL FINAL DE LA LISTA 

miLista.append("Emma")

print(miLista)


# Para agregar a la mitad de la lista el elemento se usa la funcion insert, esta funicon recibe dos parametros 
# el primero es para saber de que indice va a partir y el segundo parametro es el valor a insertar 

miLista.insert(2,"Esteban")

print(miLista)

# Agrega mas elementos pero en bruto

miLista.extend(["Carlos", "Algo", "Algo mas"])


print(miLista)

# Buscar por valor 

print (miLista.index("Juan"))

# Encontrar un elemento dentro de la lista, devulve true o false depende si se encuntra en la lista
print( "Pepe"  in miLista)

print (miLista[1])


# Eliminacion de los elemento
miLista.remove("Ivan")

print(miLista)

# Eliminar el ultimo elemento de la lista

miLista.pop()
print(miLista)

# Unir las dos listas

miLista2 = ["Oliver", "Queen", "Arsenal"]


miLista3 = miLista+miLista2
# Une las dos listas en esta caso

print(miLista3)


# Repetir la lista n numero de veces

print(miLista *3) 