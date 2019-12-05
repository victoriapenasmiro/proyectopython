import random
import time

def mostrarInstrucciones():
    instrucciones="******************************************************\
***************\n"+\
    "*** ||        ||           ||||||||||       ||       ||   ||       ||\n"+\
    "** ||||      ||||         ||              || ||     ||    ||       ||\n"+\
    "* ||  ||    ||  ||       |||||||||||     ||   ||   ||     ||       ||\n"+\
    " ||    ||  ||    ||     ||              ||     || ||      ||       ||\n"+\
    "||      ||||      ||   ||||||||||||    ||       ||        |||||||||||\n"+\
    "*********************************************************************\n"+\
    "*********************************************************************\n"+\
    "\n                        NORMAS DEL JUEGO:\n\n" +\
          "Conecta 4 es un juego para dos jugadores.El tablero consta de 6\n"+\
          "filas y 7 columnas. Cada jugador deberá seleccionar el carácter\n"+\
          "con el que van a jugar, que puede ser X u O. Cada jugador tiene\n"+\
          "un solo movimiento permitido en su turno.\n\n" +\
          "El jugador debe escoger en qué columna quiere tirar ficha.Y las\n"+\
          "fichas se irán ubicando desde las filas inferiores de la columna\n"+\
          "seleccionada, amontonándose una encima de otra.\n\n" +\
          "***************************************************************\
*****\n"+\
          "********************************************************************"
    return instrucciones

def seleccionJugador1():
    random.seed(time.time())
    jugadorinicial=random.randint(0,1)
    print("\nEMPIEZA ",end="")    
    if jugadorinicial==0:
        print(p1.get("nombre") + "!\n")
    else:
        print(p2.get("nombre") + "!\n")
    return jugadorinicial

def mostrarMenu():
    global jugadores
    global p1
    global p2
    print(mostrarInstrucciones())
    p1["nombre"]=input("Jugador 1, indica tu nombre: ")
    letraP1 = input("Elige X o O:")
    while not (letraP1=='X' or  letraP1=='O' or letraP1=='x' or letraP1=='o'):
        letraP1=input('Letra incorrecta.Elige X or O?')
    #Conversión a mayúscula + añadir dict en lista
    p1["letra"]=letraP1.upper()
    p1["marcador"]=0
    jugadores.append(p1)
    p2["nombre"]=input("Jugador 2,indica tu nombre: ")
    if p1["letra"] == "X":
        p2["letra"]="O"
    elif p1["letra"] == "O":
        p2["letra"]="X"
    p2["marcador"]=0
    jugadores.append(p2)
    print(p2.get("nombre"),"te ha tocado el carácter:",p2.get("letra"),"\n")

#Creamos el tablero
def crearTablero():
    global lista_tablero
    FILAS=6 #CONTANTE
    COLUMNAS=8 #CONTANTE
    for i in range (FILAS):
        lista_columnas=[]
        for j in range (COLUMNAS):
            if j == 0:
                lista_columnas.append("|")
            elif j == 7:
                lista_columnas.append("_|")
            else:
                lista_columnas.append("_|")
        lista_tablero.append(lista_columnas)
    mostrarTablero()

#pintamos el tablero
def mostrarTablero():
    global lista_tablero
    NUMEROS=" 1 2 3 4 5 6 7" #CONTANTE
    print (NUMEROS)   
    for i in range(len(lista_tablero)):
        for j in range(len(lista_tablero[i])):
             if j==(len(lista_tablero[i])-1):
                   print(lista_tablero[i][j])
             else:
                   print(lista_tablero[i][j],end="")

