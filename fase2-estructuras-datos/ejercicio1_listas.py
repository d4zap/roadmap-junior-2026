

clientes = ["David","ana","luis"]

print(clientes)       # ver toda la lista
print(clientes[0])    # primer elemento
print(len(clientes))  # cuantos hay 


#anade cliente
clientes.append("Pedro")
print(clientes)

#elimina cliente
clientes.remove("ana")
print(clientes)

# mira si hay alguen en la lista
print("David" in clientes)
print("ana"in clientes) 