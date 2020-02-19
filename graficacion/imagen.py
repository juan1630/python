from tkinter import *

ventana = Tk()
ventana.geometry("700x700+0+0")
ventana.title("Katia Itzel Alvarado Amaro")

# creamos la imagen

imagenL = PhotoImage( file="./nitro.gif" )
nombre ="Katia Itzel Alvarado Amaro"
formato = "el formato es de tip: gif"
top = ventana


# funciones
def verImage():
    lblImagen = Label(ventana, image=imagenL ).place(x=100, y=90)
    lblFormato = Label(ventana, text=formato).place(x=59, y=50)
    top.mainloop()

def crearVentana():
    top = Toplevel(ventana)
    top.geometry("500x500+0+0")
    lblImagen = Label(top , image=imagenL ).place(x=50, y=50)
    btnVer= Button(top, text="ver", command=verImage).place(x=20, y=80)
    top.mainloop()


# elementos de la interfaz

lblNombre = Label(ventana, text=nombre ).place(x=50, y=390)
# eventos de los elementos
btnAbrir = Button(ventana, text="Ver imagen", command=crearVentana).place(x=50,y=300)

ventana.mainloop()
