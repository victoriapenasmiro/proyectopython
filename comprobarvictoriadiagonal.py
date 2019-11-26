def comprobarVictoriaDiagonal(jugador):
    global victoria
    for i in range(len(lista_tablero)-1,-1,-1):
        for j in range(len(lista_tablero[i])):
            if j<5 and lista_tablero[i][j]==jugador.get("letra") + "|":
                if lista_tablero[i-1][j+1]==jugador.get("letra") + "|" and\
                lista_tablero[i-2][j+2]==jugador.get("letra") + "|" and\
                lista_tablero[i-3][j+3]==jugador.get("letra") + "|":
                    victoria=True
                    print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")
                    break
            elif j>=5 and lista_tablero[i][j]==jugador.get("letra") + "|":
                if lista_tablero[i-1][j-1]==jugador.get("letra") + "|" and\
                lista_tablero[i-2][j-2]==jugador.get("letra") + "|" and\
                lista_tablero[i-3][j-3]==jugador.get("letra") + "|":
                    victoria=True
                    print("\n",jugador.get("nombre"),"¡¡¡HAS GANADO!!!")
                    break
    return victoria