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


op1 = (int(input("Ingresa el primer numero: ")))
op2 = (int(input("Ingresa el segundo numero: ")))
operacion = str(input("Ingresa la operacion a realizar: "))

print(suma)

if operacion=="suma":
    print(sumar(op1, op2))
elif operacion=="resta":
    print(restar(op1, op2))
elif operacion=="multiplicacion":
    print(multiplicacion(op1, op2))
elif operacion=="division":
    print(divide(op1, op2))
else:
    print("Operaciones division, suma, resta, multiplicacion ")

print("Fin de las operaciones ")
