class Coche():

    def __init__(self):

        #propiedades del coche = variables
        self.__largo=250
        self.__ancho=300
        self.__ruedas=4
        self.__marcha=False
        self.__color="Negro"
        #creamos el constructor de la clase
        #solo se accede desde andetro de la clase  __
        #desde una clase hija _

#metodos = funciones
#self es como el this
#se encapsula la variable con __ de esta forma no se puede modifcar desde fuera de la clase

    def arrancar(self,arrancamos):
        self.__marcha=arrancamos

        if(self.__marcha):
            chequeo=self.__chequeoInterno()
        if(self.__marcha and chequeo):
            self.__marcha=True
            return "El coche esta en marcha"
        elif(self.__marcha and chequeo==False):
            return "El coche esta detenido"




    def estado(self):
        return ("El coche tiene", self.__ruedas, "ruedas. Un ancho de ", self.__ancho, "y un largo de ", self.__largo)


    def __chequeoInterno(self):

        print("Realizando un chequeo interno del coche")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="carradas"

        if(self.gasolina=="ok" and self.gasolina=="ok" and self.puertas=="carradas"):
            return True
        else:
            return False


micoche = Coche()
micoche.__ruedas=5
print("El coche tiene ", micoche.__ruedas, " ruedas")
print(micoche.arrancar(True))
print(micoche.estado())
print("Creamos el segundo objeto de nuestro programa")
micoche2=Coche()
micoche2.arrancar(False)