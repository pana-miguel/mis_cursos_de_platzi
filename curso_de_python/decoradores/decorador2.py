def check_acceso(funcion):
    def envoltura(empleado):
        # comprobar si el empleado tiene rol 'admins'
        if empleado.get('rol') == 'admin':
            return funcion(empleado)
        else:
            print("no eres administrador")
    return envoltura

@check_acceso

def eliminar_empleados(empleados):
    print(f'el empleado {empleados['name']} ha sido eliminado')

admin = {'name': 'carlos', 'rol': 'admin'}
empleados = {'name': 'ana', 'rol': 'empleado'}

eliminar_empleados(admin)
eliminar_empleados(empleados)