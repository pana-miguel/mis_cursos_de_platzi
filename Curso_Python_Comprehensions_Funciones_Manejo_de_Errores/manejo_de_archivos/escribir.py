"""with open('texto.txt', 'r+') as file: #con r+ tenemos permiso de lectura y escritura 
    for line in file:
        print(line) 
    file.write('nuevas cosas en este archivo\n')
    file.write('nuevas cosas en este archivo\n')
    file.write('nuevas cosas en este archivo\n')
"""

with open('texto.txt', 'w+') as file: #con r+ tenemos permiso de lectura y escritura pero sobreescribe las lineas del archivo 
    for line in file:
        print(line) 
    file.write('nuevas cosas en este archivo\n')
    file.write('nuevas cosas en este archivo\n')
    file.write('nuevas cosas en este archivo\n')