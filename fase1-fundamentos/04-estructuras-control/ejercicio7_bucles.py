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