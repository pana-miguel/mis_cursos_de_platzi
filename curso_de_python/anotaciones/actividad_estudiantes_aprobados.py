# Dada una lista de estudiantes con sus nombres y notas, filtra los estudiantes que han aprobado (nota mayor a 3.0)

estudiantes = [
    {"nombre": "Ana", "nota": 3.5},
    {"nombre": "Luis", "nota": 2.8},
    {"nombre": "María", "nota": 4.1},
    {"nombre": "Juan", "nota": 1.9},
    {"nombre": "Sofía", "nota": 3.9}
]

"""def estudiantes_aprobados():
    for estudiante in estudiantes:
        if estudiante['nota'] > 3.0:
            print(f"el o la estudiante {estudiante['nombre']} han pasado la materia")

estudiantes_aprobados()"""

"""def estudiantes_aprobados():
    print([estudiante for estudiante in estudiantes if estudiante['nota'] > 3.0 ] )

estudiantes_aprobados()"""

def estudiantes_aprobados():
    aprobados = [est for est in estudiantes if est['nota'] > 3.0]
    for est in aprobados:
        print(f"{est['nombre']} aprobó con {est['nota']}")

estudiantes_aprobados()