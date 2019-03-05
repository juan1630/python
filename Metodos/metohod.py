import math

valores = input("Ingresa tus valores: ")
acu=[]
iteracion=[]
val= list(valores)

def buscar(num):
    res=(math.pow(num,3 )-3)
    return res

def form(xa, xb):
    xr=(xa+xb)/2
    return xr


for i, numero in enumerate(val):
    numer=int(numero)
    resultado=buscar(numer)
    if(resultado < 0 ):
        acu.append(resultado)
        iteracion.append(i)
    elif(resultado < 6):
        acu.append(resultado)
        iteracion.append(i)

x1=int(iteracion[1])
x2=int(iteracion[2])

xr1 = form(x1,x2)
print(xr1)

while xr1 < 1.665:    
    xr1 = form(x1,x2)
    print(xr1)
    x2=xr1

    if(xr1 < 1.5):
        print("xb"+str(x2))
        x1=xr1
        xr1 = form(x1, x2)
    if(xr1==1.442):
        print(xr1)
        break 



