import random
import time

def mostrarMenu():
    print("*****************************************************\n" +
          "                  JUEGO CONECTA 4\n"
          "*****************************************************\n" +
          "                 NORMAS DEL JUEGO:\n" +
          "Conecta 4 es un juego para dos jugadores. El tablero\n" +
          "consta de 6 filas y 7 columnas. Cada jugador deberá\n" +
          "seleccionar el carácter con el que van a jugar, que\n" +
          "puede ser X u O. Cada jugador tiene un solo movimiento\n" +
          "permitido en su turno.\n"
          "El jugador debe escoger en qué columna quiere poner\n" +
          "el carácter (X o O) que ha seleccionad. Los caracteres se\n" +
          "irán ubicando en las filas inferiores de la columna seleccionada,\n" +
          "amontonándose uno encima de otro.\n" +
          "********************************************************\n" +
          "********************************************************")
    global jugadores
    global jugadorinicial
    p1=dict()
    p1["nombrep1"]=[input("Jugador 1, indica tu nombre: ")]
    letraP1 = input("Elige X o O:")
    while not (letraP1 == 'X' or letraP1 == 'O' or letraP1 == 'x' or letraP1 == 'o'):
        print('Letra incorrecta.Elige X or O?')
        letraP1 = input("X o O")
    if letraP1 == 'X' or letraP1 == 'x':
        print("Has elegido X")
        if letraP1 == "x":
            letraP1 = "X"
    elif letraP1 == 'O' or letraP1 == 'o':
        print("Has elegido O")
        if letraP1 == "o":
            letraP1 = "O"
    p1["letraP1"]=[letraP1]
    jugadores.append(p1)
    
    p2=dict()
    p2["nombrep2"]=[input("Jugador 2,indica tu nombre: ")]

    if letraP1 == "X":
        letraP2 = "O"
    elif letraP1 == "O":
        letraP2 = "X"

    p2["letraP2"]=[letraP2]
    jugadores.append(p2)
    
    print(p2.get("nombrep2"),"te ha tocado el carácter:",p2.get("letraP2"))
    random.seed(time.time())
    jugadorinicial=jugadores[random.randint(0,1)]

    #for para acceder al nombre del jugador que ha sido seleccionado
    print("Comienza:",end="")
    """tengo un error, me impime dos veces el jugador que va a empezar. hay que investigar"""
    for i in (len(jugadores),[jugadorinicial]):
        if jugadorinicial==0:
            print(p1.get("nombrep1"))

        else:
            print(p2.get("nombrep2"))

    return jugadorinicial

#este procedimiento imprime el tablero
def mostrarTablero(jugador1):
    global lista_tablero
    for i in range(len(num_columnas)):
        if i==(len(num_columnas)-1):
            print(num_columnas[i])
        else:    
            print(num_columnas[i],end="")
    for i in range(len(lista_tablero)):
        for j in range(len(lista_tablero[i])):
             if j==(len(lista_tablero[i])-1):
                   print(lista_tablero[i][j])
             else:
                   print(lista_tablero[i][j],end="")
                   
    insertarFicha(jugador1)

#este procedimiento inserta las fichas de los jugadores
def insertarFicha(jugador1):
    #mientras se trate del jugador con valor O ejecuta esto:
    columna=int(input("\nPor favor, JUGADOR1 dime la columna: "))
    #aquí veririficamos que el usuario indique un número correcto de columna para colocar su ficha
    while columna>7 or columna<1:
        columna=int(input("la columna que has indicado no es correcta, dime otra: "))

    #recorremos la columna indicada por el usuario para colocar su ficha en el hueco disponible
    #for jugador que ha seleccionado la O
    for i in range(len(lista_tablero)-1,-1,-1):
        if lista_tablero[i][columna]=="_|":
            lista_tablero[i][columna]="O|"
            break
        elif lista_tablero[0][1]!="_|":
            columna=int(input("la columna que has indicado está completa, dime otra: "))

    mostrarTablero()
    #verificar victoria

#VARIABLES
num_col=" 1 2 3 4 5 6 7 "
num_columnas=[" ",1," ",2," ",3," ",4," ",5," ",6," ",7]
lista_tablero=[["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"]]
jugadores=[]
victoria=False
jugadorinicial=" "

#Comienza el procedimiento
mostrarMenu()
while victoria==False:
        mostrarTablero(jugadorinicial)
