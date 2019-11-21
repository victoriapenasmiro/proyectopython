#este procedimiento imprime el tablero
def mostrarTablero():
    global lista_tablero
    for i in range(len(num_columnas)):
        if i==(len(num_columnas)-1):
            print(num_columnas[i])
        else:    
            print(num_columnas[i],end="")
    for i in range(len(lista_tablero)):
        for j in range(len(lista_tablero[i])):
             if j==(len(lista_tablero[i])-1):
                   print(lista_tablero[i][j])
             else:
                   print(lista_tablero[i][j],end="")
                   
    insertarFicha()

#esta 
def insertarFicha():
#aquí veririficamos que el usuario indique un número correcto de columna para colocar su ficha
    #mientras variable jugador = variable jugador:
    columna=int(input("\nPor favor, JUGADOR1 dime la columna: "))
    while columna>7 or columna<1:
        columna=int(input("la columna que has indicado no es correcta, dime otra: "))

    #recorremos la columna indicada por el usuario para colocar su ficha en el hueco disponible
    #for jugador que ha seleccionado la O
    for i in range(len(lista_tablero)-1,-1,-1):
        if lista_tablero[i][columna]=="_|":
            lista_tablero[i][columna]="O|"
            break
        elif lista_tablero[0][1]!="_|":
            columna=int(input("la columna que has indicado está completa, dime otra: "))

    mostrarTablero()
    #verificar victoria

#VARIABLES
num_columnas=[" ",1," ",2," ",3," ",4," ",5," ",6," ",7]
lista_tablero=[["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"],\
               ["|","_|","_|","_|","_|","_|","_|","_|"]]

victoria=False

while victoria==False:
    mostrarTablero()
