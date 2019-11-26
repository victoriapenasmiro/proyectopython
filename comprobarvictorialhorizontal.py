def comprobarVictoriaHorizontal(i,jugador,columna):
    global victoria
    contador=0
    for j in lista_tablero[i]:
        if lista_tablero[i][j]==(jugador.get("letra") + "|")
            contador+=1
            if contador==4:
                break
                victoria=True
                print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")

    return victoria

    """
    if lista_tablero[i][columna+1]==(jugador.get("letra") + "|") and\
    lista_tablero[i][columna+2]==(jugador.get("letra") + "|") and\
    lista_tablero[i][columna+3]==(jugador.get("letra") + "|") and\
    
    elif lista_tablero[i][columna-1]==(jugador.get("letra") + "|") and\
    lista_tablero[i][columna-2]==(jugador.get("letra") + "|") and\
    lista_tablero[i][columna-3]==(jugador.get("letra") + "|") and\
    
    elif lista_tablero[i][columna+1]==(jugador.get("letra") + "|") and\
    lista_tablero[i][columna+2]==(jugador.get("letra") + "|") and\
    lista_tablero[i][columna-1]==(jugador.get("letra") + "|") and\
    
    elif lista_tablero[i][columna+1]==(jugador.get("letra") + "|") and\
    lista_tablero[i][columna-2]==(jugador.get("letra") + "|") and\
    lista_tablero[i][columna-1]==(jugador.get("letra") + "|") and\"""



