#Autora:Alvarado Amaro Katia Itzel
#Materia:Metodos Numericos
#Profesora:Maria de Lourdes Cruz Aviles
#Grupo:2

#Este programa contiene tres tipos de errores: error absoluto que se obtine con la siguiente formula que es:
#restar el valor verdadero con el valor aproximado para que de esta manera nos de como resultado
#el error absoluto.
#el error relativo quue este so obtiene dividiendo el resultado del error absoluto entre el error
#verdadero y por ultimo el error porcentual el cual solo se multiplica el resultado del error relativo por cien



print("Ingresa tus valores ")
#imprime el mensqaje, en este caso imprimira el mensaje que dice imprimir valores

valorVerdadero = float(input("Ingresa el valor verdadero: "))
#esa es la primer variable y se pone en modo float para que ejecute los numeros decimales
valorAproximado = float(input("Ingresa el valor aproximado: ")
)#segunda variable que al igual que la primera se declara flotante

def errores (valorVerdadero, valorAproximado):


    errorAbsoluto=valorVerdadero-valorAproximado
    errorRelativo=float(valorVerdadero-valorAproximado)/float(valorVerdadero)
    errorPorcentual=errorRelativo*100
    print("el errorAbsoluto es:", errorAbsoluto)
    print("el errorRelativo es:", errorRelativo)
    print("el errorPorcentual es:", errorPorcentual)



print( errores(valorVerdadero, valorAproximado) )
#se hace la resta de las variables declaradas y se imprime el resultado
