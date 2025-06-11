numeros = 100

iterador = iter(range(1, numeros +1, 2))
print("Los números impares son:")

for i in iterador:
    print(i)

numeros2 = 100

iterador2 = iter(range(2, numeros2 +1, 2))
print("Los números pares son:")

for i in iterador2:
    print(i)


# Crear un iterador para los números pares con una funcion

def numeros(n):             ## Definimos la función como un generador en este caso
    for i in range(2, n + 1, 2): # Definimos la variable i como el rango de 2 a n + 1 con un paso de 2
        yield i                  # Devolvemos el valor de i porque el rango es de 2 a n con un paso de 2 ya que yield es un generador de números pares que guarda el estado de la función y devuelve el siguiente valor cada vez que se llama a la función
print("Los números pares son:")
for a in numeros(100):           # Llamamos a la función numeros con el valor 100
    print(a)                     # Imprimimos el valor de a este imprimiraq los números pares


numeros = 100 # Definimos la variable numeros como 100 
print("Los números pares son:")
for i in range(2, numeros +1, 2): # Definimos la variable i como el rango de 2 a numeros + 1 con un paso de 2
    print(i)                      # Imprimimos el valor de i este imprimiraq los números pares porque el rango es de 2 a 100 con un paso de 2