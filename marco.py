lista=[]
listaTemp=[]
tamaño=int(input("Dame el tamaño de la matriz: "))

for i in range(tamaño):
    for e in range(tamaño):
        listaTemp.append(0)
    lista.append(listaTemp)
    listaTemp=[]

lon=len(lista)

def derecha(lista):

    for i in range(lon):
        lista[0][i]=1
        lista[lon-1][i]=1    

def abajo(lista):
    for i in range(lon):
        lista[i][0]=1
        lista[i][lon-1]=1    


derecha(lista)
abajo(lista)

for f in lista:
    print(f)