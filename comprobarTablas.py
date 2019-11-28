esta condicion deberia empezar a partir de x movimientos
def comprobarEmpate():
    for i in range(len(lista_tablero)):
        if "_|" in lista_tablero[i]: #entra en la lista si hay huecos vacios
            for j in range(1,len(lista_tablero[i])):
                #si tengo tres huecos vacios de forma h,v o d
                # --> paso al siguiente turno
                #verificacion vertical
                if i==0 or i==1 or i==2:#si i es 3,4 o 5 es porqué no hay
                                        #4 huecos disponibles para poder ganar
                    if lista_tablero[i][j]=="_|":
                        #verifico si hay tres huecos
                        if lista_tablero[i+1][j]=="_|" and\
                        lista_tablero[i+2][j]=="_|":
                            victoria=False
                            break
                        #verifico si hay dos huecos y dos fichas iguales a continuación
                        elif lista_tablero[i+1][j]=="_|" and\
                        ((lista_tablero[i+2][j]==p1["letra"] and\
                        lista_tablero[i+3][j]==p1["letra"]) or\
                        (lista_tablero[i+2][j]==p2["letra"] and\
                        lista_tablero[i+3][j]==p2["letra"])):
                            victoria=False
                            break
                        #verifico si hay un hueco y tres fichas iguales a continuación
                        elif (lista_tablero[i+1][j]==p1["letra"] and\
                        lista_tablero[i+2][j]==p1["letra"] and\
                        lista_tablero[i+3][j]==p1["letra"]) or\
                        (lista_tablero[i+1][j]==p2["letra"] and\
                        lista_tablero[i+2][j]==p2["letra"] and\
                        lista_tablero[i+3][j]==p2["letra"]):
                            victoria=False
                            break
                #bastan tres huecos vacios, ya que si solo hay una ficha precedente es una posible victoria
                #verificar horizontal
                if j<5:
                    """hay 6 posibilidades para cada ficha:
                    1. ficha + 3 espacios
                    2. 2 fichas + 2 espacios
                    3. 3 fichas + 1 espacios
                    4. espacio + 3 fichas
                    5. 2 espacios + 2 fichas
                    6. 3 espacios + 1 ficha"""
                    #ficha + 3 espacios
                    if lista_tablero[i][j]!="_|":
                        if lista_tablero[i][j+1]=="_|" and\
                        lista_tablero[i][j+2]=="_|" and\
                        lista_tablero[i][j+3]=="_|":
                            victoria=False
                            break
                    #2 fichas + 2 espacios
                    elif lista_tablero[i][j]==p1["letra"]:
                        if lista_tablero[i][j+1]==p1["letra"] and\
                        lista_tablero[i][j+2]=="_|" and\
                        lista_tablero[i][j+3]=="_|":
                            victoria=False
                            break
                    elif lista_tablero[i][j]==p2["letra"]:
                        if lista_tablero[i][j+1]==p2["letra"] and\
                        lista_tablero[i][j+2]=="_|" and\
                        lista_tablero[i][j+3]=="_|":
                            victoria=False
                            break
                    #3 fichas + 1 espacios
                    elif lista_tablero[i][j]==p1["letra"]:
                        if lista_tablero[i][j+1]==p1["letra"] and\
                        lista_tablero[i][j+2]==p1["letra"] and\
                        lista_tablero[i][j+3]=="_|":
                            victoria=False
                            break
                    elif lista_tablero[i][j]==p2["letra"]:
                        if lista_tablero[i][j+1]==p2["letra"] and\
                        lista_tablero[i][j+2]==p2["letra"] and\
                        lista_tablero[i][j+3]=="_|":
                            victoria=False
                            break
                    #espacio + 3 fichas
                    elif lista_tablero[i][j]=="_|":
                        if lista_tablero[i][j+1]==p2["letra"] and\
                        lista_tablero[i][j+2]==p2["letra"] and\
                        lista_tablero[i][j+3]==p2["letra"]:
                            victoria=False
                            break
                    elif lista_tablero[i][j]=="_|":
                        if lista_tablero[i][j+1]==p1["letra"] and\
                        lista_tablero[i][j+2]==p1["letra"] and\
                        lista_tablero[i][j+3]==p2["letra"]:
                            victoria=False
                            break
                    #2 espacios + 2 fichas
                    elif lista_tablero[i][j]=="_|":
                        if lista_tablero[i][j+1]=="_|" and\
                        lista_tablero[i][j+2]==p2["letra"] and\
                        lista_tablero[i][j+3]==p2["letra"]:
                            victoria=False
                            break
                    elif lista_tablero[i][j]=="_|":
                        if lista_tablero[i][j+1]=="_|" and\
                        lista_tablero[i][j+2]==p1["letra"] and\
                        lista_tablero[i][j+3]==p1["letra"]:
                            victoria=False
                            break
                    #3 espacios + 1 ficha
                    elif lista_tablero[i][j]=="_|":
                        if lista_tablero[i][j+1]=="_|" and\
                        lista_tablero[i][j+2]=="_|" and\
                        lista_tablero[i][j+3]==p2["letra"]:
                            victoria=False
                            break
                    elif lista_tablero[i][j]=="_|":
                        if lista_tablero[i][j+1]=="_|" and\
                        lista_tablero[i][j+2]=="_|" and\
                        lista_tablero[i][j+3]==p1["letra"]:
                            victoria=False
                            break
                #verificar diagonal -->
                elif lista_tablero[i][j]=="_|" and j<5:
                    if lista_tablero[i-1][j+1]=="_|" and\
                    lista_tablero[i-2][j+2]=="_|":
                        victoria=False
                        break
                #verficar diagonal <--
                elif j>=5 and lista_tablero[i][j]=="_|":
                    if lista_tablero[i-1][j-1]=="_|" and\
                    lista_tablero[i-2][j-2]=="_|":
                        victoria=False
                        break
                else:
                    fin=True
                    print("YA NO HAY MÁS MOVIMIENTOS POSIBLES. ¡FIN DE PARTIDA!")
                    break
