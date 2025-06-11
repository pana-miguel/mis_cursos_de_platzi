#fibonacci
# Fibonacci es una secuencia de números en la que cada número es la suma de los dos anteriores.
# La secuencia comienza con 0 y 1, y los siguientes números son 1, 2, 3, 5, 8, 13, etc.

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)
