todo = ["Dirigirnos al hotel", "Almorzar", "Visitar un museo", "Volver al hotel"]
print(todo)
numbers = [1,2,3,4,"cinco",6,7,8,9,10]
print(type(numbers))
mix = ["uno", 1, 3.13, True]
print(type(mix))
print(mix)

print("primer elemento",mix[0])
print("segundo elemento",mix[1])
print("tercer elemento",mix[2])
print("ultimo elemento",mix[-1])
print(mix[0:2])

print(mix)
mix.append(False)
print(mix)
mix.append(["uno", 1, 3.13, True])
print(mix)

mix.insert(1,["a", "b", "c"])
print(mix)

print(mix.index(["a", "b", "c"]))

numbers = [1,2,3,80000,5,6,7,8,9,10]
print("mayor", max(numbers))
print("menor", min(numbers))

del numbers [0]
print(numbers)

del numbers #esto elimina la variable numbers
#print(numbers) #esto da error porque ya no existe la variable numbers