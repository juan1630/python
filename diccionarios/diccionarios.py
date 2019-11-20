# DICCIONARIOS 
# Son estructuras de datos, estos los hacen de una asigancion del tipo clave - valor 
# como los objetos JSON, o un array asociativo

miDiccionario = {"Alemania":"Berlin", "Francia": "Paris", "Reino unido":"Londres", "España": "Madrid"}

print(miDiccionario["Alemania"])

# Se entra a la clave alemania

miDiccionario["Italia"] = "Lisboa"
print(miDiccionario)

# Sobre escribe los valores 
miDiccionario["Italia"]="Roma"
print(miDiccionario)

#Eliminar un valor 
del miDiccionario["Italia"]

print(miDiccionario)
