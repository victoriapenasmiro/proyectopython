def comprobarVictoriaHorizontal(i,jugador):
    global victoria
    contador=0
    #comprobamos que hay almenos hay 4 fichas repetidas en la fila
    if lista_tablero[i].count(jugador.get("letra") + "|")>=4:
        #Empieza desde la posicion 1,porque en la 0 hay un | siempre
        for j in range(1,len(lista_tablero[i])):
            if lista_tablero[i][j]==jugador.get("letra") + "|":
                contador+=1
            if contador==4:
                victoria=True
                print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")
                break
            if j+1!=8:
                if lista_tablero[i][j+1]!=jugador.get("letra") + "|":
                    contador=0
    return victoria


