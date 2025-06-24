"""
Este programa simula el funcionamiento básico de una biblioteca.

Define tres clases principales:
- Libro: Representa un libro con título, autor y estado de disponibilidad.
- Persona: Representa un usuario que puede prestar y devolver libros.
- Biblioteca: Administra una colección de libros y usuarios, permitiendo agregar libros, registrar usuarios y mostrar
- los libros disponibles.

El flujo principal crea varios libros y usuarios, los añade a una biblioteca, y muestra cómo un usuario puede prestar
y devolver un libro, actualizando la disponibilidad en la biblioteca.
"""


class Libro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.libro_disponible = True

    def prestar_libro(self):
        if self.libro_disponible:
            self.libro_disponible = False
            print(f"El libro {self.titulo} ha sido prestado.")
        else:
            print(f"El libro {self.titulo} no esta disponible.")
        
    def devolver_libro(self):
        self.libro_disponible = True
        print(f"El libro {self.titulo} ha sido devuelto.")

class Persona():
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.lista_libros_prestados = []
        
    def prestar_libro(self, libro):
        if libro.libro_disponible:
            libro.prestar_libro()
            self.lista_libros_prestados.append(libro.titulo)
        else:
            print(f"El libro {libro.titulo} no esta disponible.")

    def devolver_libro(self, libro):
        if libro in self.lista_libros_prestados:
            libro.devolver_libro()
            self.lista_libros_prestados.remove(libro)
        else:
            print(f"El libro {libro.titulo} no esta en la lista de prestados")

class Biblioteca():
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def añadir_libro(self, libro):
        self.libros.append(libro)
        print(f"El libro {libro.titulo} ha sido añadido a la biblioteca.")
    
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"El usuario {usuario.nombre} ha sido registrado en la biblioteca.")

    def mostrar_libros_disponibles(self):
        print("los libros disponibles son: ")
        for libro in self.libros:
            if libro.libro_disponible:
                print(f"{libro.titulo} creado por {libro.autor}")

#crear los libros
libro1 = Libro("El principito", "Antoine de Saint-Exupery")
libro2 = Libro("Cien años de soledad", "Gabriel Garcia Marquez")    
libro3 = Libro("1984", "George Orwell")
libro4 = Libro("El amor en los tiempos del colera", "Gabriel Garcia Marquez")
libro5 = Libro("El arte de la guerra", "Sun Tzu")
    
#crear los usuarios
usuario1 = Persona("Juan", 1)
usuario2 = Persona("Maria", 2)
usuario3 = Persona("Jose", 3)
usuario4 = Persona("Luis", 4)
usuario5 = Persona("Ana", 5)

#crear biblioteca
biblioteca1 = Biblioteca()
biblioteca1.añadir_libro(libro1)
biblioteca1.añadir_libro(libro2)
biblioteca1.añadir_libro(libro3)
biblioteca1.añadir_libro(libro4)
biblioteca1.añadir_libro(libro5)
biblioteca1.registrar_usuario(usuario1)
biblioteca1.registrar_usuario(usuario2)
biblioteca1.registrar_usuario(usuario3)
biblioteca1.registrar_usuario(usuario4)
biblioteca1.registrar_usuario(usuario5)

#MOSTRAR LIBROS DISPONIBLES
biblioteca1.mostrar_libros_disponibles()

#PRESTAR LIBROS
usuario1.prestar_libro(libro1)
biblioteca1.mostrar_libros_disponibles()

#retirar libro
usuario1.devolver_libro(libro1)
biblioteca1.mostrar_libros_disponibles()



    