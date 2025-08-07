precio1 = 100 #alcance global dentro del archivo

def precios():
    precio2 = 100
    resultado = precio2 + 10
    print(resultado) #se puede usar la variable global en una funcionporque es una variable global 
    return resultado

precios()
print(precio1)