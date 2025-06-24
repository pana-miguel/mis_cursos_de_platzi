#en esta funcion se imprime la jerarquia de excepciones en python

def print_exception_hierarchy(exception_class, indent=0): #definimos una funcion que recibe una clase de excepcion y un indentado
    print(' ' * indent + exception_class.__name__)   #imprimimos el nombre de la clase de excepcion con un indentado
    for subclass in exception_class.__subclasses__(): #iteramos sobre las subclases de la clase de excepcion
        print_exception_hierarchy(subclass, indent + 4) #llamamos a la funcion recursivamente con un indentado mayor

print_exception_hierarchy(Exception) #imprimimos la jerarquia de excepciones a partir de la clase Exception

#cuando imprimimos esto nos muestra la jerarquia de excepciones en python