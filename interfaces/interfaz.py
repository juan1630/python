# para python se necesita crear una raiz para que 
#importamos la libreria

from tkinter import *

raiz=Tk()
#construimos la raiz
#llamamos al metodo mainloop
raiz.title("Ventana uno")


#recibe parametros booleanos
raiz.resizable(1,0)
#puede reimencioar a lo ancho y no a lo alto

#este metodo crea un bucle infinito
#para que la ventana se pueda ejecutar
#para que escuche los eventos debe estar en el bucle infinito
#importamos la libreria
raiz.mainloop()
#siempre debe estar al ultimo


