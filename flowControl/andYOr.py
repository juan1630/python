# el operador and es un "Y" o "Ademas" el or como "O"
print("Solicitud de beca")

distancia = int( input("Ingresa la distancia en km: ") )
numeroHermanos = int(input("Ingresa el número de hermanos en el centro: "))
salario = int( input("Ingresa el salario anual bruto: "))

# if distancia > 40 and numeroHermanos > 2 and salario <= 20000:
#     print("Tienes derecho a una beca")
# else:
#     print("No tienes derecho a beca")


if distancia > 40 and numeroHermanos > 2 or salario <= 20000:
    print("Tienes derecho a una beca")
else:
    print("No tienes derecho a beca")



