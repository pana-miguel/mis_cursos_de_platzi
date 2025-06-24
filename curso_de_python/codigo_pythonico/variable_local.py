y = 100 #variable de tipo global ya que como tal esta definida desde un inicio y no dentro de una funcion y esta puede usarse en las otrsas funciones
def local_funcion():
    x = 10 #variable de tipo local
    print(f"el valor de la variable es {x}")
    

def global_funcion():
    print(f"el valor es {y}")

local_funcion()
#print(x) #no esta definido fuera de su metodo ya que x es una variable local y solo funciona en su metodo al imprimirlo fuera de el metodo

print(y) #en este caso si la imprime ya que es una varieble global