def divide():
    # Se pueden capturar varias excepciones de una forma mas concecutiva 
    try:

        op1 = float(raw_input("Introduce el primer valor numerico: "))
        op2 = float(raw_input("Introduce el segundo valor numerico: "))

        print("La division es: "+ str(op1/op2))
    

    # except:
    #     print("Captura de excepcion general")

    except ValueError:
        print("El valor introducido es erroneo ")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

    finally:

        print("Calculo finalizado")
    # El finally ejecuta siempre  esa parte del codigo 

# Excepciones de forma concecutiva

divide()