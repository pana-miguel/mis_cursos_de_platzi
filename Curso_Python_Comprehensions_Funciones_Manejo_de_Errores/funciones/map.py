#con lamda s ehace mas facil el proceso de multilicar una lista o recorrerla y hacerle algun cambio 

numeros = [1, 2, 3, 4, 5]

numeros2 = list(map(lambda i: i * 2, numeros))

print(numeros)
print(numeros2)

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10, 11]

result = list(map(lambda x, y: x + y, lista1, lista2)) #esto suma los valores de las lista el primero de la lista 1 con el primero de la lista 2 y asi susesivamente 
#si las listas no son iguales los valores sobrantes no apareceran en la lista como en este caso el 11 no se suma con nada y no esta

print(result)