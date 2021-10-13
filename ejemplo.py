correo=input("Dame tu correo")
flag=0
cont=0
lista=[]


for i in correo:
        if(i=="@"):
            flag=1


        if(flag==1):
             lista.append(i)

for e in lista:
    if(e=="@" or e=="."):
        cont+=1

if(cont==2):
    print("Es un correo valido")
else:
    print("No es un correo valido")



           


