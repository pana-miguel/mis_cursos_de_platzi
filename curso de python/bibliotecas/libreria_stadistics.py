import statistics
import csv


# Leer los datos de ventas mensuales desde un archivo CSV
ventas_mensuales = {}
with open('ventas_mensuales.csv', mode='r') as archivo:
    leer = csv.DictReader(archivo)
    for fila in leer:
        mes = fila['mes']
        ventas = int(fila['ventas'])
        ventas_mensuales[mes] = ventas

ventas = list(ventas_mensuales.values())
#print(sales)

#Hallar la media
media_ventas = statistics.mean(ventas)
print(f"La media es: {media_ventas}")

#Hallar la mediana
media_ventas = statistics.median(ventas)
print(f"La mediana es: {media_ventas}")

#Hallar la moda
moda_ventas = statistics.mode(ventas)
print(f"La moda es: {moda_ventas}")

#Desviación Estándar
stdev_sales = statistics.stdev(ventas)
print(f"La desviación estándar es: {stdev_sales}")

#Hallar la varianza
varianza_ventas = statistics.variance(ventas)
print(f"La moda es: {varianza_ventas}")

maximas_ventas = max(ventas)
minimas_ventas = min(ventas)

rango_ventas = maximas_ventas - minimas_ventas
print(f'Rango de ventas: {rango_ventas}')