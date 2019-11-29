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

# el primer argumento de range es el inicio del rango 
# el segundo es fin del rango 
# el tercero es el incremento de cuanto en cuanto

for i in range(5, 50, 3):
   print(f"Valor de la variable: {i}")

# la F signific que es una funcion de tipo F, que nos permite jugar con los formatos de valor diferente
# crea un array de cinco elementos 
# lo que hace que se imprima la palabra hola 5 veces

#El tippo range nos da una lista aritmetica del que se le haya especificado


# la funcion len nos devuelve la longitud de un string 
valido =False
email = input("Introduce tu email: ")

for j in range(len(email)):
    if email[j] == "@":
        valido=True
    
if valido:
    print("Email valido")
else:
    print("Email no es valido")