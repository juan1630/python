edad = int(input("Ingresa tu edad: "))
if edad < 18:
    print("No puedes pasar")
elif edad > 100:
    print("Edad muy grande")
elif edad < 0:
    print("Edad incorrecta")
else:
    print("Si puedes pasar")

print("Fin del programa")