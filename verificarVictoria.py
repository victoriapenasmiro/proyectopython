num_columnas=[" ",1," ",2," ",3," ",4," ",5," ",6," ",7]
lista_tablero=[["|","_","|","_","|","_","|","_","|","_","|","_","|","_","|"]\
               ,["|","_","|","_","|","_","|","_","|","_","|","_","|","_","|"]\
               ,["|","_","|","_","|","_","|","_","|","_","|","_","|","_","|"],\
               ["|","_","|","_","|","_","|","_","|","_","|","_","|","_","|"],\
               ["|","_","|","_","|","_","|","_","|","_","|","_","|","_","|"],\
               ["|","_","|","_","|","_","|","_","|","_","|","_","|","_","|"]]

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


mostrarTablero()

columna=int(input("dime la columna: "))
while columna!=1 and columna!=2 and columna!=3 and columna!=4 and columna!=5 and columna!=6 and columna!=7:
    columna=int(input("la columna que has indicado no es correcta, dime otra: "))

for i in range(len(lista_tablero)-1,-1,-1):
    if lista_tablero[i][columna]=="_":
        lista_tablero[i][columna]="O"
print=(mostraTablero())
            
    
