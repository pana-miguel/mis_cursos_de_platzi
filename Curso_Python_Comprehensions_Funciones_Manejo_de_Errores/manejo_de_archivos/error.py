try: #esto es para registrar el error o posible error
    print(0 / 0)
except ZeroDivisionError as error: #ver que error es el que se lanza 
    print(error)

print('hola') #continua con la ejecucion aunque haya el error de atras

try:
    assert 1 != 1, 'uno no es igual a uno'
except AssertionError as error2:
    print(error2)

#de esta forma solo lanza el primer error y no el segundo
try:
    print(0 / 0)
    assert 1 != 1, 'uno no es igual a uno'
except ZeroDivisionError as error: 
    print(error)
except AssertionError as error2:
    print(error2)

print('hola')


def my_divide(a, b):
   try:
      result = a / b
   except ZeroDivisionError:
      result = "No se puede dividir por 0"
   return result
    
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0
