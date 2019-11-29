import math

# asi se importan las clases en python

# es un bucle indterminado
# i = 1

# while i <= 10:
#     print("Ejecucion: " + str(i))
#     i=i+1

# print("Termino la ejecución")


# edad = int(input("Introduce tu edad: "))

# while edad < 5 or edad > 100:
#     print("Esa edad es negativa, vuelve a intentarlo")
#     edad = int(input("Introduce tu edad: "))

# print("Edad correcta")
# print("Esta es tu edad "+  str(edad))

print("Programa de calculo de raiz cuadrada ")

raiz = int(input("Introduce un número, por favor "))
intentos = 0

while raiz < 3:
    print("No se puede hallar la raiz de un número neativo")
    if intentos > 2:
        print("Número de intentos maximos")
        break
    raiz = int(input("Introduce un número, por favor "))
    if raiz<0:
        intentos = intentos + 1

if intentos<2:
    solucion = math.sqrt(raiz)
    print("La raiz de "+ str(raiz)+ " es: "+ str(solucion))


