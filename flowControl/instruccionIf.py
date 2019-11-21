print("Programa de evaluación de los alumnos")
notaAlumno = int (input("Ingresa la nota: "))
# La funcion input admite parametros 
#Casteamos el resultado de está forma

def evalucaion(nota):
    #El ambito de las variables, en este caso solo dentro de la funcio, fuera de la funcion no se puede acceder
    aprobado = "Estás aprobado"
    
    if nota < 5:
        aprobado = "Suspenso"
    return aprobado


print( evalucaion(notaAlumno) )