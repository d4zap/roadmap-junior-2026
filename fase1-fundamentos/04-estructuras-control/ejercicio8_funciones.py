

def verificar_entrada (edad, id):
   if edad>= 18 and id:
      print ("puede entrar")
   else:
     print (" no puede entrar")

verificar_entrada (20,True)
verificar_entrada (17,True)
verificar_entrada (22,False)
verificar_entrada (16,False)