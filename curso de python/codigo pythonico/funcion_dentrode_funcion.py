x = 'global' #variable global

#funcion externa
def funcion_externa():
    x = 'valor encapsulado'

    #funcion interna a la funcion que ya tenemos
    def funcion_interna():
        x = 'local' #variable local
        print(x)

    funcion_interna()
    print(x) 

funcion_externa() #entrar a la funcion funcion externa
print(x)