import random

lista=[]
bandera=False

for i in range(10):

    bandera=False

    while bandera==False:
    
         aleatorio=random.randint(1,10)
    
         if(aleatorio in lista):
             bandera=False
           
         else:
             lista.append(aleatorio)
             bandera=True

print(lista)
             

def ordenar(lista):

    longitud=len(lista) 
    ban=True

    while ban==True:
        ban=False

        for i in range(longitud - 1):
             if(lista[i]>lista[i+1]):
                lista[i],lista[i+1]=lista[i+1],lista[i]
                ban=True
    print (lista)

ordenar(lista)


  



