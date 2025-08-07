def multiply_numbers(numbers):
    # Escribe tu solución 👇
    resultado = list(map(lambda x: x * 2, numbers))
    return resultado

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)
