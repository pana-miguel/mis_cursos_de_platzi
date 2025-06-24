#este es un ejemplo de un sistema de concesionaria de vehiculos en Python
#en el cual solo vendera vehiculos a los usuarios y no los prestara o comprara
#el vehiculo solo se podra vender una vez y no se podra comprar mas de una vez ya que no se especifica la cantidad de vehiculos
#por ello se intuye de que hay un solo vehiculo por cada id de vehiculo

class Vehiculo():
    def __init__(self, id_carro ,marca, modelo, anio, precio, descripcion):
        self.id_carro = id_carro
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
        self.descripcion = descripcion
        self.vendido = False
        
    def vender_carro(self):
        if not self.vendido:
            self.vendido = True
            print(f"El carro {self.marca} {self.modelo} se vendio")
        else:
            print(f"El carro {self.marca} {self.modelo} ya se habia vendido.")

#de esta forma tambien se puede hacer el codigo de arriba
    """def vender_carro(self):
        mensaje = f"El carro {self.marca} {self.modelo} "
        print(mensaje + ("se vendió" if not self.vendido else "ya se había vendido."))
        self.vendido = True"""

    
class Usuario():
    def __init__(self, nombre, edad, id_usuario):
        self.nombre = nombre
        self.edad = edad
        self.id_usuario = id_usuario
        self.carros_comprados = []

    def comprar_carro(self, vehiculo):
        if not vehiculo.vendido:
            vehiculo.vender_carro()
            self.carros_comprados.append(vehiculo)
            print(f"{self.nombre} ha comprado el carro {vehiculo.marca} {vehiculo.modelo}.")
        else:
            print(f"El carro {vehiculo.marca} {vehiculo.modelo} no esta disponible porque ya habia sido vendido.")

#esta es la unica forma de resumir el codigo en este caso
    """def comprar_carro(self, vehiculo):
        if not vehiculo.vendido:
            vehiculo.vender_carro(); self.carros_comprados.append(vehiculo)
            print(f"{self.nombre} ha comprado el carro {vehiculo.marca} {vehiculo.modelo}.")
        else:
            print(f"El carro {vehiculo.marca} {vehiculo.modelo} no está disponible porque ya había sido vendido.")"""

class Concesionaria():
    def __init__(self):
        self.vehiculos = []
        self.usuarios = []
    
    def añadir_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"El vehiculo {vehiculo.marca} {vehiculo.modelo} ha sido añadido a la concesionaria.")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"El usuario {usuario.nombre} ha sido registrado en la concesionaria.")

    def mostrar_vehiculos_disponibles(self):
        print("Los vehiculos disponibles son: ")
        for vehiculo in self.vehiculos:
            if not vehiculo.vendido:
                print(f"{vehiculo.marca} {vehiculo.modelo} {vehiculo.anio} ${vehiculo.precio} - {vehiculo.descripcion}")

#de esta forma se pone la condicion al final si se requiere pero asi es menos facil de entender el codigo
    """def mostrar_vehiculos_disponibles(self):
        print("Los vehículos disponibles son:")
        [print(f"{v.marca} {v.modelo} {v.anio} ${v.precio} - {v.descripcion}") for v in self.vehiculos if not v.vendido]"""


# Crear los vehiculos
vehiculo1 = Vehiculo(1, "Toyota", "Corolla", 2020, 20000, "Un carro economico y confiable.")
vehiculo2 = Vehiculo(2, "Honda", "Civic", 2021, 22000, "Un carro deportivo y elegante.")

# Crear los usuarios
usuario1 = Usuario("Juan", 30, 1)

# Crear la concesionaria
concesionaria = Concesionaria()
concesionaria.añadir_vehiculo(vehiculo1)
concesionaria.añadir_vehiculo(vehiculo2)
concesionaria.registrar_usuario(usuario1)
concesionaria.mostrar_vehiculos_disponibles()

# Comprar un vehiculo
usuario1.comprar_carro(vehiculo1)
concesionaria.mostrar_vehiculos_disponibles()
# Comprar el mismo vehiculo de nuevo
usuario1.comprar_carro(vehiculo1)  # Intentar comprar un vehiculo que ya fue vendido por lo que no se podra comprar de nuevo y esta venta se cancelara
# Comprar otro vehiculo
usuario1.comprar_carro(vehiculo2)
concesionaria.mostrar_vehiculos_disponibles()




    

