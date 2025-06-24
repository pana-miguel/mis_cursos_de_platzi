import asyncio
import multiprocessing
import time
import random

# función asincrónica para verificar inventario
async def Check_inventario(item):
    print(f'verificando inventario para {item}')
    await asyncio.sleep(random.randint(3, 6))
    print(f'inventario verificado para {item}')
    return random.choice([True, False])

# función asincrónica para procesar el pago
async def procesar_pago(orden_id):
    print(f'procesando pago para la orden {orden_id} ...')
    await asyncio.sleep(random.randint(3, 6))
    print(f'pago procesado para la orden {orden_id}')
    return True

# función para simular CPU-bound: calcular costo total
def calcular_total(items):
    print(f'calculando el costo total para {len(items)} artículos ...')
    time.sleep(5)
    total = sum(item['price'] for item in items)
    print(f'costo total calculado: {total}')
    return total

# función asincrónica principal de procesamiento de orden
async def proceso_orden(orden_id, items):
    print(f'iniciando el procesamiento de la orden {orden_id}')
    
    # verificar inventario
    inventario_checks = [Check_inventario(item['name']) for item in items]
    inventario_resultados = await asyncio.gather(*inventario_checks)

    if not all(inventario_resultados):
        print(f'orden {orden_id} se canceló porque uno o más productos no están disponibles')
        return

    # usar multiprocessing para calcular el total
    with multiprocessing.Pool() as pool:
        total = pool.apply(calcular_total, (items,))

    # procesar el pago
    pagos_resultado = await procesar_pago(orden_id)

    if pagos_resultado:
        print(f'la orden {orden_id} fue completada con éxito')
        print(f'total: {total}')
    else:
        print(f'error al procesar el pago en la orden {orden_id}')

# función main
async def main():
    orders = [
        {'order_id': 1, 'items': [{'name': 'Laptop', 'price': 1000}, {'name': 'Mouse', 'price': 50}]},
        {'order_id': 2, 'items': [{'name': 'Teclado', 'price': 80}, {'name': 'Monitor', 'price': 300}]},
        {'order_id': 3, 'items': [{'name': 'Smartphone', 'price': 700}, {'name': 'Funda', 'price': 20}]}
    ]

    tasks = [proceso_orden(order['order_id'], order['items']) for order in orders]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
