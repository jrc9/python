lista=[]
listaTemp=[]
ban=True




for i in range(11):
    listaTemp.append(i)

lista.append(listaTemp)
listaTemp=[]

for i in range(10):
    ban=True
    listaTemp=[]
    for e in range(11):
        if(ban==True):
            listaTemp.append(i+1)
            ban=False
        else:
            listaTemp.append(0)
    lista.append(listaTemp)


for i in lista:
    print(i)





def multiplicar(lista):
    for i in range(10):
        for e in range(10):
            lista[i+1][e+1]=lista[0][e+1]*lista[i+1][0]     
    for f in lista:
     print(f) 

multiplicar(lista)

