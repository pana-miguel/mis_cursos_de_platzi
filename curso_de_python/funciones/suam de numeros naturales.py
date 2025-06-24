# Este programa calcula la suma de los números naturales desde 1 hasta n utilizando recursividad.
def factorial(n): # Recursividad para calcular el factorial de un número 
    if n == 0:
        return 0 # Caso base: el factorial de 0 es 1
    else:     
        return n + factorial(n - 1) # Llamada recursiva para calcular el factorial de n-1
    
factorial_5 = print(factorial(5)) 