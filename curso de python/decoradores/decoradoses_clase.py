#un dcorador de clase es un decorador que se aplica a una clase
# se utiliza para modificar el comportamiento de la clase o sus metodos

class calculadora:
    
    @staticmethod #estaticmethod es un decorador que indica que el metodo no necesita una instancia de la clase para ser llamado
    def sumar(a: int, b: int) -> int:
        return a + b
    
print(calculadora.sumar(2, 3))  # Imprime: 5