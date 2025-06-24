class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio

    @property #sirve para definir un atributo de instancia que se comporta como un atributo de clase 
    def precio(self):
        return self._precio
    
    @precio.setter #sirve para definir un metodo que se ejecuta cuando se asigna un valor al atributo
    def precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError('el precio del producto no puede ser menor que 0')
        self._precio = nuevo_precio

    @precio.deleter #sirve para definir un metodo que se ejecuta cuando se elimina el atributo
    def precio(self):
        print(f"el producto {self.nombre} con precio de {self.precio} ha sido eliminado")
        del self.nombre
        del self._precio

#creamos instancia del producto
producto = Producto("chocorramo", 2500)
print(producto.nombre)
print(producto.precio)

#modificamos el precio del producto
producto.precio = 3000
print(producto.nombre)
print(producto.precio)

#eliminamos el producto 
del producto.precio
