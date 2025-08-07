import csv 

def leer(path):
    with open(path, 'r', encoding='utf-8-sig') as fila:#el endoding es para evitar el error de codificacion porque la primera llave sale 
                                                    #con el nombre de \ufeffsport y con el encoding se elimina ese error y deja solo sport
        leer_csv = csv.reader(fila, delimiter=',')
        cabeza = next(leer_csv)
        data1 = []
        for fila in leer_csv:
            iterar = zip(cabeza, fila)
            deportes_diccionario = {llave: valor for llave, valor in iterar}
            data1.append(deportes_diccionario)
        return data1
    

if __name__ == '__main__':
    data1 = leer('./prueba1/data1.csv')
    print(data1[0].keys())  # Muestra todas las llaves reales
