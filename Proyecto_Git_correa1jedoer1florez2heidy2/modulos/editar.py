import json
def añadido():
    sucursal_nombre = input("ingrese el nombre de la sucursal")
    direcion = input ("ingrese la direccion de la sucursal")
    telefono = input ("ingrese el telefono de la sucursal")
    gerente = input ("ingrese el nombre del gerente")
    id = input ("ingrese el id del gerente")

    sucursal = {
        "sucursal nombre " : sucursal_nombre,
        "direcion " : direcion ,
        "numero de telefono " : telefono,
        "nombre del gerente " : gerente ,
        "id" : id,
    }
    with open('guardar_informacion.json', 'w') as jf: 
        json.dump(sucursal, jf, ensure_ascii=False, indent=2)