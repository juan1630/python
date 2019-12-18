class vehiculos(object):
    # esta es la clase padre o super clase
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


# creamos la clase furgoneta
class Furgoneta(vehiculos):
    # esta es la subclase tiene 6 clases ya que sigue herando de la super clase 
    # y creamos un metodo propio de la clase furgoneta
    def carga(self, carga):
        # tiene 6 metodos 
        self.cargando=carga
        if(self.cargando):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


class Moto(vehiculos):
    #hereda de la clase vehiculos
    # de esta forma hacemos la herencia de la clase que se pasa como argumentos
    # el objeto de tipo moto tiene 6 metodos ya que hereda  5 de la superclase 
    hcaballito=""

# metodo propio de la clase en este caso de la moto 
    def caballito(self):
         self.hcaballito="Estoy haciendo el caballito"

    def estado(self):
        print("Moto")
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.marcha,
             "\nAcelerando: ", self.acelera,"\nFrenado: ", self.frena,"\n", self.hcaballito)
             # se sobre escribe el metodo de la clase padre
             # cuando se sobre escribe el metodo de la clase moto se manda a llamar a este metodo

class VElectricos():

    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True



mimoto=Moto("harley", "CBR")
# se tiene que pasar los a
mimoto.caballito()
mimoto.estado()

# Si se usa el metodo carga en la clase moto, nos dara u error ya que el metodo carga pertenece a la clase furgoneta y no moto

# objeto de la furgoneta
miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

# aca el ejemplo de la herencia multiple 
class BicicletaElectrica(VElectricos, vehiculos):
    #Herencia multiple 
    # en la herencia multiple le da la preferencia a la primera clase 
    pass

miBici=BicicletaElectrica()
#para la herencia multiple se toma el constructor de la clase que se hereda primero en este caso vehiculos
miBici.arrancar()