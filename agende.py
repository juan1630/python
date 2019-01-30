contactos = ["Tonio","Luis"]
accion = raw_input("Agrega una accion")
numero = [123456789,213456789]

if(accion=="agregar"):
    contacto = raw_input("Agrega un nuevo contacto")
    contactos.append(contacto)
    num = raw_input("Numero de tu contacto")
    numero.append(num)
    print("Contacto Agregado !!")
    print(contactos)
    print(numero)

elif(accion=="borrar"):
    contacto = raw_input("Nombre del contacto que vas a borrar")
    contactos.remove(contacto)
    print("Contacto eliminado !!!")
    print(contacto)
