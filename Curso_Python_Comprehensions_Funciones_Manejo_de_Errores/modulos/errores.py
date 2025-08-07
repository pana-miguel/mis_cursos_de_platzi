#print(0 / 0) #cero division error

#print(result) #name error

# print(10 + '10') #type error

#suma = lambda x, y: x + y
#assert suma(2, 2) == 3 #assert error 

edad = 10
if edad < 18:
    raise Exception('No puedes pasar, eres menor de edad')