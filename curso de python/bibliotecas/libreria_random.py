import random

#generar un numero entero aleatorio

random_numero = random.randint(1, 20) #me da un numero ramdon entre el 1 y el 20 que siempre seran numeros enteros
print(random_numero)

#elegir colores aleatorios

colores = ['rojo', 'azul', 'verde']
color_random = random.choice(colores) #busca en la lista los datos y los pone de manera ramdom
print(color_random)

#barajar una lista de cartas
cartas = ['As','rey','reina','jota','10'] #reordenara este mano de cartas de la manera que quiera 
random.shuffle(cartas)
print(cartas)