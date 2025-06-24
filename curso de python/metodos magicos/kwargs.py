def imprimir_info(**kwargs):       #se usa cuando no se sabe la cantidad de informacion como args pero cuando hay una llave y un valor en ella 
    for key, value in kwargs.items(): #se usan key y value para despues mostrar la informacion y .item lo que hace es dividir la informacion en llaves
                                        #y contenido en ellas para que la llave se almacene en la primera variable en este caso key y el valor en la segunda 

        print(f'{key}: {value}')    #se imprimen la llave y el valor 

imprimir_info(name = 'jose', age = 30, city = 'bogota') #se define la llave y el valor que despues con el ciclo for se recorrera por cada una de estas
imprimir_info(name = 'jose',
            age = 30,
            city = 'bogota',
            country = 'colombia') #practicamente el ciclo for lo lee y lo msotrara de esta manera 