class Coche:
    def __init__(self, gasolina):
        self.gasolina= gasolina
        print"La gasolina es ",self.gasolina
    def arrancar(self):
        if (self.gasolina < 0):
            print("Hace falta gasolina")
        else:
            print("Arranco")
    def manejar(self):
        if(self.gasolina > 0):
            print("La gasolina es de  ",self.gasolina)
        else:
            print("Sigue sin gasolina")
            self.arrancar



carro = Coche(6)    
carro.manejar()