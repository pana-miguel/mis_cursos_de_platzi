#este codigo es un ejemplo de iteraciones for y while en python

numbers = [1, 2, 3, 4, 5]

for i in numbers:
    print("i es igual a ", i)


for i in range(10):
    print(i)

print("otra forma de hacerlo")
for i in range(3,10):
    print(i)

frutas = ["manzana", "pera", "tomate", "uva"]
for fruta in frutas:
    print(fruta)
    if fruta == "pera":
        print("pera encontrada")

x = 0
while x < 5:
    if x == 3: # cuando x es igual a 3, se sale del bucle
        break # se sale del bucle cuando aga 3 bucles
    print(x) 
    x += 1
print("fin del bucle while")