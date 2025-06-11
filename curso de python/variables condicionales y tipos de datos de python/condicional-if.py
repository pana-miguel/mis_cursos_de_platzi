x = 10
y = 20

if x > 5:
    print("x es mayor que 5") #esto es parte del bloque if
elif x == 10:
    print("x es igual a 10") #si hay una similitud antes de esta linea de codigo se ejecutara la que esta antes porque es la primera que cumple la condicion
else:
    print("x es menor que 10")

print("estoy afuera del if") #esto porque no es parte del bloque if

if x > 5 and y > 15: #esto es un operador logico que une dos condiciones
    print("x es mayor que 5 y y es mayor que 15")

    