import math

def calcular(semi, itera):
    
    x=[]        
    aux=""
    x3=0
    contador=0

    if contador < itera:
             res=math.pow(semi,2)
             result=str(res)
             resultado=list(result)
             print(resultado)
             x1=resultado[3]
             x2=resultado[4]
             x3=resultado[5]
             x4=resultado[6]

             x.append(x1)
             x.append(x2)
             x.append(x3)
             x.append(x4)
               
             aux=aux.join(x)
             x1=int(aux)
             print(x1)
             x3=calcular(x1, itera)
             print("x3: "+str(x3))
             contador=contador+1





  # """ for j in range(iter):
  #      x3=calcular(x1,iter) 
  #     x4=x3/1000
  #      print(x4)
  #     return x3 """

    


semilla = input("Ingresa una semilla: ")
iteraciones=int(input("Ingresa el número de iteraciones: "))


semilla=int(semilla)
x2=calcular(semilla,iteraciones)
print(x2)
