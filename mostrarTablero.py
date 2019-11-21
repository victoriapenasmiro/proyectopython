num_columnas=[1,2,3,4,5,6,7]
lista_tablero=[["|","_","|","_","|","_","|","_","|","_","|","_","|","_","|"]\
               ,["|","_","|","_","|","_","|","_","|","_","|","_","|","_","|"]\
               ,["|","_","|","_","|","_","|","_","|","_","|","_","|","_","|"],\
               ["|","_","|","_","|","_","|","_","|","_","|","_","|","_","|"],\
               ["|","_","|","_","|","_","|","_","|","_","|","_","|","_","|"],\
               ["|","_","|","_","|","_","|","_","|","_","|","_","|","_","|"]]

def mostraTablero():
    global lista_tablero
    for i in range(len(num_columnas)):
        print(num_columnas[i],end="")
    for i in range(len(lista_tablero)):
        for j in range(len(lista_tablero[i])):
             if j==(len(lista_tablero[i])-1):
                   print(lista_tablero[i][j])
             else:
                   print(lista_tablero[i][j],end="")


mostraTablero()
                            

