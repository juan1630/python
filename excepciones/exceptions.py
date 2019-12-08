operacion = ""
def sumar (a,b):
    return a+b

def restar (a,b):
    return a-b
    
def multiplicacion(a,b):
    return a*b

def divide (a,b):
        
    try:
        return a/b

    except ZeroDivisionError:
        print("No se puede dividir entre 0 ")
        return "Operacion erronea"

#se captura la excepcion hecha, en  este caso se trata de la division de cero entre un numero
# se imprime el mensaje 
# Se tiene que hacer una excepcion por cada uno de los futuros errores que llegaran a producirse en la ejecucion del programa

while True:
    try:
        op1 = (int(raw_input('Ingresa el primer numero: ')))
        op2 = (int(raw_input('Ingresa el segundo numero: ')))
        break
    except ValueError:
        print("Los valores introducidos no son correctos. Intentalo de nuevo ")

operacion = raw_input('Ingresa la operacion a realizar: ')
# usar la funcion raw_input porque genereba un error al usar solo la funcion input

if operacion == 'suma':
    print(sumar(op1, op2))
elif operacion=='resta':
    print(restar(op1, op2))
elif operacion=='multiplicacion':
    print(multiplicacion(op1, op2))
elif operacion=='division':
    print(divide(op1, op2))
else:
    print('Operaciones division, suma, resta, multiplicacion ')

print("Fin de las operaciones ")
