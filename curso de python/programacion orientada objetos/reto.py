class CuentaBancaria:
    def __init__(self, nombre, saldo):    
        self.nombre = nombre
        self.saldo = saldo

    def _actualizar_saldo(self, monto, transaccion):
        self.transaccion = transaccion
        self.saldo += monto 
        print(f'Se añadieron {monto} pesos. Tu saldo ahora es de {self.saldo}')
        self.__registro_transaccion(transaccion)

    def __registro_transaccion(self, registro):
        if registro == self.transaccion:
            print('Se ha registrado la transacción')
        else:
            print('No se ha registrado la transacción')


# Crear una cuenta
cuenta = CuentaBancaria(nombre='Miguel', saldo=100000)

# Hacer una transacción con nombre
cuenta._actualizar_saldo(50000, "pagado")

