

placas_registradas = {"ABC123", "XYZ789", "DEF456"}

# Verificar si una placa ya existe
placa_nueva = "GHI999"
if placa_nueva in placas_registradas:
    print("Esta placa ya tiene un registro activo")
else:
    placas_registradas.add(placa_nueva)
    print("Placa registrada exitosamente")