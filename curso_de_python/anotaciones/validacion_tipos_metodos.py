def dividir(a: int, b: int) -> float:
    #validar que ambos parametros sean enteros 
    if  not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambos parametros deben ser enteros") #esto apra que en la terminal se vea mejor
        """print('Error: ambos parametros deben ser enteros o flotantes')    
        return None"""
        


    #verificar que no sea igual a 0
    if b==0:
        raise ValueError('El divisor no puede ser cero')
        """print('Erro: el segundo numero no puede ser cero')
        return None"""
    
    return a/b

#result1 = dividir(5, "3")
#result2 = dividir(10, 0)
#result3 = dividir(10, 2)
#print(result3)

#ejemplo de uso esto para que no salga como tal todo el error sino solo el imprimido qu queremos 
try: 
    result = dividir(10, "2") #error de tipo type error
    print(result)
except TypeError as i:
    print(f'Error: {i}')

try: 
    result = dividir(10, 0) #error de tipo type error
    print(result)
except ValueError as i:
    print(f'Error: {i}')