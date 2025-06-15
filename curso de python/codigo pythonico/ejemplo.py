"""numeros = [1, 2, 3, 4, 5]

numero_cuadrado = []

for numero in numeros:
    cuadrado = numero ** 2
    numero_cuadrado.append(cuadrado)

print(numero_cuadrado)"""

#este es un mejor codigo que el de arriba porque usamos list compresion
#osea que en una misma linea podemos ahorrarnos varias
numeros = [1, 2, 3, 4, 5]
numero_cuadrado = [x**2 for x in numeros]

print(numero_cuadrado)