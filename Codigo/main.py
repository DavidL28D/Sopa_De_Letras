import os, random, string
from colorama import init, Fore, Back, Style, Cursor

def getch():

    import sys, tty, termios

    old_settings = termios.tcgetattr(0)
    new_settings = old_settings[:]
    new_settings[3] &= ~termios.ICANON

    try:
        termios.tcsetattr(0, termios.TCSANOW, new_settings)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(0, termios.TCSANOW, old_settings)
    return ch

def limpiar():
    os.system('clear')

def verSopa(sopa, x, y, controlador):

    ("""
    print()
    for fil in range(20):
        print("    ", end="")
        for col in range(20):

            if y == fil and x == col:
                print(Fore.BLUE+sopa[fil][col]+Fore.RESET, end=" ")
            else:
                print(sopa[fil][col], end=" ")

        print()
    """)

    for fil in range(20):
        for col in range(20):
            print(Cursor.POS(2*(fil+3), col+4)+sopa[fil][col])

    ("""
    fil = controlador[0][3]
    col = controlador[0][4]
    print(Cursor.POS(2*(fil+3), col+4)+Fore.BLUE+sopa[fil][col]+Fore.RESET)
    """)

    for i in range(5):

        if controlador[i][2] == 1:

            lon = len(controlador[i][0])

            fil = controlador[i][3]
            col = controlador[i][4]

            if controlador[i][1] == 0: # N

                for j in range(lon):

                    print(Cursor.POS(2*(fil+3), col-j+4)+Fore.BLUE+sopa[fil][col-j]+Fore.RESET)

            elif controlador[i][1] == 1: # NE

                for j in range(lon):

                    print(Cursor.POS(2*(fil+j+3), col-j+4)+Fore.BLUE+sopa[fil+j][col-j]+Fore.RESET)

            elif controlador[i][1] == 2: # E

                for j in range(lon):

                    print(Cursor.POS(2*(fil+j+3), col+4)+Fore.BLUE+sopa[fil+j][col]+Fore.RESET)
                
            elif controlador[i][1] == 3: # SE

                for j in range(lon):

                    print(Cursor.POS(2*(fil+j+3), col+j+4)+Fore.BLUE+sopa[fil+j][col+j]+Fore.RESET)

            elif controlador[i][1] == 4: # S

                for j in range(lon):

                    print(Cursor.POS(2*(fil+3), col+j+4)+Fore.BLUE+sopa[fil][col+j]+Fore.RESET)

            elif controlador[i][1] == 5: # SO

                for j in range(lon):

                    print(Cursor.POS(2*(fil-j+3), col+j+4)+Fore.BLUE+sopa[fil-j][col+j]+Fore.RESET)

            elif controlador[i][1] == 6: # O
                for j in range(lon):

                    print(Cursor.POS(2*(fil-j+3), col+4)+Fore.BLUE+sopa[fil-j][col]+Fore.RESET)

            elif controlador[i][1] == 7: # NO
                for j in range(lon):

                    print(Cursor.POS(2*(fil-j+3), col-j+4)+Fore.BLUE+sopa[fil-j][col-j]+Fore.RESET)

    
    print(Cursor.POS(2*(x+3), y+4)+Fore.RED+sopa[x][y]+Fore.RESET)
                
def jugar(seleccionadas, sopa, controlador):

    x = y = 0
    xi = yi = xf = yf = 0
    wait = False

    while True:

        limpiar()

        print(Cursor.POS(14, 2)+"*** Sopa de letras ***") 
        verSopa(sopa, x, y, controlador)
        print(Cursor.POS(50, 6)+"Palabras Disponibles:") 

        for i in range(5):
            if(controlador[i][2] == 1):
                print(Cursor.POS(55, 8+i)+Fore.GREEN+controlador[i][0]+Fore.RESET)
            else:
                print(Cursor.POS(55, 8+i)+controlador[i][0])

        print(Cursor.POS(50, 15)+"Instrucciones:")
        print(Cursor.POS(50, 17)+"x = Salir.")
        print(Cursor.POS(50, 18)+"i = Inicio de palabra.")
        print(Cursor.POS(50, 19)+"f = Final de palabra.")
        print(Cursor.POS(50, 20)+"Movimiento = Pad direccional."+Cursor.POS(0, 0))

        tecla = str.lower(getch())

        if tecla == "x":
            break

        elif tecla == "i" and not wait:
            xi = x
            yi = y
            wait = True
        
        elif tecla == "f" and wait:
            xf = x
            yf = y
            wait = False

        elif tecla == "w":
            if y - 1 >= 0:
                y -= 1

        elif tecla == "a":
            if x -1 >= 0:
                x -= 1

        elif tecla == "s":
            if y + 1 <= 19:
                y += 1

        elif tecla == "d":
            if x + 1 <= 19:
                x+= 1

            

    return sopa, controlador

