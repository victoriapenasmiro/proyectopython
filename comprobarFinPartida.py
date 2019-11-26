def finPartida():
    global fin
    fin=True
    if "_|" in lista_tablero[0]:
        fin=False
    else:
        print ("\n¡EMPATE! FIN DE PARTIDA")
        
def volverJugar ():
    global victoria
    repetir=input("Quieres volver a jugar Y/N?")
    if repetir == "Y":
        victoria=False
        mostrarMenu()
        crearTablero(FILAS,COLUMNAS)
        while victoria==False:
            insertarFicha(jugadorinicial)
    elif repetir !="N" or repetir !="Y":
            repetir = input("Opcion incorrecta.Quieres volver a jugar Y/N?")