from math import gcd # Importar gcd para simplificar fracciones

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, otra_fracicon):
        nuevo_denominador = (self.denominador * otra_fracicon.denominador)
        nuevo_numerador = (self.numerador * otra_fracicon.denominador + otra_fracicon.numerador * self.denominador)
        comun_divisor = gcd(nuevo_numerador, nuevo_denominador)
        return Fraccion(nuevo_numerador // comun_divisor, nuevo_denominador // comun_divisor)


    def __repr__(self):
        return f"{self.numerador}/{self.denominador}"

f1 = Fraccion(1, 4)
f2 = Fraccion(1, 2)

f3 = f1 + f2  # Suma de fracciones
print(f3)  # Output: 3/4
