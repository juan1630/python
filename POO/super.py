class Persona():
    def __init__(self, nombre, edad, lugarResidencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar = lugarResidencia

    def desc(self):
        print("Nombre: ", self.nombre, "Edad: ", self.edad, " Donde vive: ", self.lugarResidencia)


class Empleado(Persona):
    def __init__(self, salario, actiguedad):
        super().__init__()

        self.salarios = salario
        self.antiguedades = actiguedad
        print("El salario es: ", self.salarios, "la antiguedad: ", self.antiguedades)


Antonio = Empleado("1500", "54")
Antonio.desc()