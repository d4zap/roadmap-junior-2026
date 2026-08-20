#El gimnasio FitZone necesita un sistema básico de registro que haga lo siguiente:
#Pedir los datos del usuario:
#Nombre
#Edad
#Peso en kg
#Altura en metros
#Calcular automáticamente el IMC con la fórmula:
#IMC = peso / (altura * altura)
#Clasificar el IMC con estas categorías:
#Menos de 18.5 → "Bajo peso"
#Entre 18.5 y 24.9 → "Peso normal"
#Entre 25 y 29.9 → "Sobrepeso"
#30 o más → "Obesidad"
#Verificar si puede inscribirse al gimnasio:
#Debe ser mayor de 15 años
#Su IMC no debe ser menor de 10 (dato inválido)
#Todo esto dentro de una función llamada registrar_usuario() que retorne un diccionario con todos los datos (nombre, edad, IMC, categoría, puede_inscribirse)
#Llamar la función e imprimir un reporte final con todos los datos del usuario

nombre = input("ingrese su nombre: ")

edad = int(input("Ingresar tu edad: "))

pesoKG = int(input("Ingresa tu peso en KG: "))

altura = float(input("Ingresa tu estatura en metros: "))

IMC= pesoKG / (altura*altura)


def autoIMC ():
    if IMC<=18.5: 
     print("Bajo peso")
    elif IMC>18.5 and IMC<=24.9:
     print("peso normal")
    elif IMC>=25 and IMC<29.9:
        print("sobrepeso")
    else :
        print("obesidad")     

def Medad ():        
    if edad >15:
       return True
    else:
       return False 

resultado = Medad()


def registrar_usuario():

 print(f"Su nombre es: {nombre} ")
 print(f"Su edad es: {edad} ")
 print (f"su IMC es: {IMC} ")
 print(f"Su peso es: {pesoKG}kg ")

 if resultado:
   print ("Bienvenido, puede entrar")
 else:
   print ("lo sentimos, no puede entrar")   

 print(f"Su estatura es: {altura} ")
 autoIMC()

