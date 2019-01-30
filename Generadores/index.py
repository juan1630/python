

def generPares(limite):
    num=1

    while num<limite:
        yield num*2
        num=num+1

pares=generPares(10)


print(next(pares))

print(next(pares))

print(next(pares))
