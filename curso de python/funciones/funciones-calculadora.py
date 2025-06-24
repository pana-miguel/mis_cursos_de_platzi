#las funciones en este ejercicio son funciones de una calculadora que realizan operaciones basicas como suma, resta, multiplicacion
# y division

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculadora():
    while True:
        print("\n--- Calculadora ---")
        print("Seleccione una operacion:")
        print("1. Suma")    
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        opcion = int(input("Ingrese su opcion (1-5): "))
        
        if opcion == 5:
            print("Saliendo de la calculadora.")
            break

        if opcion in [1, 2, 3, 4]:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == 1:
                print("La suma es:", suma(num1, num2))
            elif opcion == 2:    
                print("La resta es:", resta(num1, num2))
            elif opcion == 3:    
                print("La multiplicación es:", multiplicacion(num1, num2))
            elif opcion == 4:    
                print("La división es:", division(num1, num2))
        else:
            print("Opción no válida. Intente de nuevo.")
   
calculadora()
        

