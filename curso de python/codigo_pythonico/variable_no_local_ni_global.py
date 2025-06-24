def otra_funcio():
    x = 'encapsulada'
    def funcion_inerte():
        nonlocal x  #con este se puede cambiar los demas variables que se llamen igul sin importar si son locales o globales 
        x = 'valor modificado'
        print(f"el valor inerte es {x}")
    funcion_inerte()
    print(f"el valor de ora funcion es {x}")
otra_funcio()