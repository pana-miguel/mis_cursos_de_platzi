#decorador que comprueba si un empleado tiene un rol especifico 
def check_acceso(rol_requerido):
    def decorador(funcion):
        def envolver(empleado):
            #comprobamos si el rol del empleado coincide con el rol requerido
            if empleado.get('rol') == rol_requerido:
                return funcion(empleado)
            else:
                print("no tienes acceso ya que no eres administrador")
        return envolver
    return decorador

def log_accion(funcion):
    def envolver(empleado):
        print(f"registrando accion para el empleado {empleado['name']}")
        return funcion(empleado)
    return envolver

@check_acceso('admin') #aqui definimos las anteriores funciones para ejecutar el codigo de otra forma 
@log_accion
def eliminar_emppleado(empleado):
    print(f"el empleado {empleado['name']} ha sido eliminado")

admin = {'name': 'carlos', 'rol': 'admin'}
empleados = {'name': 'ana', 'rol': 'empleado'}

eliminar_emppleado(admin)
eliminar_emppleado(empleados)