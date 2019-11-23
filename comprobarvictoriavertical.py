def comprobarVictoriaVertical(i,jugador,columna):
    global victoria
    if lista_tablero[5] or lista_tablero[4] or lista_tablero[3]:
        if lista_tablero[i][columna]==(jugador.get("letra") + "|") and\
        lista_tablero[i-3][columna]==(jugador.get("letra") + "|") and\
        lista_tablero[i-2][columna]==(jugador.get("letra") + "|") and\
        lista_tablero[i-1][columna]==(jugador.get("letra") + "|"):
            victoria==True
            print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")

    elif lista_tablero[0] or lista_tablero[1] or lista_tablero[2]:
        if lista_tablero[i][columna]==(jugador.get("letra") + "|") and\
        lista_tablero[i+1][columna]==(jugador.get("letra") + "|") and\
        lista_tablero[i+2][columna]==(jugador.get("letra") + "|") and\
        lista_tablero[i+3][columna]==jugador.get("letra") + "|":
            victoria==True
            print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")
        
    return victoria
