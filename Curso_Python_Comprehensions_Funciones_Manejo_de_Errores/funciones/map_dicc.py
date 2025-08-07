items = [
    {
        'producto': 'camisa',
        'precio': 1000
    },
    {
        'producto': 'pantalon',
        'precio': 2000
    },
    {
        'producto': 'zapatos',
        'precio': 3000
    },
    {
        'producto': 'bufanda',
        'precio': 4000
    },
    {
        'producto': 'abrigo',
        'precio': 5000
    }
]

precios = list(map(lambda item: item['precio'], items))
print(precios)
print('___________________________')

def agregar_impuesto(item: float)-> float:
    item['impuesto'] = item['precio'] * 0.15
    return item

modificacion = list(map(agregar_impuesto, items)) #utilizo la lista items para agregar una nueva columna de impuesots
print(modificacion)


def precio_final(item):
    item['precio final'] = item['precio'] + item['impuesto']
    return item

precio_final = list(map(precio_final, modificacion))#utilizo la lista modificada ya que esta tiene la nueva columna de impuestos para agregarle el precio final
print('___________________________')
print(precio_final)
print('___________________________')
print(items)