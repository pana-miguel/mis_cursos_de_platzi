import json

archivo_abrir = 'productos.json' #archivo que contiene la lista de productos 

nuevo_archivo = {
        "name": "Mouse",
        "price": 45,
        "quantity": 120,
        "brand": "TechGear",
        "category": "Accessories",
        "entry_date": "2024-02-10"
    }

with open(archivo_abrir, mode='r') as archivo:
    productos = json.load(archivo)

productos.append(nuevo_archivo)

with open(archivo_abrir, mode='w') as archivo:
    json.dump(productos, archivo, indent=4)

#todas las veces que ejecute eso se volvera a poner un nuevo archivo