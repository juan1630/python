lista = [4,2,6,8,5,7]
#declaramos una lista
lista.append(24)
print(lista)

for i in range(len(lista)):
#la iteramos pero por pasada
    for x in range(len(lista)-1):
    #recorre indice por indice
    #la funcio range deja undato fuera
        if lista[x] > lista[x+1]:
            aux=lista[x]
            lista[x] = lista[x+1]
            lista[+1]=aux
            print(lista)
