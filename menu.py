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
    p1["letra"]=letraP1.upper()
    jugadores.append(p1)
    p2["nombre"]=input("Jugador 2,indica tu nombre: ")
    if p1["letra"] == "X":
        p2["letra"]="O"
    elif p1["letra"] == "O":
        p2["letra"]="X"
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







