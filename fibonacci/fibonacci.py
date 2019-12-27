
aux = 1
ultimo = 0
antes_de_ultimo = 0

for contador in range(0,9):
        
    print(contador ," = " , aux)
    antes_de_ultimo = ultimo
    ultimo = aux
    aux = antes_de_ultimo + ultimo


