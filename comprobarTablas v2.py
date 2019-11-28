def comprobarEmpate():
    contador_espacios=0
    contador_ficha=0
    while victoria==False:
        for i in range(len(lista_tablero)):
            #verificacion vertical
            if i==0 or i==1 or i==2:#si i es 3,4 o 5 es porqué no hay
                                    #4 huecos disponibles para poder ganar
                for j in range(1,len(lista_tablero[i])):
                    if lista_tablero[i][j]=="_|":
                        contador_espacios+=1
                    if lista_tablero[i+1][j]=="_|":
                        contador_espacios+=1
                        if lista_tablero[i+2][j]="_|":
                            contador_espacios+=1
                        else:
                            contador_ficha+=1

