#asincyo es una libreria de python que permite ejecutar codigo de manera asincrona
#significa que el codigo no se ejecuta de manera secuencial, sino que se puede ejecutar en paralelo dos  o mas tareas

import asyncio

async def proceso(data): #definimos una variable asincrona
    print(f'procesando: {data} ...') # imprimimos el mensaje que se esta procesando la variable
    #simular una operacion
    await asyncio.sleep(10) #esperamos 10 segundos para simular una operacion larga
    print(f'{data} ya termino de procesarce') # imprimimos el mensaje que indica que la variable ya termino de procesarse
    return data * 2 #retornamos el resultado de la operacion esto para simular que se esta procesando un archivo

async def main(): # funcion principal que se ejecutara de manera asincrona
    print('inicio de procesamiento') 
    resultado = await proceso('archivo.txt') # llamamos a la funcion proceso y esperamos su resultado de procesar un archivo
    print(f'resultado {resultado}') # imprimimos el resultado de la operacion

asyncio.run(main()) # ejecutamos la funcion principal de manera asincrona