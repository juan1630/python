class Persona():
    def __init__(self, nombre, edad, lugaR):
        self.nombre = nombre
        self.edad = edad
        self.lugar = lugaR

    def description(self):
        print("Nombre:" , self.nombre , "Edad: " , self.edad , "Lugar: " , self.lugar)

class Empleado(Persona):
    def __init__(self, salario, antiguedad):
        self.salario=salario
        self.antiguedad=antiguedad

        super().__init__("Antonio", 55, "Mexico")
        #Se llama al superconstructor
        super().description()
        #tambien se puede llamar a otras funciones
        print("El salrio es:", self.salario, "La antiguedad: ", self.antiguedad)

antonio=Empleado(1600,4)
antonio.description()
#devuelve true si el objeto es instancia de la clase
print(isinstance(antonio, Persona))