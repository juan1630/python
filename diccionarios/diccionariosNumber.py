miDiccionario = {"Alemania":"Berlin", 24:"Jordan", "Mosqueteros": 3}
print(miDiccionario[24])


miTupla = ["España", "Francia"]
miDiccionario = {miTupla[0]: "Madrid", miTupla[1]:"Paris"}
print(miDiccionario)
print(miDiccionario["Francia"])

# Almacenar una tupla entera de los valores 
diccionario2 = {"Nombre":"Conor", "Cinturones": ["Peso ligero", "Peso pluma"]}
print(diccionario2["Cinturones"])

# Imprimi todos las llaves del diccionario
print(diccionario2.keys() )

# Imprimie todos los valores del diccionario
print(diccionario2.values())

#Imprimi la longitud del diccionario
print(len( diccionario2 ))