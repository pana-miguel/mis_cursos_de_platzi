import os

#Obtener el directorio actual
"""cwd = os.getcwd()             #crea un directorio y el os.getcwd es para saber en que variable esta
print("Directorio de trabajo actual", cwd) #esto es para la ruta como tal de donde esta este archivo
"""
#Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')] #llamar otra vez todo lo que este en este directorio por el punto que se pone
print("Archivos txt: ", txt_files) #y solo seran los archivos .txt

#Renombrar archivo
os.rename('caperusita.txt', 'cuento.txt') #renombra el archivo en este caso caperusita pasa a llamarse cuento
print('Archivo renombrado')

#Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')] #otra vez mostramos los archivos que tenemos con .txt
print("Archivos txt: ", txt_files)