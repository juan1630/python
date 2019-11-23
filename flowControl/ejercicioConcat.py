print("Evaluación de salarios ")

salariPrecidente = int(input("Introduce salario presidente "))
print("Salario presidente: "+ str(salariPrecidente))

# convertimos el tipo number a un string con la funcio str

salarioDirector  = int(input("Introduce salario del director "))
print("Salario director: "+ str(salarioDirector ))

salarioJefe = int(input("Introduce salario jefe del área "))
print("Salario jefe de área: "+ str(salarioJefe))

if salarioJefe < salarioDirector < salariPrecidente:
    print("Todo bien")
else:
    print("Algo anda mal")