class MultiplierFactory:
    """
    Clase que actúa como una fábrica de multiplicadores.

    Esta clase crea objetos que pueden multiplicar un número dado por un factor
    específico definido al momento de instanciar la clase.

    Métodos:
    --------
    __new__(cls, factor: int)
        Controla la creación de una nueva instancia y muestra un mensaje con el factor.

    __init__(self, factor: int)
        Inicializa la instancia asignando el factor de multiplicación.

    __call__(self, number: int) -> int
        Permite que la instancia se comporte como una función, multiplicando el número dado por el factor.
    """

    def __new__(cls, factor: int):
        """
        Crea y devuelve una nueva instancia de la clase.

        Args:
            factor (int): El factor por el cual se multiplicarán los números.

        Returns:
            instancia de MultiplierFactory
        """
        print(f"Creando instancia con factor {factor}")
        return super(MultiplierFactory, cls).__new__(cls)

    def __init__(self, factor: int):
        """
        Inicializa la instancia con el factor dado.

        Args:
            factor (int): Factor de multiplicación que se usará en la instancia.
        """
        print(f"Inicializando con factor {factor}")
        self.factor = factor

    def __call__(self, number: int) -> int:
        """
        Permite llamar la instancia como si fuera una función.

        Multiplica el número dado por el factor almacenado en la instancia.

        Args:
            number (int): Número a multiplicar.

        Returns:
            int: Resultado de multiplicar el número por el factor.
        """
        return number * self.factor


# Ejemplo de uso:

multiplier = MultiplierFactory(5)  # Crea un multiplicador con factor 5
result = multiplier(10)             # Multiplica 10 por 5
print(result)                      # Imprime 50
