import math
#importamos la libreria math

# las excepciones son un error en tiempo de ejecucion que no se tenia previsto, un error no contemplado
# uno de estos errores puede para toda la ejecucio  n del programa 

#  una captura o control de excepciones nos ayuda a intentar realizar una tarea, con el catch se puede enviar un mensaje de 
# de error sin tener que detener todo el programa, controlamos mejor los errores 

def cuadrado(num):
    if(num<0):
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num)

r1=(float(input("Ingresa un numero: ")))

try:
    print(cuadrado(r1))
except ValueError as ErrorDeNumnero:
    # creamos un alias a la excepcion 
    print(ErrorDeNumnero)

print("El programa termino")
print("Fin del programa")
