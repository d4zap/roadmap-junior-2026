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

def registrar_usuario():
    nombre = input("ingrese su nombre: ")
    edad = int(input("Ingresar tu edad: "))
    pesoKG = int(input("Ingresa tu peso en KG: "))
    altura = float(input("Ingresa tu estatura en metros: "))

    IMC= pesoKG / (altura*altura)

    if IMC<=18.5: 
        categoria ="Bajo peso"
        
    elif IMC>18.5 and IMC<=24.9:
        categoria ="peso normal"
    elif IMC>=25 and IMC<29.9:
           categoria ="sobre peso"
    else :
           categoria ="obesidad"

    puede_inscribirse= edad > 15 and IMC >=10

    return{
     "nombre": nombre,
     "edad": edad,
     "IMC": IMC,
     "categoria": categoria,
     "puede_inscribirse": puede_inscribirse,
       
    }       
datos = registrar_usuario()
print(datos)
