empleados = [
        {'name': 'Yesica', 'age': 27, "salary": 5000},
        {'name': 'Santiago', 'age': 28, "salary": 4000},
        {'name': 'Maria Ofelia', 'age': 30, "salary": 2200},
        {'name': 'Yesica', 'age': 15, "salary": 3000}
    ]

def salario_superior(empleados):
    salario_superior = []
    for i in empleados:
        if i['salary'] >= 3500:
            salario_superior.append((i['name'], i['salary']))
    print("Los empleados con mayor salario son:")
    for nombre, salario in salario_superior:           #en este caso separamos las variables para que podamos hacer un print mas interactivo 
        print(f"{nombre} con un salario de ${salario}") #o si no se veria en modo de listo como (jessica, santiago) (3000, 4500)
#pero de esta forma se vera mejor la salida del mensaje

salario_superior(empleados)







            
    
    





