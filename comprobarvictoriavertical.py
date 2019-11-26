def comprobarVictoriaVertical(i,jugador,columna):
    global victoria
    if i==0 or i==1 or i==2:
        if lista_tablero[i][columna]==jugador.get("letra") + "|" and\
        lista_tablero[i+1][columna]==jugador.get("letra") + "|" and\
        lista_tablero[i+2][columna]==jugador.get("letra") + "|" and\
        lista_tablero[i+3][columna]==jugador.get("letra") + "|":
            victoria=True
            print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")
            
    return victoria
