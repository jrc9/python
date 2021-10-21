from random import *
from io import *
import time

def numeros():
    archivo_general=open("numero.txt","w")
    lista=sample(range(1,366),365)
    lista.sort()
    for i in lista:
        archivo_general.write(str(i)+"\n")
    print(lista)
    archivo_general.close()


def generaNumeros(lista):

    archivo_general=open("numero.txt","w")

    for i in lista:
        archivo_general.write(str(i))
        
        
    archivo_general.close()

def sorteo(nombre,fecha):

    archivo_sorteo=open("sorteo.txt","a")
    archivo_general=open("numero.txt","r")

    lista=archivo_general.readlines()
    numero=lista[randint(0,len(lista)-1)]
    numerotxt=numero.replace("\n","")
    archivo_sorteo.write("A "+nombre+" le toco pagar: "+numerotxt+" el "+fecha+"\n")
    print("Se escribio en sorteo: " + str(numero))
    lista.remove(numero)
    print("Se elimino: "+numero)
       
    generaNumeros(lista)
    archivo_general.close()
    archivo_sorteo.close()

nombre=input("A quien le toca: ")
fecha=str(time.strftime("%d/%m/%y"))

sorteo(nombre,fecha)


