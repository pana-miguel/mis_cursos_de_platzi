# Matrices y tuplas en Python explicacion de la ubicación de los elementos en una matriz y tuplas

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matriz)

print(matriz[0]) # Imprime la primera fila de la matriz

print(matriz[0][0]) # Imprime el primer elemento de la primera fila

number = (1, 2, 3, 4, 5) # Tupla de números, las tuplas son inmutables
print(number)
print(type(number)) # Imprime el tipo de dato de la variable number, que es una tupla
print(number[0]) # Imprime el primer elemento de la tupla

#number[0] = 10 #esto da error porque las tuplas son inmutables