#insertar ficha + validar victoria
def insertarFicha(jugador):
    global victoria
    global fin
    #este contador se utiliza para establecer cuando deben empezar
    #a ejecutarse las comprobaciones de victoria
    contador=0
    if jugador==0:
        jugador=p1
    else:
        jugador=p2
    while victoria==False and fin==False:
        columna=0
        #verificamos que el usuario inserta un int y que
        #corresponde con una columna valida
        while columna==0:
            try:
                columna=int(input("\nPor favor " + jugador.get("nombre")+\
                " dime la columna: "))
                while columna>7 or columna<1:
                    columna=int(input("la columna que has indicado no es correcta,"+\
                    "dime otra: "))
            except:
                print("El valor introducido no es correcto.")
                columna=0
        if lista_tablero[0][columna]!="_|":
            columna=int(input("la columna que has indicado está completa,"+\
            "dime otra: "))
        #Insertar ficha en el hueco disponible indicado por el jugador
        for i in range(len(lista_tablero)-1,-1,-1):
            if lista_tablero[i][columna]=="_|":
                lista_tablero[i][columna]=jugador.get("letra") + "|"
                contador+=1
                break
        mostrarTablero()
        #verificamos que almenos haya 7 fichas insertadas para empezar
        #a comprobar una posible victoria
        if contador > 6 and contador < 42:
            comprobarVictoriaVertical(i,jugador,columna)
            comprobarVictoriaHorizontal(i,jugador)
            comprobarVictoriaDiagonal(jugador)
        elif contador==42:
            finPartida()
        if victoria==False and fin==False:
            if jugador==p1:
                jugador=p2
            else:
                jugador=p1

#*******preguntar a rafa si valen la pena los returns*********
def comprobarVictoriaVertical(i,jugador,columna):
    global victoria
    global fin
    if i==0 or i==1 or i==2:
        if lista_tablero[i][columna]==jugador.get("letra") + "|" and\
        lista_tablero[i+1][columna]==jugador.get("letra") + "|" and\
        lista_tablero[i+2][columna]==jugador.get("letra") + "|" and\
        lista_tablero[i+3][columna]==jugador.get("letra") + "|":
            victoria=True
            fin=True
            jugador["marcador"]+=1 #Incremento del marcador del jugador
            print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")
    return victoria

def comprobarVictoriaHorizontal(i,jugador):
    global victoria
    global fin
    contador=0
    #comprobamos que hay almenos hay 4 fichas repetidas en la fila
    if lista_tablero[i].count(jugador.get("letra") + "|")>=4:
        #Empieza desde la posicion 1,porque en la 0 hay un | siempre
        for j in range(1,len(lista_tablero[i])):
            if lista_tablero[i][j]==jugador.get("letra") + "|":
                contador+=1
            if contador==4:
                victoria=True
                fin=True
                jugador["marcador"]+=1 #Incremento del marcador del jugador
                print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")
                break
            if j+1<8:
                if lista_tablero[i][j+1]!=jugador.get("letra") + "|":
                    contador=0
    return victoria

def comprobarVictoriaDiagonal(jugador):
    global victoria
    global fin
    for i in range(len(lista_tablero)-1,-1,-1):
        for j in range(len(lista_tablero[i])):
            if j>4 and lista_tablero[i][j]==jugador.get("letra") + "|":
                if lista_tablero[i-1][j-1]==jugador.get("letra") + "|" and\
                lista_tablero[i-2][j-2]==jugador.get("letra") + "|" and\
                lista_tablero[i-3][j-3]==jugador.get("letra") + "|":
                    victoria=True
                    fin=True
                    jugador["marcador"]+=1 #Incremento del marcador del jugador
                    print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")
                    break
            elif j<4 and j>0 and lista_tablero[i][j]==jugador.get("letra") + "|":
                if lista_tablero[i-1][j+1]==jugador.get("letra") + "|" and\
                lista_tablero[i-2][j+2]==jugador.get("letra") + "|" and\
                lista_tablero[i-3][j+3]==jugador.get("letra") + "|":
                    victoria=True
                    fin=True
                    jugador["marcador"]+=1 #Incremento del marcador del jugador
                    print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")
                    break
            elif j==4 and lista_tablero[i][j]==jugador.get("letra") + "|":
                if lista_tablero[i-1][j+1]==jugador.get("letra") + "|" and\
                lista_tablero[i-2][j+2]==jugador.get("letra") + "|" and\
                lista_tablero[i-3][j+3]==jugador.get("letra") + "|":
                    victoria=True
                    fin=True
                    jugador["marcador"]+=1 #Incremento del marcador del jugador
                    print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")
                    break
                elif lista_tablero[i-1][j-1]==jugador.get("letra") + "|" and\
                lista_tablero[i-2][j-2]==jugador.get("letra") + "|" and\
                lista_tablero[i-3][j-3]==jugador.get("letra") + "|":
                    victoria=True
                    fin=True
                    jugador["marcador"]+=1 #Incremento del marcador del jugador
                    print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")
                    break
    return victoria
