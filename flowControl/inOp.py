# operador in
# evalua varias condiciones a la vez

print("Asignaturas del año 2019")

# python es case sensitive 

# funciones lower() y upper de igual forma están en python

print("Informatica grafia - Pruebas de software - Usabilidad y accesibilidad")

opcion = input("Escribe la asignatura elegida: ")

asignatura = opcion.lower()
print( asignatura.upper() )
print(asignatura)
# convertimos lo que se introdju  por teclado a minusculas 

if asignatura in ("informatica grafica", "pruebas de software" , "usabilidad y accesibilidad"):
    print("Asignatura elegida")
else:
    print("Asignatura no valida")