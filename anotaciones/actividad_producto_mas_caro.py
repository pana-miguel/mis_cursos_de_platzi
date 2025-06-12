# Dada una lista de productos con sus nombres y precios, encuentra el producto más caro

productos = [
    {"nombre": "Teclado", "precio": 120},
    {"nombre": "Mouse", "precio": 80},
    {"nombre": "Monitor", "precio": 600},
    {"nombre": "Laptop", "precio": 950},
    {"nombre": "USB", "precio": 35}
]


"""def producto_mas_caro():
    producto_caro = None
    precio_caro = 0
    for producto in productos:
        if producto['precio'] > precio_caro:
            producto_caro = producto
            precio_caro = producto["precio"]
    print(f"El producto más caro es {producto_caro['nombre']} con un precio de {producto_caro['precio']}")

producto_mas_caro()"""

def producto_mas_caro():
    producto_caro = max([producto for producto in productos], key=lambda precio : precio['precio'])
    print(f"El producto más caro es {producto_caro['nombre']} con un precio de {producto_caro['precio']}")

# Llamada a la función
producto_mas_caro()





