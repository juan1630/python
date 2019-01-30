def cuadrado (n):
    return n**2


l = [2,3,4,5,6,7,8,10]
#declaramos una lista 
#declaramos una funcion
l2 = map(cuadrado, l)
#creamos una variable la cual se convertira en una lista dado 
#el retorno de la funcion map
#primero le pasamos por parametro la funcion 
#como segundo parametro la lista la cual sera iterada n veces en este caso 3
#no usar acentos en python
def pares(n):
    return n%2==0
l3=filter(pares,l)
#la funcio filter filtra los elementos :v de una lista cuando una condicion se 
#se cumple 



def suma(n,m):
    return n+m
l4=reduce(suma,l)
#la funcion reduce sirve para retornar un solo elemento
#la funcion lamnda que son como los callbacks de javascript
l5=filter(lambda n: n%2==0,l)
#se obtiene lo mismo que declarando la funcion
print(l2)
print(l3)
print(l4)
print(l5)