def suma_numeros(*args): #se almacenan en una variable una cantidad indefinida de informacion
    return sum(args)   #se van a sumar numeros
 
print(suma_numeros(1, 2, 3, 4, 5))      #se suma hasta donde esta la informacion en la funcion
print(suma_numeros(1, 2))                
print(suma_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))