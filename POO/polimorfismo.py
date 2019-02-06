class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seies ruedas")

def desplazamientoV(vehiculo):
    #aca se ve el polimorfismo
    vehiculo.desplazamiento()

miVehiculo=Coche()
#toma la forma dependiendo del objeto que se instancia
desplazamientoV(miVehiculo)
