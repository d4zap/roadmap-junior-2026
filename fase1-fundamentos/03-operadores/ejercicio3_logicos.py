# Ana
edad_ana = 20
id_ana = True

# Luis
edad_luis = 17
id_luis = True

# María
edad_maria = 22
id_maria = False

# Pedro
edad_pedro = 16
id_pedro = False

pase_vip_luis = True
ingreso_luis_vip = edad_luis >= 18 or pase_vip_luis

lista_negra_pedro = True 


ingreso1= edad_ana>=18 and id_ana 
ingreso_luis_vip = edad_luis >= 18 or pase_vip_luis
ingreso3= edad_maria>=18 and id_maria
puede_entrar_not = not lista_negra_pedro

print("pueden ingresar ana: ",ingreso1)
print("¿Puede ingresar Luis con VIP?", ingreso_luis_vip)
print("pueden ingresar maria: ",ingreso3)
print("¿Puede entrar Pedro? (no lista negra)", puede_entrar_not)