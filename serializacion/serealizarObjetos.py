import pickle

class Vehiculo():
    def __init__(self,marca, modelo):
        self.marca=marca
        self.model=modelo
    def arrancar(self):
        print("El auto es: "+ str(self.marca))

    def apagar(self):
        print('El auto esta apagado'  +self.model)



coche1 = Vehiculo('bmw', '2018')
coche2 = Vehiculo('seat', '2018')
coche3 = Vehiculo('renault', '2018')

coches=[coche1, coche2, coche3]

fichero= open("coche", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

fichero_apertura=open('lista_nombres', 'rb')
micochs=pickle.load(fichero_apertura)
fichero_apertura.clo