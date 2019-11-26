def volverJugar ():
    global victoria
    global fin
    global lista_tablero
    global jugadores
    global p1
    global p2
    global letraP1
    global letraP2
    global jugadorinicial
    if victoria==True and fin==True:
        repetir=input("\nQuieres volver a jugar Y/N?")
        while repetir!="N" and repetir!="Y" and repetir!="y" and repetir!="n":
            repetir = input("Opcion incorrecta.Quieres volver a jugar Y/N?")
        if repetir=="Y" or repetir=="y":
            #VARIABLES --> Reseteo de valores
            lista_tablero=[]
            jugadores=[]
            p1=dict()
            p2=dict()
            letraP1=" "
            letraP2=" "
            victoria=False
            fin=False
            jugadorinicial=" "
            mostrarMenu()
            crearTablero(FILAS,COLUMNAS)
        else:
            print("\n¡HASTA PRONTO!")