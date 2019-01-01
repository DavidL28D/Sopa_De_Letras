import os
import random

def limpiar():
    os.system('clear')

def verSopa(sopa):

    for fil in range(20):
        for col in range(20):
            print(sopa[fil][col], end=" ")
        print()

def jugar(seleccionadas, sopa, controlador):

    print("\n*** Sopa ***\n")
    verSopa(sopa)
    input()

def constSopa(seleccionadas, sopa, controlador):

    # sopa[filas][columnas]
    # controlador[palabra, estado, xi, yi, xf, yf]
    
    for fil in range(20):
        sopa.append([])
        for col in range(20):
            sopa[fil].append("*")

    # print(seleccionadas)

    for i in seleccionadas:

        sopaAux = [row[:] for row in sopa]

        # Donde
        # 0 N
        # 1 NE
        # 2 E
        # 3 SE
        # 4 S
        # 5 SO
        # 6 O
        # 7 NO

        s = random.randrange(8)
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

                        #print("revisando si "+letra+" es igual a "+sopa[yA][x])

                        if sopa[yA][xA] == letra or sopa[yA][xA] == "*":

                            sopaAux[yA][xA] = letra
                            yA -= 1
                            
                        else:
                            
                            flag = True
                            #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por choque " + str(flag))
                            break

                    yA += 1

                else:

                    flag = True
                    #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por espacio " + str(flag))
                    
            elif s == 1: # NE

                if y - lon >= 0 and x + lon <= 20:

                    for letra in i:

                        #print("revisando si "+letra+" es igual a "+sopa[yA][xA])

                        if sopa[yA][xA] == letra or sopa[yA][xA] == "*":

                            sopaAux[yA][xA] = letra
                            yA -= 1
                            xA += 1

                        else:

                            #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por choque " + str(flag))
                            flag = True
                            break
                    
                    yA += 1
                    xA -= 1

                else:

                    #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por espacio " + str(flag))
                    flag = True
                    
            elif s == 2: # E
                
                if x + lon <= 20:

                    for letra in i:

                        #print("revisando si "+letra+" es igual a "+sopa[yA][xA])

                        if sopa[yA][xA] == letra or sopa[yA][xA] == "*":

                            sopaAux[yA][xA] = letra
                            xA += 1

                        else:

                            #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por choque " + str(flag))
                            flag = True
                            break

                    xA -= 1

                else:

                    #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por espacio " + str(flag))
                    flag = True

            elif s == 3: # SE

                if y + lon <= 20 and x + lon <= 20:

                    for letra in i:

                        #print("revisando si "+letra+" es igual a "+sopa[yA][xA])

                        if sopa[yA][xA] == letra or sopa[yA][xA] == "*":

                            sopaAux[yA][xA] = letra
                            yA += 1
                            xA += 1

                        else:

                            #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por choque " + str(flag))
                            flag = True
                            break

                    yA -= 1
                    xA -= 1

                else:

                    #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por espacio " + str(flag))
                    flag = True

            elif s == 4: # S

                if y + lon <= 20:

                    for letra in i:

                        #print("revisando si "+letra+" es igual a "+sopa[yA][xA])

                        if sopa[yA][xA] == letra or sopa[yA][xA] == "*":

                            sopaAux[yA][xA] = letra
                            yA += 1

                        else:

                            #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por choque " + str(flag))
                            flag = True
                            break
                    
                    yA -= 1

                else:

                    #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por espacio " + str(flag))
                    flag = True

            elif s == 5: # SO

                if y + lon <= 20 and x - lon >= 0:

                    for letra in i:

                        #print("revisando si "+letra+" es igual a "+sopa[yA][xA])

                        if sopa[yA][xA] == letra or sopa[yA][xA] == "*":

                            sopaAux[yA][xA] = letra
                            yA += 1
                            xA -= 1

                        else:

                            #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por choque " + str(flag))
                            flag = True
                            break

                    yA -= 1
                    xA += 1

                else:

                    #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por espacio " + str(flag))
                    flag = True

            elif s == 6: # O

                if x - lon >= 0:

                    for letra in i:

                        #print("revisando si "+letra+" es igual a "+sopa[yA][xA])

                        if sopa[yA][xA] == letra or sopa[yA][xA] == "*":

                            sopaAux[yA][xA] = letra
                            xA -= 1

                        else:

                            #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por choque " + str(flag))
                            flag = True
                            break

                    xA += 1

                else:

                    #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por espacio " + str(flag))
                    flag = True

            elif s == 7: # NO

                if y - lon >= 0 and x - lon >= 0:

                    for letra in i:

                        #print("revisando si "+letra+" es igual a "+sopa[yA][xA])

                        if sopa[yA][xA] == letra or sopa[yA][xA] == "*":

                            sopaAux[yA][xA] = letra
                            yA -= 1
                            xA -= 1

                        else:

                            #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por choque " + str(flag))
                            flag = True
                            break
                    
                    yA += 1
                    xA += 1

                else:

                    #print("no se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") por espacio " + str(flag))
                    flag = True
        

            if flag:
                
                sopaAux = [row[:] for row in sopa]

            else:
                
                #print("se puede sampar la palabra " + i + " - "+ str(lon) + " - en las coordenadas (" + str(x) + ", " + str(y) + ") " + str(flag))
                sopa = [row[:] for row in sopaAux]

        controlador.append([i, 0, x, y, xA, yA])
        
    #print(controlador)
    #print("*** Sopa ***\n")
    #verSopa(sopa)
    #input("\nPresione cualquier tecla para continuar...")
    return sopa
    
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

    input("""Elaborado por:\n\nDavid L. Chacón G.\n25.023.230\nComputacion I Seccion X\n\nPresione cualquier tecla para continuar...""")

def menu():

    game = False
    palabras = ("ABACO", "BEBE", "CABALGAR", "DUENDE", "EXITO", "FUENTE", "GUANTES", "HUESO", "IDEAS", "JARRON", "KILO", "MONO", "NAUTILUS", "OBELISCO", "PETROLEO", "QUEBRAR", "RABANO", "SAPO", "TIA", "UVAS")

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
                sopa = constSopa(seleccionadas, sopa, controlador)

                game = True
                jugar(seleccionadas, sopa, controlador)

            elif x == 3:

                if game:

                    jugar(seleccionadas, sopa, controlador)

                else:

                    input("No existe un juego nuevo, por favor selecciona antes la opcion 2...")

            elif x == 4:

                creditos()


        else:
            print("Opcion incorrecta, vuelve a intentarlo.")


menu()