# 🧵 Concurrencia y Paralelismo en Programación

## 📘 ¿Qué es la Concurrencia?

La **concurrencia** es la capacidad de un sistema para manejar múltiples tareas que progresan al mismo tiempo, aunque **no necesariamente se ejecuten al mismo tiempo**.

> 👉 Es como tener un solo cocinero preparando varios platos: mientras uno se cuece, el cocinero corta verduras para otro.

### ✅ ¿Para qué se usa?

- Mejorar el rendimiento percibido en aplicaciones.
- Realizar tareas que pueden esperar sin bloquear todo el sistema (por ejemplo, lectura de archivos, peticiones a red, etc.).
- Responder rápidamente en interfaces gráficas.

### 🧪 Ejemplo en Python (usando `asyncio`):

```python
import asyncio

async def tarea(nombre, segundos):
    print(f"{nombre} empieza")
    await asyncio.sleep(segundos)
    print(f"{nombre} termina después de {segundos}s")

async def main():
    await asyncio.gather(
        tarea("Tarea 1", 2),
        tarea("Tarea 2", 1)
    )

asyncio.run(main())
```
## ⚙️ ¿Qué es el Paralelismo?
El paralelismo ocurre cuando dos o más tareas se ejecutan realmente al mismo tiempo, utilizando múltiples núcleos de CPU.

👉 Es como tener varios cocineros, cada uno haciendo su propio plato al mismo tiempo.

✅ ¿Para qué se usa?
Aumentar el rendimiento real de procesamiento.

Ejecutar tareas pesadas como cálculos matemáticos, simulaciones o procesamiento de datos masivos.

### 🧪 Ejemplo en Python (usando multiprocessing)

```python
from multiprocessing import Process
import time

def tarea(nombre):
    print(f"{nombre} empieza")
    time.sleep(2)
    print(f"{nombre} termina")

if __name__ == '__main__':
    p1 = Process(target=tarea, args=("Tarea A",))
    p2 = Process(target=tarea, args=("Tarea B",))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

```


