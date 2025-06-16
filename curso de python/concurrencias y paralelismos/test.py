import asyncio
import random

#este codigo es un ejemplo de como descargar archivos de manera asincrona
async def donwload_process(file):
    print(f'Descargando archivo {file}') # imprimimos el mensaje que indica que se esta descargando el archivo
    time=random.randint(1,10) #simulamos el tiempo de descarga de un archivo entre 1 y 10 segundos
    await asyncio.sleep(time) #esperamos el tiempo de descarga del archivo
    print(f'{file} downloaded') # imprimimos el mensaje que indica que el archivo ya fue descargado
    return file #retornamos el nombre del archivo descargado

async def main():
    print('Inicio de la descarga')
    result=await donwload_process('file1.txt') # llamamos a la funcion donwload_process y esperamos su resultado de descargar un archivo
    result1=await donwload_process('file2.txt')
    result2=await donwload_process('file3.txt')
    print(f'{result,result1,result2}')


asyncio.run(main()) # ejecutamos la funcion principal de manera asincrona