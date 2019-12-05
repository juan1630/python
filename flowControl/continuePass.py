
# La instrucciòn continue sirve para saltar a la siguiente iteracion de bucle, ignorando la iteraciòn 

# pass, devuelve null en el interior del bucle 

# else funciona como en la condicional if


for letra in "python":
    if letra == "h":
        continue

    print("Viendo la letra: " + letra)

# con la instruccion continue se salta la iteracion de h y no imprime dicha letra 

# nombre = "pildoras informaticas"
# contador = 0

# for i in nombre:
#     contador +=1
#     if i == "":
#         continue
    

# print (len(nombre))


# while True:
#     pass

# pass nos ayuda a salir dl bucle infinito

arroba = False
email = input("Intoroduce tu email pro favor: ")

for i in email:
    if i == "@":
        arroba = True
    break


else:
    arroba = False

print( arroba )


