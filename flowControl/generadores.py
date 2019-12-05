
# Son estructuras que extraen los valores de una funcion y se almacenan en objetos iterables 
# Se almacenan de uno en uno
# Se crera una funcion normal y la instruccione yield, que contruye un objecto iterable

# -----------------------Ventajas 
# Son màs eficientes que las funciones, se puede acceder aun elemento de la lista de forma màs facìl


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


def pares (limite):
    num = 1
    while num < limite:
        yield num*2
        num+=1



devuelvePares = pares(10)

# print(devuelvePares)


for i in devuelvePares:
    print(i)