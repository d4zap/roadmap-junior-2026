
edad = int(input("Cuantos años tienes: "))
respuesta = input(" tienes identificacion (si/no): ")
tienes_id = respuesta == "si" 


def verificar_entrada (edad,tiene_id):
   if edad>= 18 and tiene_id:
      return True
   else:
      return False

resultado = verificar_entrada(edad,tienes_id)

if resultado:
   print ("Bienvenido, puede entrar")
else:
   print ("lo sentimos, no puede entrar")   