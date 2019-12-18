class Coche():

# Definimos el nombre de la clase

    # Constructor
    def __init__(self):
        # el constructor le proporsiona un estado inicial de la clase
        # el constructor es un metodo especial que les da un valor inicial a las propieades de la clase
        #propiedades del coche = variables
        self.__largo=250
        self.__ancho=300
        self.__ruedas=4
        self.__marcha=False
        self.__color="Negro"
        # encapsulamos las propiedades, poniendo los dos guiones bajos
        #creamos el constructor de la clase
        #solo se accede desde adentro de la clase  __
        #desde una clase hija _
        # los guiones bajos se ponen en todo el programa

#metodos = funciones
#self es como el this
#se encapsula la variable con __ de esta forma no se puede modifcar desde fuera de la clase

    # declarmos el metodo arrancar 
    def arrancar(self,arrancamos):
    # recibe un parametro 
        self.__marcha=arrancamos
        # le asignamos el valor que pasa por parametro el booleano

        if(self.__marcha):
            chequeo=self.__chequeoInterno()
        if(self.__marcha and chequeo):
            self.__marcha=True
            return "El coche esta en marcha"
        elif(self.__marcha and chequeo==False):
            return "El coche esta detenido"




    def estado(self):
        return ("El coche tiene", self.__ruedas, "ruedas. Un ancho de ", self.__ancho, "y un largo de ", self.__largo)

    # Encapuslamiento del metodo
    def __chequeoInterno(self):

        print("Realizando un chequeo interno del coche")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="carradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="carradas"):
            return True
        else:
            return False


micoche = Coche()
micoche.__ruedas=3
print("El coche tiene ", micoche.__ruedas, " ruedas")
print(micoche.arrancar(True))
print(micoche.estado())
print("Creamos el segundo objeto de nuestro programa")
micoche2=Coche()
micoche2.arrancar(False)
