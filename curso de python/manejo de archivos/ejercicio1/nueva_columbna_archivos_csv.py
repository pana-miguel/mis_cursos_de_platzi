# en este ejercicio vamos a crear una copia del archivo para hacer pruebas en la nformacion sin alterar el primer archivo que nos dieron
import csv

file_path = 'products_updated.csv' #nuestra archivo principal y a partir de este vamos a crear ua copia para hacer pruebas
nuevo_archivo_copia = 'products_updated2.0.csv' #nombre del nuevo archivo que vamos a crear
archivo_prueba_= 'products_updated3.0.csv' # #nombre del nuevo archivo que vamos a crear para hacer pruebas con una nueva columna

with open(file_path, mode='r') as archivo:         #identifica y abre el archivo que vamos a usar
    csv_leer = csv.DictReader(archivo)                          #lee el archivo para recorrerlo
    #obtener los nombres de las columnas existentes
    nombres_columnas = csv_leer.fieldnames + ['total_value'] #crea una nueva columna llamada valor total
    otra_columna = csv_leer.fieldnames + ['disponibilidad']

    with open(nuevo_archivo_copia, mode='w', newline='') as nuevo_archivo: #se maneja aqui el nuevo archivo que vamos a usar
        csv_escribir = csv.DictWriter(nuevo_archivo, fieldnames=nombres_columnas)
        csv_escribir.writeheader() #escribir iformacion del encabezado

        for filas in csv_leer:
            filas['total_value'] = float(filas['price']) * int(filas['quantity'])
            csv_escribir.writerow(filas)


#cuando ejecutemos va a salir la version 2.0 de este archivo en este caso


#ejemplo siguiendo las lineas de codigo de arriba para aladir una nueva columna 
# SEGUNDA LECTURA: crear archivo con columna 'disponibilidad'
with open(file_path, mode='r') as archivo:
    csv_leer = csv.DictReader(archivo)
    otra_columna = csv_leer.fieldnames + ['disponibilidad']

    with open(archivo_prueba_, mode='w', newline='') as nuevo_archivo_prueba:
        csv_escribir = csv.DictWriter(nuevo_archivo_prueba, fieldnames=otra_columna)
        csv_escribir.writeheader()


    with open(archivo_prueba_, mode='w', newline='') as nuevo_archivo_prueba: #se maneja aqui el nuevo archivo que vamos a usar
        csv_escribir = csv.DictWriter(nuevo_archivo_prueba, fieldnames=otra_columna)
        csv_escribir.writeheader() #escribir iformacion del encabezado

        for filas in csv_leer:
            if int(filas['quantity']) > 20:
                filas['disponibilidad'] = 'disponible'
            else:
                filas['disponibilidad'] = 'no disponible'
            csv_escribir.writerow(filas)
       