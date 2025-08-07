numeros = []
for elements in range(1, 11):
    numeros.append(elements * 2)

print(numeros)

numeros2 = [elemento * 2 for elemento in range(1, 11)]
print(numeros2)


numeros3 = []
for i in range(1, 11):
    if i % 2 == 0:
        numeros3.append(i * 2)

print(numeros3)


numeros4 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numeros4)