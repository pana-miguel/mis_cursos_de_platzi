# 🌀 Decoradores en Python

## 📘 ¿Qué es un decorador?

Un **decorador en Python** es una función que **envuelve otra función para modificar su comportamiento** sin alterar su estructura original.

> En otras palabras: los decoradores te permiten **añadir funcionalidades** extra a una función de forma limpia y reutilizable.

---

## 🛠️ ¿Para qué sirven los decoradores?

- Agregar lógica antes o después de ejecutar una función.
- Registrar llamadas a funciones.
- Verificar permisos o autenticación.
- Medir el tiempo de ejecución.
- Validar argumentos.

---

## ⚙️ ¿Cómo se usa un decorador?

```python
def mi_decorador(func):
    def funcion_envuelta():
        print("Antes de la función")
        func()
        print("Después de la función")
    return funcion_envuelta

@mi_decorador
def saludar():
    print("Hola!")

saludar()
```
# Resultado 

```python
Antes de la función
Hola!
Después de la función
```

# 🧪 Ejemplo 1: Medir tiempo de ejecución

```python
import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱️ Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def tarea_lenta():
    time.sleep(2)
    print("Tarea completada")

tarea_lenta()
```

# Resultado

```python
Tarea completada
⏱️ Tiempo de ejecución: 2.0001 segundos
```