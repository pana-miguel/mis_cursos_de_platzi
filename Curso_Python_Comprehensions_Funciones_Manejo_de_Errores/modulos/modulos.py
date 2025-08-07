import sys
print(sys.path)

import re 
texto = 'mi numero de telefono es 31129889384 y el codigo del pais es 57 mi numero de la suerte es el 3'
resultado = re.findall('[0-9]+', texto)
print(resultado)

import time 
tiempo = time.time()
hora_local = time.localtime()
resultado = time.asctime(hora_local)
print(resultado)
print(tiempo)

import collections
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 3, 3, 2, 1, 5, 5]
counter = collections.Counter(numeros)
print(counter)
