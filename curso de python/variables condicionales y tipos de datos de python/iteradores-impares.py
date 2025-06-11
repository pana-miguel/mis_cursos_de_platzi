# Crear un iterador para los numeros impares

#Limite
limit = 10

#Crear iterador
odd_itter = iter(range(1,limit+1,2)) # range(1,10+1,2) genera los números impares desde 1 hasta 10 el 1 es el primer número impar y el 10 es 
#el último número impar, el 2 es el paso que se va a dar para obtener los números impares. el limit+1 es para que el 10 se incluya en el rango,
#ya que el rango no incluye el último número. y el nnumero 2 es el paso que se va a dar para obtener los números impares.

#Usar el iterador
for num in odd_itter:
    print(num)