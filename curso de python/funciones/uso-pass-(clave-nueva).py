# Este programa solicita al usuario un número entero y lo divide entre 10. y si no es un numero entero se genera un error y si el numero es
#cero se genera otro error que con el try y el except se pueden manejar los errores y no se cierra el programa
try:
    divisor = int(input("Introduce el divisor: "))
    resultado = 10 / divisor
    print(resultado)
except ZeroDivisionError as varieble: # Manejo de excepción para división por cero
    print("Error: No se puede dividir por cero.")
    print("ha ocurrido un error", varieble)  # Imprime el error específico
except ValueError as varieble:  # Manejo de excepción para valor no entero
    print("Error: Debe ingresar un número entero.")
    print("ha ocurrido un error", varieble)  # Imprime el error específico