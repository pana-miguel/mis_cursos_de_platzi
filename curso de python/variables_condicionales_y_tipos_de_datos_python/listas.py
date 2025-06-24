#este codigo esplica mix que es una lista de diferentes tipos de datos y como se pueden manipular las listas en python

todo = ["Dirigirnos al hotel", "Almorzar", "Visitar un museo", "Volver al hotel"]
print(todo)
numbers = [1,2,3,4,"cinco",6,7,8,9,10]
print(type(numbers))
mix = ["uno", 1, 3.13, True]
print(type(mix))
print(mix)

print("primer elemento",mix[0]) #primer elemento de la lista
print("segundo elemento",mix[1]) #segundo elemento de la lista
print("tercer elemento",mix[2]) #tercer elemento de la lista
print("ultimo elemento",mix[-1]) #ultimo elemento de la lista
print(mix[0:2]) #elementos de la lista desde el 0 al 2 (sin incluir el 2)

print(mix)
mix.append(False) #agrega un elemento al final de la lista
print(mix)
mix.append(["uno", 1, 3.13, True]) #agrega una lista al final de la lista
print(mix)

mix.insert(1,["a", "b", "c"]) #inserta una lista en la posicion 1 de la lista
print(mix)

print(mix.index(["a", "b", "c"])) #devuelve el indice de la lista que se le pasa como parametro

numbers = [1,2,3,80000,5,6,7,8,9,10] #crea una lista de numeros
print("mayor", max(numbers)) #devuelve el numero mayor de la lista
print("menor", min(numbers)) #devuelve el numero menor de la lista

del numbers[0] #esto elimina el primer elemento de la lista numbers
print(numbers) #esto elimina el primer elemento de la lista numbers

del numbers #esto elimina la variable numbers
#print(numbers) #esto da error porque ya no existe la variable numbers