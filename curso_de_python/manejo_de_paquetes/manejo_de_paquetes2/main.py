#importamos los modulos que estan dentro del paquete ecomerce
#desde aqui podemos traer los modulos que estan dentro de cada paquete solo hay que escribir bien la ruta


from ecomerce.inventario.stocks import add_producto,eliminar_producto #est ruta que es ecomerce.inventario.stocks es el paquete ecomerce y stocks es el modulo que contiene las funciones add_producto y eliminar_producto
from ecomerce.ventas.ordenes import cantidad_ordenes #importamos la funcion cantidad_ordenes del modulo ordenes que esta dentro del paquete ventas

add_producto('laptop', 10)
eliminar_producto('laptop')
cantidad_ordenes(5)