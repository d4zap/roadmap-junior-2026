
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