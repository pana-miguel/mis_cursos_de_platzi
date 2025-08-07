#en este map lo que aremos es que si creamos otra lista no tenga el mismo codigo de referencia en memoria que la original 

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


def agregar_impuesto(item: float)-> float:
    nuevo_item = item.copy()
    item['impuesto'] = item['precio'] * 0.15
    return nuevo_item

modificacion = list(map(agregar_impuesto, items)) #utilizo la lista items para agregar una nueva columna de impuesots
print(modificacion)
print('___________________________')
print(items)