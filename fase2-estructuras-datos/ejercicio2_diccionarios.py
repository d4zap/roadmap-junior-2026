
cliente = {
    "nombre": "David",
    "cedula": 123456,
    "telefono": "3001234567",
    "servicio": "SOAT",
    "matricula": "ABC123",
    "estado": "pendiente",
    "valor": 0

}
print(cliente["nombre"])

print(cliente["servicio"])

cliente["estado"] = "procesado"

cliente["valor"] = 150000


print(cliente)


clientes = [
    {"nombre": "David", "servicio": "SOAT", "estado": "pendiente"},
    {"nombre": "Ana", "servicio": "Tecnomecánica", "estado": "pendiente"},
    {"nombre": "Luis", "servicio": "SOAT", "estado": "procesado"}
]

print(clientes[1]["nombre"])


clientes = [
    {"nombre": "David", "servicio": "SOAT", "estado": "pendiente"},
    {"nombre": "Ana", "servicio": "Tecnomecanica", "estado": "pendiente"},
    {"nombre": "Luis", "servicio": "SOAT", "estado": "procesado"}
]

for cliente in clientes:
    print(cliente["nombre"], "-", cliente["servicio"])