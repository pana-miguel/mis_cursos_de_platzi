class Empleado:
    def __init__(self, name, *args, **kwargs):
        self.name = name 
        self.habilidades = args
        self.detalles = kwargs

    def informacion_empleado(self):
        print(f'empleado: {self.name}')
        print(f'habilidades: {self.habilidades}')
        print(f'detalles: {self.detalles}')

empleado = Empleado('carlos', 'python', 'java', 'c++', age = 30, city = 'bogota')
empleado.informacion_empleado()


empleado = Empleado('carlos',                    #se almacena en self.name ya que si esta definida
                    'python', 'java', 'c++',     #se almacenan los3 e agrs porque no estan definidas y no se sabia cuantos eran
                    age = 30, city = 'bogota')   #se almacena en kwargs ya que son definiciones de el empleado mostradas por llave y informacion 