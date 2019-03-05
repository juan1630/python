from io import open

archivoTexto=open("archivo.txt","r+")

#lectura y escritura r+

#frase="Hola a todos Bienvenidos"

#archivoTexto.write(frase)

#archivoTexto.close()
# lo cierra en la memoria

#texto=archivoTexto.read()

#archivoTexto.close()

#print( texto)

#lineas=archivoTexto.readline()

#archivoTexto.close()

#print(lineas)

#archivoTexto.write(" Un gusto ternerlos aqui ")
#archivoTexto.close()


#archivoTexto.seek(len(archivoTexto.read())/2)
archivoTexto.seek((len(archivoTexto.readline())))
#lee una linea en concreto
print(archivoTexto.read(12))
#seek posiciona el puntero
print(archivoTexto.read())
#el metodo readlines nos devuel un arreglo con los saltos de linea
archivoTexto.write("Comienzo de lectura")


