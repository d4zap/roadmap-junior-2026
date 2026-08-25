
# busqueda lineal

def busqueda_lineal(lista,objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i     # retorna la posicion donde lo encontro
    return -1        #-1 signfica "no encontrado"
cedulas = [123456,789012, 345678, 111222, 999888]

resultado = busqueda_lineal(cedulas,345678)
print("encontrado en posicion:", resultado)

resultado2 = busqueda_lineal (cedulas,000000)
print("Encontrado en posicion:", resultado2)


def busqueda_binaria(lista,objetivo):
    izquierda= 0
    derecha= len(lista) -1

    while izquierda <= derecha:
        medio= (izquierda + derecha) //2

        if lista[medio]== objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda= medio+1
        else:
            derecha = medio -1
    return -1     

cedulas_ordenadas = [111222, 123456, 345678, 789012, 999888]   

resultado3 = busqueda_binaria(cedulas_ordenadas,345678)
print("Binaria - encontrado en posicion:", resultado3)