class vehiculos(object):
    """docstring forvehiculos."""
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.marcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.marcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.marcha,
                    "\nAcelerando: ", self.acelera,"\nFrenado: ", self.frena)


class Furgoneta(vehiculos):
    def carga(self, carga):
        self.cargando=carga
        if(self.cargando):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


class Moto(vehiculos):
    #hereda de la clase vehiculos
    hcaballito=""

    def caballito(self):
         self.hcaballito="Estoy haciendo el caballito"

    def estado(self):
        print("Moto")
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.marcha,
             "\nAcelerando: ", self.acelera,"\nFrenado: ", self.frena,"\n", self.hcaballito)
             #sobre escribe el metodo de la clase padre
class VElectricos():

    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True



mimoto=Moto("harley", "CBR")

mimoto.caballito()

mimoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))


class BicicletaElectrica(VElectricos, vehiculos):
    #Herencia multiple
    pass

miBici=BicicletaElectrica()
#para la herencia multiple se toma el constructor de la clase que se hereda primero en este caso vehiculos
