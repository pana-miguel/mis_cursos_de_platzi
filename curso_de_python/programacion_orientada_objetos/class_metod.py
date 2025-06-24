class Order:
    global_descuento = 10

    def __init__(self, monto):
        self.monto = monto
    
    @classmethod #esta es una clase de metodo que sirve para acceder a atributos de clase fuera de la instancia
    def actualizar_global_descuento(cls, nuevo_valor_descuento):
        cls.global_descuento = nuevo_valor_descuento

Order.actualizar_global_descuento(20)
print(Order.global_descuento)