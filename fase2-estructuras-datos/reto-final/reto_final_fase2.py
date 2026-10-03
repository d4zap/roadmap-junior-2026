

clientes = [
    {"cedula": "11112" , "nombre": "David", "telefono": "3165424", "servicio": "SOAT", "placa": "ABC123", "estado": "pendiente", "valor": 0},
    {"cedula": "11113" , "nombre": "Mari", "telefono": "3154254", "servicio": "Tecnomecanica", "placa": "XYZ789", "estado": "pendiente", "valor": 0},
    {"cedula": "11114" , "nombre": "Ana", "telefono": "315452", "servicio": "SOAT", "placa": "DEF456", "estado": "procesado", "valor": 1500000},
    {"cedula": "11115" , "nombre": "Luis", "telefono": "314685", "servicio": "SOAT", "placa": "DES193", "estado": "procesado", "valor": 1500000}
    ]

placas = set()

for cliente in clientes:
    placas.add(cliente["placa"])


placa_nueva = "GHI999"
if placa_nueva in placas:
    print("Esta placa ya tiene un registro activo")
else:
    placas.add(placa_nueva)
    print("Placa registrada exitosamente")

cola_clientes= []

# llega el cliente

cola_clientes.append("David") #primero en llegar
cola_clientes.append("Ana")   #segundo
cola_clientes.append("Luis")  # tercero

print("Cola actual:", cola_clientes)

#Atender al primero (FIFO)

atendido= cola_clientes.pop(0) #saca al primero

print("Atendido a:", atendido)
print("Cola restante:", cola_clientes)


print(clientes[1]["nombre"])

for cliente in clientes:
    print(cliente["nombre"], "-", cliente["servicio"])

print()
print()
print()
print()

for cliente in clientes:

    if cliente["servicio"] == "SOAT" and cliente["estado"] == "pendiente":
      print(cliente)   

def buscar_cliente(cedula_buscada):
    for cliente in clientes:
        if cliente["cedula"] == cedula_buscada:
            return cliente
    return None

resultado = buscar_cliente("99999")  


if resultado is None:
    print("La cédula 99999 no está registrada en el sistema")
else:
    print("Cliente encontrado:", resultado["nombre"], "-",resultado["servicio"])        


                    
       
print(buscar_cliente("11115"))
print(buscar_cliente("11114"))
print(buscar_cliente("99999"))


