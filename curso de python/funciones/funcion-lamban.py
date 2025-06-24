multiplicaicon = lambda a, b : a * b # Multiplicación utilizando lambda para que sea más corto
print(multiplicaicon(2, 3))

#cuadrado de cada numero de una lista
numero = range(11) #range(11) genera una lista de 0 a 10
numeros_cuadrados = list(map(lambda x: x**2, numero)) #map aplica la funcion lambda a cada elemento de la lista
print(numeros_cuadrados) #imprime la lista de cuadrados


#pares 
numero_eventos = list(filter(lambda x: x % 2 == 0, numero)) #filter aplica la funcion lambda a cada elemento de la lista y devuelve los que cumplen la condicion
print(numero_eventos) #imprime la lista de numeros pares
