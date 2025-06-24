class Base:
    def __init__(self):
        self._variable_protergida = 'protegido'
        self.__variable_pribada = 'privado'

    def _metodo_protegido(self):
        print('este es un metodo protegido')

    def __metodo_privado(self):
        print('esto es un metodo privado')

    def metodo_publico(self):
        self.__metodo_privado()

base = Base()
print(base._variable_protergida)
base._metodo_protegido()
base.metodo_publico()
#print(base.__variable_pribada) #nos mostrara que hay un error y que no existe porque es privada en la terminal o al usuario