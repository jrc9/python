cadena1=input("dame la cadena: ")
cadena1=cadena1.replace(" ","")
cadena2=""

longitud=len(cadena1)

for i in range(longitud):
        cadena2=cadena2+cadena1[longitud-1]
        longitud-=1

if(cadena1==cadena2):
    print("Es palindromo")
else:
    print("No es palindromo")



    