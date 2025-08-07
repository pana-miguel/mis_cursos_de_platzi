def suma_rango(min, max):
    print(f'el minimo es {min} y el max es {max}')
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

reusltado = suma_rango(1, 20)
print(reusltado)
resultado2 = suma_rango(20, 30)
print(resultado2)
resultado3 = suma_rango(23, 10) #como tal siempre dara 0 porque el miimo o el primer numero no puede superar al segundo 
print(resultado3)
