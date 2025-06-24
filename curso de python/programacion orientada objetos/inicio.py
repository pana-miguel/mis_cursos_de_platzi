class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saludar(self):
        print(f"hola, minombre es {self.name} y tengo {self.age} años.")


persona1 = Persona("Juan", 30)
persona2 = Persona("Maria", 25)

persona1.saludar()
persona2.saludar()