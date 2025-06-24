#calculo de factorial de un numero con recursion
def factorial(n): # Recursividad para calcular el factorial de un número
    if n == 0: # Caso base: el factorial de 0 es 1
        return 1 
    else:     
        return n * factorial(n - 1) # Llamada recursiva para calcular el factorial de n-1
    
factorial_5 = print(factorial(5)) 

#serie de fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1 
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2) # Llamada recursiva para calcular el n-ésimo número de Fibonacci
    
numero = print(fibonacci(7)) # Imprime el décimo número de la serie de Fibonacci


