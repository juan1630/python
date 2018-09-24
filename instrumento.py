class instrumento:
    def __init__(self, precio):
        self.precio=precio
        print "El precios es: ",self.precio
    def tocar(self):
        print "Estamos tocando"
    def romper(self):
        print "Se rompio"
        print "Son: "+str(self.precio)+" $$"

class bateria(instrumento):
    def __init__(self, cuerdas, precio):
        self.precio=precio
        self.cuerdas= cuerdas
        instrumento.__init__(self, precio)
        print "Las cuerdas son: ", self.cuerdas

class guitarra(instrumento):
    pass

violin= bateria(4,2000)
violin.tocar()