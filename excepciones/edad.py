
def evaluaEdad (edad):
    if(edad<0):
        # raise es una funcion que personaliza le mensaje que se le da al usuario
        # despues de raise va el tio de excepcion en el que se clasifica 
        raise TypeError("Agrega una edad valida")
    if edad<20:
        return "Eres muy joven"
    elif(edad<30):
        return "Eres joven"
    elif(edad<40):
        return "Aun eres algo joven"
    elif(edad<80):
        return "Cuidate..."

print(evaluaEdad(-15))
print("Otra linea")
