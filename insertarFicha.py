def insertarFicha(jugador):
    global victoria
    global fin
    if jugador==0:
        jugador=p1
    else:
        jugador=p2
    while victoria==False and fin==False:
        columna=int(input("\nPor favor " + jugador.get("nombre") + " dime la columna: "))
        while columna>7 or columna<1:#veririfición número correcto de columna
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
        comprobarVictoriaHorizontal(i,jugador)
        comprobarVictoriaDiagonal(jugador)
        finPartida()
        if victoria==False and fin==False:
            if jugador==p1:
                jugador=p2
            else:
                jugador=p1
    volverJugar ()