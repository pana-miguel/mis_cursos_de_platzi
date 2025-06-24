# Clase base que representa un Vehiculo generico
class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca                          # Marca del vehiculo
        self.modelo = modelo                        # Modelo del vehiculo
        self.precio = precio                        # Precio del vehiculo
        self.esta_disponible = True                 # Estado de disponibilidad

    def vender(self):
        if self.esta_disponible:
            self.esta_disponible = False
            print(f"el vehiculo {self.marca} {self.modelo} ha sido vendido.")
        else:
            print("el vehiculo ya ha sido vendido.")

    def estado(self):
        return self.esta_disponible                 # Retorna el estado de disponibilidad

    def get_precio(self):                           #esto es abstraccion porque no se puede acceder a la variable precio directamente
        return self.precio                          # Devuelve el precio del vehiculo

    def iniciar_vehiculo(self):
        raise NotImplementedError("Este metodo debe ser implementado por las subclases.")

    def detener_vehiculo(self):
        raise NotImplementedError("Este metodo debe ser implementado por las subclases.")

# Subclase Automovil
class Automovil(Vehiculo):
    def iniciar_vehiculo(self):
        if not self.esta_disponible:
            print(f"el motor del automovil {self.marca} esta en marcha")
        else:
            print(f"el automovil {self.marca} no esta disponible.")

    def detener_vehiculo(self):
        if not self.esta_disponible:
            print(f"el motor del automovil {self.marca} se ha detenido.")
        else:
            print(f"el automovil {self.marca} no esta disponible.")

# Subclase Bicicleta
class Bicicleta(Vehiculo):
    def iniciar_vehiculo(self):
        if not self.esta_disponible:
            print(f"la bicicleta {self.marca} esta en marcha")
        else:
            print(f"la bicicleta {self.marca} no esta disponible.")

    def detener_vehiculo(self):
        if not self.esta_disponible:
            print(f"la bicicleta {self.marca} se ha detenido.")
        else:
            print(f"la bicicleta {self.marca} no esta disponible.")

# Subclase Camion
class Camion(Vehiculo):
    def iniciar_vehiculo(self):
        if not self.esta_disponible:
            print(f"el motor del camion {self.marca} esta en marcha")
        else:
            print(f"el camion {self.marca} no esta disponible.")

    def detener_vehiculo(self):
        if not self.esta_disponible:
            print(f"el motor del camion {self.marca} se ha detenido.")
        else:
            print(f"el camion {self.marca} no esta disponible.")

# Clase que representa a un Comprador
class Comprador:
    def __init__(self, nombre):
        self.nombre = nombre                        # Nombre del comprador
        self.vehiculos_comprados = []               # Lista de vehiculos que ha comprado

    def comprar_vehiculo(self, vehiculo: Vehiculo):
        if vehiculo.esta_disponible:
            vehiculo.vender()
            self.vehiculos_comprados.append(vehiculo)
        else:
            print(f"el vehiculo {vehiculo.marca} no esta disponible.")

    def disponibilidad_vehiculo(self, vehiculo: Vehiculo):
        disponibilidad = "esta disponible" if vehiculo.esta_disponible else "no esta disponible"
        print(f"el vehiculo {vehiculo.marca} {disponibilidad} y cuesta {vehiculo.get_precio()}.")

# Clase que representa el Inventario de vehiculos y compradores
class Inventario:
    def __init__(self):
        self.inventario = []                        # Lista de vehiculos
        self.compradores = []                       # Lista de compradores

    def add_vehiculo(self, vehiculo: Vehiculo):
        self.inventario.append(vehiculo)
        print(f"el vehiculo {vehiculo.marca} ha sido anadido al inventario.")

    def add_comprador(self, comprador: Comprador):
        self.compradores.append(comprador)
        print(f"el comprador {comprador.nombre} ha sido anadido.")

    def mostrar_vehiculos_disponibles(self):
        print("Los vehiculos disponibles son:")
        for vehiculo in self.inventario:
            if vehiculo.esta_disponible:
                print(f"- {vehiculo.marca} {vehiculo.modelo}, precio: {vehiculo.get_precio()}")

# ---------------- PRUEBA DEL CODIGO ----------------

# Crear instancias de vehiculos
carro1 = Automovil("Toyota", "Corolla", 20000)
bicicleta1 = Bicicleta("BMX", "Rojo", 500)
camion1 = Camion("Ford", "F150", 30000)

# Crear un comprador
comprador1 = Comprador("Juan")

# Crear el inventario
inventario = Inventario()

# Anadir vehiculos al inventario
inventario.add_vehiculo(carro1)
inventario.add_vehiculo(bicicleta1)
inventario.add_vehiculo(camion1)

# Anadir comprador al inventario
inventario.add_comprador(comprador1)

# Mostrar los vehiculos disponibles antes de la compra
inventario.mostrar_vehiculos_disponibles()

# El comprador consulta disponibilidad del vehiculo
comprador1.disponibilidad_vehiculo(carro1)

# El comprador realiza la compra del vehiculo
comprador1.comprar_vehiculo(carro1)

# Mostrar los vehiculos disponibles despues de la compra
inventario.mostrar_vehiculos_disponibles()
