"""def my_print(texto):
    print(texto)

my_print('este es mi texto relacionado con la variable texto') #se ejecuta con los parentesis 
my_print('hola')

a = 10
b = 5

c = a + b

def suma(a, b):
    print(a + b)
    print(f'se sumo {a} mas {b} y esto da {a+b}')

suma(1, 5)
suma(10, 4)"""

#utilizart una funcion dentro de otra
def my_print(texto):
    print(texto * 2) #multiplica el texto dos veces o si es un numero si no (si es un texto) coloca dos veces el texto




def suma(a, b):
    my_print(a + b) #utilizamos la funcion de arriba para que los numeros tambien se multipliquen 


my_print('hola')
suma(1, 5)
suma(10, 4)