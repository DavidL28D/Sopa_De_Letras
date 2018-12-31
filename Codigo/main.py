import os
import random

def limpiar():
    os.system('clear')

def verSopa(sopa):

    for fil in range(20):
        for col in range(20):
            print(sopa[fil][col], end=" ")
        print()

def constSopa(seleccionadas, sopa, controlador):

    # sopa[filas][columnas]
    # controlador[palabra, sentido, estado, x, y]
    sopaAux = sopa

    for fil in range(20):
        sopa.append([])
        for col in range(20):
            sopa[fil].append("*")

    print(seleccionadas)

    for i in seleccionadas:

        # Donde
        # 0 N
        # 1 NE
        # 2 E
        # 3 SE
        # 4 S
        # 5 SO
        # 6 O
        # 7 NO

        #s = random.randrange(8)
        s = 0
        lon = len(i)
        
        flag = True
        while flag:

            flag = False
            x = random.randrange(20)
            y = random.randrange(20)

            xA = x
            yA = y           

            if s == 0: # N

                if y - lon >= 0:

                    for letra in i:

                        if sopa[yA][x] == letra or sopa[yA][x] == "*":
                            #print("revisando si "+letra+" es igual a "+sopa[yA][x])
                            sopaAux[yA][x] = letra
                            yA -= 1

                        else:

                            flag = True
                            #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ")")
                            break

                else:

                    flag = True
                    #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ")")

            elif s == 1: # NE
                pass

            elif s == 2: # E
                pass

            elif s == 3: # SE
                pass

            elif s == 4: # S
                pass

            elif s == 5: # SO
                pass

            elif s == 6: # O
                pass

            elif s == 7: # NO
                pass
        
            if flag:

                sopaAux = sopa

            else:

                print("se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ")")
                sopa = sopaAux

        controlador.append([i, 0, s, x, y])

    print(controlador)
    verSopa(sopa)
    input("\nPresione cualquier tecla para continuar...")




def selPalabras(palabras, seleccionadas):

    for i in range(5):

        x = random.randrange(20)

        if i != 0:

            flag = True
            while flag:

                flag = False

                for j in seleccionadas:
                    
                    if j == palabras[x]:

                        x = int(random.randrange(20))
                        flag = True
                        break

        seleccionadas.append(palabras[x])

    #print(seleccionadas)
    #input("\nPresione cualquier tecla para continuar...")


def listado(palabras):

    print("Palabras disponibles: \n")

    for i in palabras:
        print(i)

    input("\nPresione cualquier tecla para continuar...")


def creditos():

    print("""Elaborado por:\n\nDavid L. Chacón G.\n25.023.230\nComputacion I Seccion X\n\nPresione cualquier tecla para continuar...""")
    input()


def menu():

    palabras = ("ABACO", "BEBE", "CABALGAR", "DUENDE", "ESTIVA", "FUENTE", "GUANTES", "HUESO", "IDEAS", "JARRON", "KILO", "MONO", "NAUTILUS", "OBELISCO", "PETROLEO", "QUEBRAR", "RABANO", "SAPO", "TIA", "UVAS")

    seleccionadas = []
    sopa = []
    controlador = []

    while True:

        limpiar()
        print("*** Sopa de letras***\n")
        print("1.- Ver listado de palabras.")
        print("2.- Nueva sopa de letras.")
        print("3.- Continuar con la ultima sopa de letras.")
        print("4.- Creditos.")
        print("0.- Salir.")

        x = int(input("\nIngrese la opcion: "))

        if x >= 0 and x<=4:

            limpiar()

            if x == 0:
                break
                
            elif x == 1:

                listado(palabras)

            elif x == 2:
                
                seleccionadas = []
                controlador = []
                sopa = []

                selPalabras(palabras, seleccionadas)
                constSopa(seleccionadas, sopa, controlador)

            elif x == 3:
                print("opcion 3")

            elif x == 4:

                creditos()


        else:
            print("Opcion incorrecta, vuelve a intentarlo.")


menu()