def evaluaEdad (edad):
    if(edad<0):
        raise TypeError("Agrega una edad valida")
    if edad<20:
        return "Eres muy joven"
    elif(edad<30):
        return "Eres joven"
    elif(edad<40):
        return "Aun eres algo joven"
    elif(edad<80):
        return "Cuidate..."

print(evaluaEdad(-7))
print("Otra linea")
