class Order:
    # Método estático que calcula un impuesto según un monto y un porcentaje
    @staticmethod
    def calcular_impuesto(monto, porcentaje):
        return monto * (porcentaje / 100)

# Se llama al método sin necesidad de crear una instancia de la clase
print(Order.calcular_impuesto(1000, 18))  # Salida: 180.0
