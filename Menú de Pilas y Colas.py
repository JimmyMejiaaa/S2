import os
class menu:

    print ("""*******************
Observe el menu
*******************
Menu:
1) Pila
2) Cola
3) Lista
4) Salir""")

    opc = int(input("Selecione Opcion: "))
    if (opc==1):

        print("""
***********
Menu Pila:
***********
1)Push
2)Pop
3)Show
4)Longitud
5)Empty
6)Salir""")
        opc1 = int(input("Selecione Opcion: "))
        pila = [2,4,6]

        if (opc1 == 1):
            print("PUSH")
            pila.append(7)
            print(pila)
            input("presione una tecla para continuar...")

        elif (opc1 == 2):
            print("POP")

            if pila.pop():
                print("los elementos que quedan son :{}".format(pila))
            else:
                print(" La lista esta vacia")
                input("presione una tecla para continuar...")
        elif (opc1 == 3):
            print("SHOW")
            n=pila.pop()
            print(n)
            n = pila.pop()
            print(n)
            n = pila.pop()
            print(n)
            input("presione una tecla para continuar...")
        elif (opc1 == 4):
            print("LONGITUD")
            cont = len(pila)
            print(cont)

            input("presione una tecla para continuar...")

        elif (opc1 == 5):

            print("EMPTY")
            empty=pila
            if empty == True:
                print("La pila se encuentra vacía")
            else:
                print("La pila se encuentra con elementos")
                input("presione una tecla para continuar...")


    elif (opc == 2):
        print("""
***********        
Menu Cola:
***********
1)Push
2)Pop
3)Show
4)Longitud
5)Empty
6)Salir""")
        opc2 = int(input("Selecione Opcion: "))
        cola=[3,6,9]
        if (opc2 == 1):
            print("PUSH")
            cola.append(8)
            print(cola)
            input("presione una tecla para continuar...")

        elif (opc2 == 2):

            print("//POP//")

            if cola.pop(0):
                print("los elementos que quedan son :{}".format(cola))
            else:
                print(" La lista esta vacia")
            input("presione una tecla para continuar...")

        elif (opc2 == 3):
            print("SHOW")
            n=cola.pop(0)
            print(n)
            n = cola.pop(0)
            print(n)
            n = cola.pop(0)
            print(n)
            input("presione una tecla para continuar...")

        elif opc2 == 4:
            print("LONGITUD")
            C = len(cola)
            print(C)

            input("presione una tecla para continuar...")

        elif (opc2 == 5):

            print("EMPTY")
            empty=cola
            if empty == True:
                print("La cola se encuentra vacía")
            else:
                print("La cola se encuentra con elementos")
                input("presione una tecla para continuar...")

    elif (opc == 3):
        print("""
***********   
Menu Lista:
***********
1)Append
2)BUSCAR dato y su POSICIÓN 
3)Insertar
4)Eliminar y Obtener eliminado
5)Mostrar
6)Salir""")
        opc3 = int(input("Selecione Opcion: "))
        R= int(input("¿Cuantos valores desea agregar a la lista?"))
        NLim =[]
        for i in range(R):
            Valors = int(input("Ingrese valor{}:".format(i+1)))
            NLim.append(Valors)
            print(NLim)

        if (opc3 == 1):
            print("OPERACIONES CON APPEND")
            N = (input("Ingrese valor APPEND"))
            NLim.append(N)
            print(NLim)
            input("presione una tecla para salir...")

        if (opc3 == 2):
            print("BUSCAR DATO OBTENIENDO SU POSICIÓN ")
            dato = int(input("Ingrese el dato que desee conocer : "))
            for x in range(len(NLim)):
                if dato == NLim[x]:
                    print("El dato {} se encontró en la posición {}".format(dato, x))
                else:
                    print ("El dato {} no se encontró en la posición {}".format (dato, x))
            input("presione una tecla para continuar...")

        if (opc3 == 3):
            print ("INSERTAR")
            print ("INSERTAR")
            N = (input("Ingrese el valor"))
            NLim.append(N)
            print(NLim)
            input("presione una tecla para salir...")

        if (opc3 == 4):
            print ("Eliminar y Obtener eliminado")

        if (opc3 == 5):
            print ("MOSTRAR")