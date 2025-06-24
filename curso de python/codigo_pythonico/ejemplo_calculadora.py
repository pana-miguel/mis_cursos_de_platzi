

class Calculadora:
    def add_numeros(self, primer_numero, segundo_numero):
        resultado = primer_numero + segundo_numero
        return resultado

calc = Calculadora()

print(calc.add_numeros(5,3))