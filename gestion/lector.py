archivo ="/Users/headc/Desktop/Proyectos/ingles/index.js"

file = open(archivo)
files= file.readlines()
contador=0

for line in files:
    palabras = line.split()
    
    for palabra in palabras:
        if(palabra=='const'):
            contador= contador+1
            print(contador) 


