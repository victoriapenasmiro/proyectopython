import random
import time

def mostrarMenu():
    #Isma creará una función que sea mostrarInstrucciones con return instrucciones y enviar a esta función
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
    global p1
    global p2
    global letraP1
    global letraP2
    
    p1["nombre"]=input("Jugador 1, indica tu nombre: ")
    letraP1 = input("Elige X o O:")#probar si podemos eliminar la variable y hacer directamente p1["letra"]
    while not (letraP1=='X' or  letraP1=='O' or letraP1=='x' or letraP1=='o'):
        letraP1=input('Letra incorrecta.Elige X or O?')
    #Convertir letra a mayúscula e insertamos en la lista como diccionario
    """if letraP1 == "x":#podemos eliminar este código
        letraP1 = "X"
    elif letraP1 == "o":
        letraP1 = "O"      
    p1["letra"]=letraP1"""
    p1["letra"]=letraP1.upper()
    jugadores.append(p1)
    p2["nombre"]=input("Jugador 2,indica tu nombre: ")
    if p1["letra"] == "X":
        #letraP2 = "O"
        p2["letra"]="O"
    elif p1["letra"] == "O":
        #letraP2 = "X"
        p2["letra"]="X"
    #p2["letra"]=letraP2
    jugadores.append(p2)
    print(p2.get("nombre"),"te ha tocado el carácter:",p2.get("letra"))
    
    random.seed(time.time())
    jugadorinicial=random.randint(0,1)

    print("Empieza ",end="")    
    if jugadorinicial==0:
        print(p1.get("nombre") + "!\n")
    else:
        print(p2.get("nombre") + "!\n")

    return jugadorinicial

#este procedimiento imprime el tablero
"""Isma creará una función que cree el tablero y lo devuelva"""
def mostrarTablero():
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

#este procedimiento inserta las fichas de los jugadores
def insertarFicha(jugador):
    global victoria
    if jugador == 0:
        jugador=p1
    else:
        jugador=p2
        
    while victoria==False:
        columna=int(input("\nPor favor " + jugador.get("nombre") + " dime la columna: "))
        if lista_tablero[0][columna]!="_|":
            columna=int(input("la columna que has indicado está completa, dime otra: "))
        #veririfición número correcto de columna
        while columna>7 or columna<1:
            columna=int(input("la columna que has indicado no es correcta, dime otra: "))
            if lista_tablero[0][columna]!="_|":
                columna=int(input("la columna que has indicado está completa, dime otra: "))
        #recorremos la columna indicada por el usuario para colocar su ficha en el hueco disponible
        for i in range(len(lista_tablero)-1,-1,-1):
            if lista_tablero[i][columna]=="_|":
                lista_tablero[i][columna]=jugador.get("letra") + "|"
                break
        mostrarTablero()
        comprobarVictoriaVertical(i,jugador,columna)
        if victoria==False:
            if jugador==p1:
                jugador=p2
            else:
                jugador=p1

def comprobarVictoriaVertical(i,jugador,columna):#el valor de victoria no aplica bien
    global victoria
    if i==0 or i==1 or i==2:
        if lista_tablero[i][columna]==(jugador.get("letra") + "|") and\
        lista_tablero[i+1][columna]==(jugador.get("letra") + "|") and\
        lista_tablero[i+2][columna]==(jugador.get("letra") + "|") and\
        lista_tablero[i+3][columna]==jugador.get("letra") + "|":
            victoria=True
            print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")
            
    return victoria
    
#VARIABLES
num_columnas=[" ",1," ",2," ",3," ",4," ",5," ",6," ",7]
lista_tablero=[["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"]]
jugadores=[]
p1=dict()
p2=dict()
letraP1=" "
letraP2=" "
victoria=False
jugadorinicial=" "

#Comienza el procedimiento
mostrarMenu()
while victoria==False:
    mostrarTablero()
    insertarFicha(jugadorinicial)
