import pickle

lista_nombres = ["Juan", "Pedro", "Maria"]

fichero_binario=open("lista_nombres", "wb")
#wb escirtuta binaria

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del (fichero_binario)
#borra de la memoria