def constSopa(seleccionadas, sopa, controlador):

    # sopa[filas][columnas]
    # controlador[palabra, sentido, estado, xi, yi, xf, yf]
    
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

                        if sopa[xA][yA] == letra or sopa[xA][yA] == "*":

                            sopaAux[xA][yA] = letra
                            yA -= 1
                            
                        else:
                            
                            flag = True
                            break

                    yA += 1

                else:

                    flag = True
                    
            elif s == 1: # NE

                if y - lon >= 0 and x + lon <= 20:

                    for letra in i:

                        if sopa[xA][yA] == letra or sopa[xA][yA] == "*":

                            sopaAux[xA][yA] = letra
                            yA -= 1
                            xA += 1

                        else:

                            flag = True
                            break
                    
                    yA += 1
                    xA -= 1

                else:

                    flag = True
                    
            elif s == 2: # E
                
                if x + lon <= 20:

                    for letra in i:

                        if sopa[xA][yA] == letra or sopa[xA][yA] == "*":

                            sopaAux[xA][yA] = letra
                            xA += 1

                        else:

                            flag = True
                            break

                    xA -= 1

                else:

                    flag = True

            elif s == 3: # SE

                if y + lon <= 20 and x + lon <= 20:

                    for letra in i:

                        if sopa[xA][yA] == letra or sopa[xA][yA] == "*":

                            sopaAux[xA][yA] = letra
                            yA += 1
                            xA += 1

                        else:

                            flag = True
                            break

                    yA -= 1
                    xA -= 1

                else:

                    flag = True

            elif s == 4: # S

                if y + lon <= 20:

                    for letra in i:

                        if sopa[xA][yA] == letra or sopa[xA][yA] == "*":

                            sopaAux[xA][yA] = letra
                            yA += 1

                        else:

                            flag = True
                            break
                    
                    yA -= 1

                else:

                    flag = True

            elif s == 5: # SO

                if y + lon <= 20 and x - lon >= 0:

                    for letra in i:

                        if sopa[xA][yA] == letra or sopa[xA][yA] == "*":

                            sopaAux[xA][yA] = letra
                            yA += 1
                            xA -= 1

                        else:

                            flag = True
                            break

                    yA -= 1
                    xA += 1

                else:

                    flag = True

            elif s == 6: # O

                if x - lon >= 0:

                    for letra in i:

                        if sopa[xA][yA] == letra or sopa[xA][yA] == "*":

                            sopaAux[xA][yA] = letra
                            xA -= 1

                        else:

                            flag = True
                            break

                    xA += 1

                else:

                    flag = True

            elif s == 7: # NO

                if y - lon >= 0 and x - lon >= 0:

                    for letra in i:

                        if sopa[xA][yA] == letra or sopa[xA][yA] == "*":

                            sopaAux[xA][yA] = letra
                            yA -= 1
                            xA -= 1

                        else:

                            flag = True
                            break
                    
                    yA += 1
                    xA += 1

                else:

                    flag = True
        

            if flag:
                
                sopaAux = [row[:] for row in sopa]

            else:
                
                sopa = [row[:] for row in sopaAux]

        controlador.append([i, s, 1, x, y, xA, yA])
        
    #print(controlador)
    #print("*** Sopa ***\n")
    #verSopa(sopa, 0, 0, controlador)
    #input("\nPresione cualquier tecla para continuar...")

    for fil in range(20):
        for col in range(20):
            if sopa[fil][col] == ".":
                sopa[fil][col] = random.choice(string.ascii_uppercase)

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