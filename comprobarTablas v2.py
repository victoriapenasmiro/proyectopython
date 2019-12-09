def comprobarEmpate(jugador):
    global fin
    contador_espacios=0
    contador_ficha=0
    while (contador_espacios+contador_ficha==4):
        for i in range(len(lista_tablero)):#verificacion vertical
            if i==0 or i==1 or i==2:#si i es 3,4 o 5 hay 4 huecos para ganar
                for j in range(1,len(lista_tablero[i])):
                    if lista_tablero[i][j]=="_|":
                        contador_espacios+=1
                    if lista_tablero[i+1][j]=="_|":
                        contador_espacios+=1
                        if lista_tablero[i+2][j]=="_|":
                            contador_espacios+=1
                        else:
                            contador_ficha+=1
                            ficha=jugador["letra"]
                            if lista_tablero[i+3][j]==ficha+"|":
                                contador_ficha+=1
                    else:
                        contador_ficha+=1
                        ficha=jugador["letra"]
                        if lista_tablero[i+2][j]==ficha+"|":
                            contador_ficha+=1
                                if lista_tablero[i+3][j]==ficha+"|":
                                    contador_ficha+=1
    if (contador_espacios+contador_ficha<4):
        fin=True
        print ("\n¡EMPATE!¡YA NO HAY MÁS MOVIMIENTOS POSIBLES PARA VICTORIA!\n")