#esta función comprueba si el tablero está completo y no hay ganador
def finPartida():
    global fin
    if victoria==False and fin==False:
        if "_|" in lista_tablero[0]:
            fin=False
        else:
            fin=True
            print ("\n¡EMPATE!\n")

def mostrarMenuFin():
    opcion=0
    salir=False
    while salir==False:
        print("\n")
        print("************************************************************")
        print("********* |||||||||||||||   ()         || ||        || *****")
        print("******** ||                 ||        ||   ||      ||  *****")
        print("******* ||||||||||||||      ||       ||     ||    ||   *****")
        print("****** ||                   ||      ||       ||  ||    *****")
        print("***** ||                    ||     ||         ||||     *****")
        print("************************************************************\n")
        print (" 1) REINICIAR JUEGO")
        print (" 2) JUGAR REVANCHA")
        print (" 3) SALIR")
        while opcion==0:
            try:
                opcion=int(input("\n¿Qué opción deseas? "))
            except:
                print("EL VALOR INTRODUCIDO NO ES CORRECT0, VUELVE A INTENTARLO.")
                opcion=0
        if opcion==1:
            salir=True
            volverJugar()
        elif opcion==2:
            salir=True
            jugarRevancha()
        elif opcion==3:
            print("\n¡HASTA PRONTO!")
            salir=True
        else:
            print ("LA OPCION INTRODUCIDA ES INCORRECTA, VUELVE A INTENTARLO: ")

def volverJugar():
    global victoria
    global fin
    global lista_tablero
    global jugadores
    global p1
    global p2
    #VARIABLES --> Reseteo de valores
    lista_tablero=[]
    jugadores=[]
    p1=dict()
    p2=dict()
    victoria=False
    fin=False
    mostrarMenu()

def jugarRevancha():
    print("\n************************************************************")
    print("************************************************************")
    print("**********    ||||||||||||||   ||||||||||||||   ||   *******")
    print("**********    |||              |||        |||   ||   *******")
    print("**********    |||   ||||||||   |||        |||   ||   *******")
    print("**********    |||        |||   |||        |||   ||   *******")
    print("**********    ||||||||||||||   ||||||||||||||   ()   *******")
    print("************************************************************")
    print("************************************************************")
    print("************************************************************\n")
    print("          <<<<<<<<<<<---- MARCADOR ---->>>>>>>>>>>\n")
    print("                      ",p1.get("nombre"),"VS",p2.get("nombre"),"\n")
    print(p1.get("nombre"),":",p1.get("marcador"),"VICTORIAS\n")
    print(p2.get("nombre"),":",p2.get("marcador"),"VICTORIAS\n")
    global victoria
    global fin
    global lista_tablero
    lista_tablero=[]
    victoria=False
    fin=False

#=================== PROGRAMA PRINCIPAL ============================

#LISTAS
lista_tablero=[]
jugadores=[]

#DICCIONARIOS
p1=dict()
p2=dict()

#VARIABLES
victoria=False
fin=False

#=================== EMPIEZA EL JUEGO ============================
mostrarMenu()
while victoria==False and fin==False:
    crearTablero()
    insertarFicha(seleccionJugador1())
    mostrarMenuFin()