#leer un archivo linea por linea

"""with open('caperusita.txt', 'r') as file: # en esta linea la r significa leer el archivo en este caso el de caperita.txt
                                          #esta vez como lo tenemos en la misma carpeta lo colocamos asi pero si esta en otra debemos
                                          #definir la ruta, (as file) es para definir las lineas
    for lineas in file:                   #aqui hacemos un ciclo for con todas las lineas que tiene el texto
        print(lineas.strip()) """            #imprimimos el archivo con el script para que quite los saltos de linea

#leer todas las lineas en una lista

"""with open('caperusita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)"""

#añadir texto
"""with open('caperusita.txt', 'a') as file:  #utilizamos a que es append que añade al final lo que queramos poner 
    file.write("\n\nBy:chatgpt")   #modifica el text con lo que le queramos poner"""

#sobreescribir el texto
"""with open('caperusita.txt', 'w') as file: #en w es el modo para sobreescribir 
     file.write("\n\nBy:chatgpt") #solo se vera esto y no todo el texto ya que se sobreescribe"""

with open('caperusita.txt', 'r') as f:
    lineas = f.readlines()
    cantidad = len(lineas)
    print("Número de líneas:", cantidad)