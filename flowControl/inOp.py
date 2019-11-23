# operador in
# evalua varias condiciones a la vez

print("Asignaturas del año 2019")

print("Informatica grafia - Pruebas de software - Usabilidad y accesibilidad")

asignatura = input("Escribe la asignatura elegida")

if asignatura in ("Informatica grafica", "Pruebas de software" , "Usabilidad y accesibilidad"):
    print("Asignatura elegida")
else:
    print("Asignatura no valida")