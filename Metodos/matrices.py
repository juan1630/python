matriz1=input("Ingresa tu primer matriz: ")
matriz2=input("Ingresa tu segunda matriz")

matriz1=list(matriz1)
matriz2=list(matriz2)
i=1
j=1

for i in range(len(matriz1)):
    a=float( matriz1[i] )
    b=float( matriz2[i] )
    res= a+b
    print(res)

for j in range(len(matriz1)):
    a=float( matriz1[j] )
    b=float( matriz2[j] )
    res= a - b
    print("Resta: " +str(res))

matriz_2=input("Ingresa tu matriz de 2x2: ")
matrizPrincipal=input("Ingresa tu matriz 3x3: ")

matrizPrincipal=list(matrizPrincipal)
matriz_2=list(matriz_2)

for k in range(len(matrizPrincipal)):
    for d in range(len(matriz_2)):
