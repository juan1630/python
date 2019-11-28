# No sabemos cuantas veces se va a repetir la linea de codigo
# En python existen los bucles determinados y los indeterminados 
# Los determinados sabemos el número de veces que se van a repetir 
# con los ideterminados no sabemos el número de veces que se van a repetir

# el bucle for cuenta con la declaracion del bucle 
# el codigo a repetir 

# Sintaxis de un bucle for
# for varibale in elemento_a_recorrer:
#   Cuerpo del bucle
#   identar el cuerpo del bucle 
# los elementos a recorrer pueden ser una lista, una tupla, un texto, un rango
# declaracion del bucle 

# for a in ["primaver", "otoño", "verano", "invierno"]:
#     print("Estaciones del año", a)

# for i in [1,2,3,4]:
#     print("Hola", i)
#     # asigna en cada iteracion del bucle el valor a la variable i
#     #cuerpo del bucle 

# for j in ["Hola", "mundo", "jejeje", "jejej"]:
#     print("Hola de nuevo", j)

# el tipo range nos ayuda a usar el bucle for con los conteos numericos

# for i in ["Pildoras", "informaticas", "otro"]:
#     print("Hola", end=" ")

# email = input("Ingresa un correo electronico: ")

# contador  = 0

# for i in email:
#     if(i == "@" or i == "." ):
#         contador= contador +1
# if contador == 2:
#     print("Correo valido")
# else:
#     print("Correo no es valido")


for i in range(5):
    print("Hola")
# crea un array de cinco elementos 
# lo que hace que se imprima la palabra hola 5 veces

