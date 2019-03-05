import math

semilla=int(input("Ingresa la semialla: "))
iteraciones=int(input("Ingresa el numero de iteracones: "))

contador=1

while contador < iteraciones:
    semillaCuadrada=math.pow(semilla, 2)
    NsemillaCuadrada=str(semillaCuadrada)
    numeros=NsemillaCuadrada[4:8]
    semilla=int(numeros)
    print("R"+str(contador)+": "+str(semilla))
    resultado=semilla/10000
    print(resultado)
    contador=contador+1
