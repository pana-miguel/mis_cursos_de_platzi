class Barco:
    def __init__(self, nombre, tamanio):
        self.nombre = nombre
        self.tamanio = tamanio
        self.posiciones = []

    def guardar_posicion(self, fila, columna):
        posicion = (fila, columna)
        self.posiciones.append(posicion)  # Se guarda de forma persistente en el objeto

    def ejemplo_temporal(self):
        posiciones = []
        posiciones.append((0, 0))  # Solo existe dentro del método
        print("Dentro del método:", posiciones)

barco = Barco("Submarino", 3)
barco.guardar_posicion(1, 2)
print(barco.posiciones)  # => [(1, 2)]
barco.ejemplo_temporal()  # => [(0, 0)] pero no afecta self.posiciones
print(barco.posiciones)  # => [(1, 2)] no cambió


#pero si reemplazamos posiciones por self.posiciones y habra cambio
#ya que ejemplo temporal cambiaria los parametros de self.posiciones
