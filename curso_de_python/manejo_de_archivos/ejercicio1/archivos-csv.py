#este es un ejercicio importando la libreria de csv esto para menejar archivos de exel
#en este caso tenemos que toda la informacion del archivo esta en una sola columna separando sus datos por comas 
#a continuacion se haraun ejemplo para imprimir estos datos por consola y haciendo que el id de cada producto sea su nombre 
import csv

#leer archivo
"""with open('products_updated.csv', mode='r') as file:  
    # open = abrir archivo  
    # 'products_updated.csv' = el archivo que queremos abrir  
    # mode='r' = modo de lectura del archivo  
    # as file = almacenar en la variable file

    csv_reader = csv.DictReader(file)  
    # csv_reader = creamos una variable para guardar el lector CSV  
    # csv. = usamos el módulo csv  
    # DictReader(file) = lee el archivo como diccionarios, usando los encabezados como claves

    for row in csv_reader:  
    # for = bucle para recorrer cada fila  
    # row = variable que representa una fila (como diccionario)  
    # in csv_reader = vamos a recorrer todas las filas del lector

        print(row)  
        # print = mostrar en pantalla  
        # (row) = muestra el diccionario con los datos de cada fila"""

#mostrar la iformacion por columnas 
with open('products_updated.csv', mode='r') as file:
    csv_reader = csv.DictReader(file) 
    for row in csv_reader: 
        print(f"el producto {row['name']}, precio {row['price']}")