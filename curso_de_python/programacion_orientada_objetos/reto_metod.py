class Pedido:
    # Atributo de clase que define un descuento global inicial
    global_discount = 10

    # Método estático que solo verifica el monto del pedido y decide si aplicar el descuento
    @staticmethod
    def verificar_monto(monto_pedido: float, global_discount: float):
        if monto_pedido >= 100.00:
            print(f"Se aplica el descuento del {global_discount}%")
        else:
            print(f"No se aplica descuento")

    # Método de clase que tiene acceso a la clase a través de 'cls'
    @classmethod
    def realizar_pedido(cls, monto_pedido: float):
        # Si el pedido supera los 1000, se aumenta el descuento global a 20%
        if monto_pedido > 1000:
            cls.global_discount = 20

        # Se llama al método estático para verificar si aplica descuento
        cls.verificar_monto(monto_pedido, cls.global_discount)

        # Si el monto es menor de 100, se retorna el monto sin descuento
        if monto_pedido < 100:
            return monto_pedido
        else:
            # Si es 100 o más, se aplica el descuento global y se retorna el monto con descuento
            return monto_pedido - (monto_pedido * (cls.global_discount / 100))


# Prueba con diferentes montos de pedido
print(Pedido.realizar_pedido(90))     # No aplica descuento
print(Pedido.realizar_pedido(150))    # Aplica 10% de descuento
print(Pedido.realizar_pedido(2140))   # Aplica 20% de descuento y cambia el descuento global
