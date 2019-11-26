def crearTablero(filas,columnas):
    global lista_tablero
    for i in range (filas):
        lista_columnas=[]
        for j in range (columnas):
            if j == 0:
                lista_columnas.append("|")
            elif j == 7:
                lista_columnas.append("_|")
            else:
                lista_columnas.append("_|")
        lista_tablero.append(lista_columnas)
    mostrarTablero()
