

cola_clientes = []

# llega el cliente

cola_clientes.append("David") #primero en llegar
cola_clientes.append("Ana")   #segundo
cola_clientes.append("Luis")  # tercero

print("Cola actual:", cola_clientes)

#Atender al primero (FIFO)

atendido = cola_clientes.pop(0) #saca al primero

print("Atendido a:", atendido)
print("Cola restante:", cola_clientes)

pila = []

pila.append("accion1")
pila.append("accion2")
pila.append("accion3")

print("pila",pila)

ultimo = pila.pop()   # sin numero saca al ultimo
print("Deshaciendo:", ultimo)
print("pila restante:", pila)