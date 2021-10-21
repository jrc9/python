import random

lista=[]

for i in range(5):
    lista_temp=[]

    for i in range(5):
       lista_temp.append(random.randint(1,9))

    lista.append(lista_temp)

for e in lista:
    print(e)

menu=int(input("Que desea hacer 1.-suma Fila 2.-Suma Columna 3.-Suma diagonal 4.-Suma todo"))


def sumaFila(fila):

    suma=0
    for i in lista[fila-1]:
            suma=suma+i
    print("La suma de la fila es: " + str(suma))

def sumaColumna(columna):
    suma=0
    for i in lista:
        suma=suma+i[columna-1]
    print("La suma de la columna es " + str(suma))

    
def sumaDiagonal():
    suma=0
    cont=0
    for i in lista:
        suma=suma+i[cont]
        cont+=1
    print("La suma de la diagonal es: "+str(suma))


def sumaTodo():

    suma=0

    for i in lista:
        for e in i:
            suma=suma+e

    print("La suma de todo es: "+str(suma) )


if(menu==1):
    fila=int(input("Que fila quiere sumar: "))
    sumaFila(fila)
elif(menu==2):
    columna=int(input("Que columna quiere sumar"))
    sumaColumna(columna)
elif(menu==3):
    sumaDiagonal()
elif(menu==4):
    sumaTodo()




