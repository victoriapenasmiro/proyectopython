def finPartida():
    global fin
    if victoria==False and fin==False:
        if "_|" in lista_tablero[0]:
            fin=False
        else:
            fin=True
            print ("\n¡EMPATE! FIN DE PARTIDA")