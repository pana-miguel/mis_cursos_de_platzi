import csv

nuevo_producto = {
    'name': 'cargador inalambrico',
    'price': '76',
    'quantity': 100,
    'brand': 'colgate',
    'category': 'Accessories',
    'entry_date': '2024-12-10'
}

with open('products_updated.csv', mode='a', newline='') as file: # abrimos el archivo en modo append para agregar informacion al final del archivo
    #file.write('\n')  #esta linea es por si acaso no se realiza el salto de linea en la informacion que agregamos en el archivo
    csv_escritura = csv.DictWriter(file, fieldnames = nuevo_producto.keys())
    csv_escritura.writerow(nuevo_producto)