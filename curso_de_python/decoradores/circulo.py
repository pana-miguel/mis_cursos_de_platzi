# La clase Circulo representa un círculo con un radio y puede calcular su área
class Circulo:
    def __init__(self, radio: float):
        # El atributo _radio se declara "privado" por convención (guion bajo al inicio)
        # para acceder a él mediante propiedades (getters y setters).
        self._radio = radio

    # -----------------------
    # @property:
    # Este decorador convierte el método 'area' en una propiedad.
    # Permite acceder a 'area' como si fuera un atributo (sin paréntesis).
    # Se usa para exponer atributos derivados (como el área) de forma elegante y controlada.
    # -----------------------
    @property 
    def area(self) -> float:
        # Calcula y retorna el área del círculo usando el radio actual
        return 3.1415 * (self._radio ** 2)

    # -----------------------
    # @property:
    # Este decorador convierte el método 'radio' en un getter.
    # Permite acceder al valor del radio de forma controlada.
    # -----------------------
    @property
    def radio(self) -> float:
        # Retorna el valor del atributo privado _radio
        return self._radio

    # -----------------------
    # @radio.setter:
    # Este decorador define un "setter" para la propiedad 'radio'.
    # Permite establecer un nuevo valor a 'radio' como si fuera una variable pública.
    # Aquí se puede incluir lógica de validación (por ejemplo, no permitir valores negativos).
    # -----------------------
    @radio.setter 
    def radio(self, value: float):
        # Si el valor nuevo es negativo, se lanza un error
        if value < 0:
            raise ValueError('el radio no puede ser negativo')
        # Si el valor es válido, se asigna al atributo privado _radio
        self._radio = value

# Crear una instancia de la clase Circulo con radio 5
circulo1 = Circulo(5)

# Accede a la propiedad 'area' como si fuera un atributo (sin usar paréntesis)
print(circulo1.area)  # Salida: 78.53750000000001

# Se cambia el radio del círculo usando el setter (gracias a @radio.setter)
circulo1.radio = 10

# Se imprime el área nuevamente, ahora con el nuevo radio
print(circulo1.area)  # Salida: 314.15000000000003



  
    



