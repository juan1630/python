import math
#importamos la libreria math
def cuadrado(num):
    if(num<0):
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num)

r1=(float(input("Ingresa un numero: ")))

try:
    print(cuadrado(r1))
except ValueError as ErrorDeNumnero:
    #hacemos el ValueError como ErrorDeNumnero
    print(ErrorDeNumnero)

print("El programa termino")
