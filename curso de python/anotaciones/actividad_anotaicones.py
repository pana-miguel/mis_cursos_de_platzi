#en este codigo lo que hacemos es crear una lista de empleados con su nombre edad y sueldo 
#y lo que hacemos es crear una funcion que nos muestre los empleados que tienen un sueldo mayor a 3100

empleados_planta = [
    {"nombre": "Carlos Gómez", "edad": 35, "sueldo": 3200},
    {"nombre": "Laura Méndez", "edad": 29, "sueldo": 3100},
    {"nombre": "Jorge Rivas", "edad": 41, "sueldo": 3500},
    {"nombre": "Paula Sánchez", "edad": 33, "sueldo": 3000},
    {"nombre": "Hernán Díaz", "edad": 38, "sueldo": 3300}
]
#asi se ve un codigo basico
"""def mayor_salario():
    for empleados in  empleados_planta:
        if empleados['sueldo'] > 3100:
            print(empleados)

mayor_salario()"""

#este es un codigo mejor 
def mayor_salario():
    print([empleado for empleado in empleados_planta if empleado['sueldo'] > 3100])

mayor_salario()