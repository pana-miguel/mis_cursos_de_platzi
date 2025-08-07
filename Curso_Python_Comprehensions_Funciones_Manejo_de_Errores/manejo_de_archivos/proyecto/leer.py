import csv
def leer(ruta):
    with open(ruta, 'r', encoding='utf-8-sig') as fila:
        leer = csv.reader(fila, delimiter=',')
        cabeza = next(leer)
        data2 = []
        for fila in leer:
            iterar = zip(cabeza, fila)
            tiendad_diccionario = {llave: valor for llave, valor in iterar}  
            data2.append(tiendad_diccionario)
        return data2
    

if __name__ == '__main__':
    data2 = leer('./proyecto/data2.csv')
    print(data2[0].keys()) 