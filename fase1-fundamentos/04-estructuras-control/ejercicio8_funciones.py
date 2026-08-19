
edad = int(input("Cuantos años tienes: "))
respuesta = input(" tienes identificacion (si/no): ")
tienes_id = respuesta == "si" 


def verificar_entrada (edad, id):
   if edad>= 18 and id:
      return True
   else:
      return False

resultado = verificar_entrada(edad, id)

if resultado:
   print ("Bienvenido, puede entrar")
else:
   print ("lo sentimos, no puede entrar")   