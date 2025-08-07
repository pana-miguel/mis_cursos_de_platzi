file = open('texto.txt', 'r')

#print(file.read()) #leer el texto y se lee todo el contenido en una sola vez 

#print(file.readline()) #leer el texto por lineas para que los archivos pesados se puedan leer mejor 
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())

for line in file:
    print(line) #imprimir el contenido de cada linea del documento sin nesecidad de saber cuantos hay 

file.close() #cerrar el archivo para liberar memoria 

#de esta forma abre y cierra el archivo solo leyendo de maner correcta el archivo
with open('texto.txt', 'r') as file:
    for line in file:
        print(line) 