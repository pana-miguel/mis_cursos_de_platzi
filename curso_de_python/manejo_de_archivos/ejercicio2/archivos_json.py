import json

#lectura del archivo
with open('productos.json', mode='r') as archivo:
    productos = json.load(archivo)

#mostrar el contenido
for producto in productos:
    #print(producto)
    print(f"producto: {producto['name']}, precio: {producto['price']}") #traigo solo nombre y precio el producto del archivo json