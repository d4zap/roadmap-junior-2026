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

ingreso1= edad_ana>=18 and id_ana 
ingreso2= edad_luis>=18 and id_luis 
ingreso3= edad_maria>=18 and id_maria
ingreso4= edad_pedro>=18 and id_pedro

print("pueden ingresar ana: ",ingreso1)
print("pueden ingresar luis: ",ingreso2)
print("pueden ingresar maria: ",ingreso3)
print("pueden ingresar pedro: ",ingreso4)