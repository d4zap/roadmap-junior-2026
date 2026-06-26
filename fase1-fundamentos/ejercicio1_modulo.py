

##Escribe código en Python que: Guarde 17 en una variable caramelos
##Guarde 5 en una variable tamano_grupo
##Calcule los grupos completos usando //
#Calcule los caramelos sobrantes usando %
#Imprima ambos resultados con print()

#Pistas de sintaxis Python que necesitas:

#Asignación: variable = valor
#Imprimir texto + variable junto: print("texto", variable)

print("tenemos 17 caramelos y necesitamos guardarlos en grupos de 5")
print()
print("cuantos caramelos podemos agrupar?")
print()
print("cuantos caramelos sobran?")
print()      

caramelos = 17
tamano_grupo = 5

Gtotales=(caramelos//tamano_grupo)
Csobrantes=(caramelos%tamano_grupo)

print('los caramelos sobrantes son=', Csobrantes)
print()
print('los caramelos agrupados son=', Gtotales)