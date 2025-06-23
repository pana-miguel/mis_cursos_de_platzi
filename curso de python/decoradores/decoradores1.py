#decorador
def transaccion(funcion):
    def envolver():
        print("1 log de la transaccion...")
        funcion()
        print("3 log terminado...")
    return envolver

@transaccion #este es un decorador, se aplica a la funcion pago para modificar su comportamiento


def pago():
    print("2 prosesando pago...")

pago()
