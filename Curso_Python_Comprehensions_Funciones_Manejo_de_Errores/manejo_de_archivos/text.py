import csv

def read_csv(path):
    total = 0
    with open(path, 'r', encoding='utf-8') as file:
        lector = csv.reader(file, delimiter=',')
        for fila in lector:
            total += int(fila[1])  # Asumiendo que la segunda columna contiene números
    return total

response = read_csv('./data.csv')
print(response)

