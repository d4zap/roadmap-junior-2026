print ("---numeros del 1 al 10---")

for numero in range (1,11):
    print (numero)

print ("---numeros del 1 al 20---")

for numero2 in range (1,21):  
    if numero2 % 2 == 0:
       print (numero2)


print("---adivina el numero---")
numero_secreto = 7
intento = 0

while intento != numero_secreto:
    intento = int (input("Adivina el numero: "))
    if intento != 7:
        print("vuelve a intentarlo")
print("Correcto")

     


print("---adivina con limite de intentos---")
numero_secretos = 5
intento = 0
intentos = 0

while intentos < 3:
     intento = int (input("adivina el numero: "))
     
     if intento == 5:
         print ("correcto")
         break
     else: 
         intentos += 1
         print ("vuelve a intentarlo, tienes ", 3 - intentos  ,"intentos") 

     if intentos == 3:
         print ("perdiste, el numero era ", numero_secretos)


