#improtar las funciones de los modulos del paquete

from ecomerce.inventario import add_producto,eliminar_producto
from ecomerce.ventas import procesar_venta

add_producto('laptop', 10) #usamos la funcion add_producto del modulo inventario
eliminar_producto('laptop') #usamos la funcion eliminar_producto del modulo inventario
procesar_venta('laptop', 5)  #usamos la funcion procesar_venta del modulo ventas
