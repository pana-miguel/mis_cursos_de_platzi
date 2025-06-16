#de esta forma se ejecuta la cantidad de veces que nosotros queramos en un lapso de tiempo que todas las iteraciones o hilos 
#se ejecutan al mismo tiempo esto dependera de la cantidad de nucleos de nuestro pc preo es solo testeando como se puede hacer
#mas eficiente este codigo


import threading
import time

# Función que simula el procesamiento de una solicitud.
# Cada hilo llamará a esta función pasándole su propio ID.
def solicitud(solicitud_id):
    print(f'procesando solicitud {solicitud_id}')
    time.sleep(5)  # Simula un trabajo que tarda 3 segundos
    print(f'solicitud {solicitud_id} completada')


# Lista donde guardaremos los objetos Thread
hilos = []

# Bucle que itera i = 0, 1 y 2 (en total 3 iteraciones)
for i in range(5):
    # Por cada valor de i creamos un Thread que ejecuta 'solicitud(i)'
    # args=(i,) es una tupla con un solo elemento
    hilo = threading.Thread(target=solicitud, args=(i,))
    # Añadimos el hilo a la lista para poder hacer join más tarde
    hilos.append(hilo)
    # Arrancamos el hilo: a partir de aquí corre en paralelo
    hilo.start()

# Una vez lanzados todos los hilos, esperamos a que terminen:
for hilo in hilos:
    hilo.join()  # El hilo principal se bloquea hasta que éste termine

# Cuando todos los join() han finalizado:
print('todas las solicitudes fueron completadas')


