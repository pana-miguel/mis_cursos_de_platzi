#ejemplo de anotaciones en funciones y clases

class Empleado:
    name: str
    age: str
    salary: float

    def __init__(self, name: str, age: str, salary: float ):
        self.name = name
        self.age = age
        self.salary = salary

    def presentaicon(self) -> str:
        return f"hola me llamo {self.name} y tengo {self.age} anios"
    
empleado1 = Empleado('carlos', 30, 3500.0)
print(empleado1.presentaicon())