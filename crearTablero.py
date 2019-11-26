def crearTablero(filas,columnas):
    global lista_tablero
    print (NUMEROS)
    for i in range (filas):
        lista_columnas=[]
        for j in range (columnas):
            if j == 0:
                lista_columnas.append("|")
                print ("|", end = "")
            elif j == 7:
                lista_columnas.append("_|")
                print ("_|")
            else:
                lista_columnas.append("_|")
                print ("_|", end = "")
        lista_tablero.append(lista_columnas)
