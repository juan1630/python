
# Son estructuras que extraen los valores de una funcion y se almacenan en objetos iterables 
# Se almacenan de uno en uno
# Se crera una funcion normal y la instruccione yield, que contruye un objecto iterable

# -----------------------Ventajas 
# Son mas eficientes que las funciones, se puede acceder aun elemento de la lista de forma mas facil

# De esta forma se hace el ejemplo con funciones 


# def numeroPareas (limite):
#     num = 1
#     miLista =  [] 

#     while num < limite:
#         miLista.append(num*2)
#         num +=1
#     return miLista


# print (numeroPareas(10))



# De esta con generedores 


# def pares (limite):
#     num = 1
#     while num < limite:
#         yield num*2
#         num+=1



# devuelvePares = pares(10)

# print(devuelvePares)


# print(next(devuelvePares))

# print("hay mas codigo")

# for i in devuelvePares:
#     print(i)


# print(next(devuelvePares))

# print("Mas codigo")

# print("Estado de suspencion, para ser mas eficiente ")
# print(next(devuelvePares))


## Yield from

# Nos ayuda con los bucles anidados en los que se puede acceder a un array bidmensional

# Generador


def devuelveCiudades (*ciudades):
    for elemento in ciudades:
        #for letra in elemento:
        #    yield letra
        # yield from elemento


# Cuando se pone el asterisco delante del arugmento nos dice que va a recibir un numero indeterminado de elementos 
# y los  recibe en forma de tupla


ciudadesDevueltas = devuelveCiudades("Madrid", "CDMX", "Cuernavaca","Merida")
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))

# devuelve los primeros dos elementos

# la instruccion yield nos dio un problema, queda pendiente 
