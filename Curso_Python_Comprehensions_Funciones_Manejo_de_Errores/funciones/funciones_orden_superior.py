#lo que hace esto es crear dos variables en la primera se suma un numero mas 1 y en la segunda en este caso se sumara un numero mas 
#el resultado de laanterior funcion

def incrementar(x):
    return x + 1

def high_order_funcion(x, funcion):
    return x + funcion(x)

#enviandole como datos a x = 2 y a la funcion como tal la funcion que esta arriba funcion(x se llamaria practicamente incrementar(X))
#esto sifnifica que en el high order funcion hay un 2 en la x y se va a sumar lo que se traiga de la funcion de arriba 
#en el caso la funcion de arriba tambienreciobe un 2 por funcion(x) que al usar la funcion como variable es igual a incrementar(2)
#y lo que hace arriba es sumar 2 + 1 para posterior mente abajo sumar 2 + el resultado de arriba que es 3 dando 5 
resultado = high_order_funcion(2, incrementar)
print(resultado)


#esto es lo mismo que lo de arriba 
incrementar2 = lambda x: x + 1
hof2 = lambda x, funcion: x + funcion(x)

resultado2 = hof2(2, incrementar2)
print(resultado2)