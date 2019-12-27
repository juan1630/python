class Persona():
    # super clase persona
    def __init__(self, nombre, edad, lugaR):
        self.nombre = nombre
        self.edad = edad
        self.lugar = lugaR

    def description(self):
        print("Nombre:" , self.nombre , "Edad: " , self.edad , "Lugar: " , self.lugar)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre, edad, lugarResidencia):
        
        self.salario=salario
        self.antiguedad=antiguedad

        super().__init__(nombre, edad, lugarResidencia)
        #Se llama al superconstructor de la clase persona
        super().description()
        #tambien se puede llamar a otras funciones con la funcion super 
    
        print("El salrio es:", self.salario, "La antiguedad: ", self.antiguedad)

    def descripcion(self):
        super().description()
        print("Salario: ", self.salario, "Aniguead: ", self.antiguedad)
        
antonio=Empleado(1600,4, "Antonio", 32, "Polonia")
print (antonio.description())
#devuelve true si el objeto es instancia de la clase
print(isinstance(antonio, Persona))