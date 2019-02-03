#imprime en pantalla la palabra hello world un print como el de java
print("Hello World")

#declaramos variables :
#Tipo cadena
cadena  =  "SISTEMASPROGRAMABLES"
#Entero
c = 3
#Listas

youhavesleep = True
drinkcoffee=True
#asignamos el valor True a las variables

if (youhavesleep ==drinkcoffee):
    print("coffee")

else:
    print(":P")
#un if en este caso los : sirven como parentesis de java

print (cadena)
#imprimimos el valo de la variable cadena
def saludar(nombre):
    return"Hola "+nombre
#creamos nuestra primera funcion

lista = [22, True, "Hola mundo", [1,2]]
#creamos una lista
# una lista se puede partir con [posicion 1 : posiscion 2]

#Tuplas similares a las listas
t = ( 10, "Hola", True, 1 )

#Diccionarios

d = {
    "Batman inicia":"Nolan",
    "Kill bill" :"Tarantino"
}
#un ciclo while
while True:
    entrada = input("Agrega una palabra: ")
    if entrada == "adios":
        break
    else:
        print(str(entrada))

promedio = 5

if promedio >= 7:
    print ("Aprobado")
elif promedio == 0:
    print("Eres muy tonto")
else:
    print("Reprobado")

#elif igaul a un else if
edad = 0

while edad < 20:
    edad=edad+1
    print("Tu edad es de "+ str(edad))

numero=[2,3,4, "cadena"]

for elemento in numero:
    print(elemento)

#ciclo for
def saludo(nombre, anios, hijo=0, *sabes):
    """ Primera funcion en python """
    print("Hola " +nombre+" tienes "+str(anios)+" y tienes "+str(hijo)+" hijos"+ " y sabes"+str(sabes))
#la funcion str convierte de string a decimal
#Se debe de usar al imprimir numeros en una cadena

saludo("Juan", 23, 1, "Riak","Node","React")
print (t[1])
print (type(cadena))
print(lista[0:2])
print(type(c))
print (d['Kill bill'])

print(saludar("juan"))
#ejecutamos la funcion
