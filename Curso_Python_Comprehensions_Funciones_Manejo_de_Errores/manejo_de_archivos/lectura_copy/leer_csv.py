import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./lectura/data.csv')
  print(data[0]) #esto es solo para ver como se veria el diccionariio en el primer dato para no mostrar todos los datos porque son muchos 
  #al final todos los datos tendran este mismo patron 

  
