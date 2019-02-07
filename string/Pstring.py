nombre=input("Ingresa tu nombre de usuario :")

print("El nombres :", nombre.upper())
#upper convierte el string a mayusculas

print("El nombres :", nombre.lower())
print("El nombres :", nombre.capitalize())

edad=input("Introduce tu edad: ")

while(edad.isdigit()==False):
    print("Por favor ingresa un número")
    edad = input("Introduce tu edad: ")

if(int(edad)<18):
    print("Eres menor de edad")
else:
    print("Si puedes pasar")


print(edad.isdigit())