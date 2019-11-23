print("Sistema de evalucaion de los alumnos")

nota_alumno = int( input("Introduce tu nota, por favor: ") )


# Elif es una acortación del else if () {
#  }
# de forma mas simple



if nota_alumno < 5:
    print("Insuficiente")
elif nota_alumno < 6:
    print("Suficienta")
elif nota_alumno < 7:
    print("Bien")
elif nota_alumno < 9:
    print("Notable")
else:
    print("Sobresaliente")
