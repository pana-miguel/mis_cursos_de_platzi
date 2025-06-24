def great(name, apellido):
    print("Hola", name, apellido)

great("miguel", "sierra")
#great("maria")  #grenera un error porque no se le pasa el segundo argumento


def great(name, apellido="no tiene apellido"): #con apellido se soluciona el problema de la anterior funcion
    print("Hola", name, apellido)

great("miguel", "sierra")
great("maria")                #se genera el nombre por defecto y el apeellido sera "no tiene apellido"
great(apellido="sierra", name="miguel") #se puede definir los parametros por su nombre y se quedara igual 