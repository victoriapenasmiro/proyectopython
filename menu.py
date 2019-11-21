import random
import time
def printearMenu():
    print ("*****************************************************")
    print("                 JUEGO CONECTA 4")
    print("*****************************************************")
    print("                 NORMAS DEL JUEGO:")

    print("Conecta 4 es un juego para dos jugadores. El “tablero”")
    print("consta de 6 filas y 7 columnas. Cada jugador deberá")
    print("seleccionar el carácter con el que van a jugar, que")
    print("puede ser X u O. Cada jugador tiene un solo")
    print("movimiento permitido en su turno.")

    print("El jugador debe escoger en qué columna quiere")
    print("“colocar” su carácter. Los caracteres se irán ubicando")
    print("en las filas inferiores de la columna seleccionada, se")
    print("irán amontonando uno encima de otro.")
    print("****************************************************************")
    print("****************************************************************")
    p1 = input("Jugador 1,Selecciona un nombre")
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

    p2 = input("Jugador 2,Selecciona un nombre")

    if letraP1 == "X":
        letraP2 = "O"
    elif letraP1 == "O":
        letraP2 = "X"
    random.seed(time.time())
    jugadorinicial = (random.choice([p1, p2]))

    print("Comienza:", jugadorinicial)


printearMenu()







