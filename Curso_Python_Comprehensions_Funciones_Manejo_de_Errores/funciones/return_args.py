def volumen(alto=1, ancho=1, profundo=1):
    return alto * ancho * profundo

resultado = volumen(10, 20, 3)
print(resultado)
resultado2 = volumen(ancho=30) #solo mandamos la variable anchop en este caso y los demas seran el numero 1 como lo tenemosdefinido 
print(resultado2)              #si no lo definimos o no mandamos todos los valores cuando no definimos un valor por defecto nos mandara error 