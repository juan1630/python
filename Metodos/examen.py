import math

numero=input("Ingresa a: ")
numero1=input("Ingresa b: ")
resul=int(numero)
resultado=int(numero1)


def res(a,x1,b,fb):
    xr=( (x1)(b-a)/((fb)-(x1))) -a
    return xr


def suma(num):
    res=(math.pow(num, 2)-2)
    return res


xa=suma(resul)
xb=suma(resultado)

xb=int(xb)
xa=int(xa)

print(res(resul,xa,resultado,xb))

