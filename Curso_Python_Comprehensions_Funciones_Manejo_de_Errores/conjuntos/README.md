# 🐍 Curso de Python: Conceptos Fundamentales

Este documento recopila varios temas clave de Python, incluyendo módulos, decoradores, funciones,
manejo de archivos, paquetes, métodos mágicos, POO, variables, condicionales, tipos de datos,
y conjuntos.

---

## 📦 Creación de Módulos en Python

En Python, un **módulo** es un archivo con extensión `.py` que contiene definiciones y declaraciones de Python.
Sirve para organizar el código en partes reutilizables.

**Uso:**
```python
# mi_modulo.py
def saludar(nombre):
    return f"Hola, {nombre}"

# main.py
import mi_modulo
print(mi_modulo.saludar("Juan"))
```

---

## 🎯 Decoradores en Python

Los **decoradores** son funciones que envuelven a otras funciones para modificar o ampliar su comportamiento
sin cambiar su código original.

**Ejemplo 1: Decorador básico**
```python
def decorador(func):
    def envoltura():
        print("Antes de la función")
        func()
        print("Después de la función")
    return envoltura

@decorador
def saludar():
    print("Hola!")

saludar()
```

**Ejemplo 2: Decorador con argumentos**
```python
def repetir(n):
    def decorador(func):
        def envoltura(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return envoltura
    return decorador

@repetir(3)
def decir(msg):
    print(msg)

decir("Python")
```

---

## 🛠 Funciones en Python

Las **funciones** son bloques de código reutilizables que realizan una tarea específica.

**Ejemplo:**
```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)
```

---

## 📂 Manejo de Archivos en Python

Permite leer, escribir y manipular archivos en disco.

**Ejemplo:**
```python
# Escribir en un archivo
with open("archivo.txt", "w") as f:
    f.write("Hola, Python!")

# Leer un archivo
with open("archivo.txt", "r") as f:
    contenido = f.read()
    print(contenido)
```

---

## 📦 Manejo de Paquetes

Un **paquete** es una colección de módulos organizados en carpetas con un archivo `__init__.py`.

**Estructura:**
```
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
```

**Uso:**
```python
from mi_paquete import modulo1
```

---

## 🔮 Métodos Mágicos en Python

Algunos de los más usados son:
- `__init__`
- `__str__`
- `__repr__`
- `__len__`
- `__getitem__`
- `__setitem__`
- `__delitem__`
- `__iter__`
- `__next__`
- `__call__`
- `__eq__`
- `__lt__`
- `__gt__`
- `__add__`
- `__sub__`
- `__mul__`
- `__truediv__`
- `__floordiv__`
- `__mod__`
- `__pow__`

---

## 🚗 Programación Orientada a Objetos (POO) – Ejemplo de un Carro

```python
class Carro:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El {self.marca} {self.modelo} está arrancando.")

    def detener(self):
        print(f"El {self.marca} {self.modelo} se ha detenido.")

mi_carro = Carro("Toyota", "Corolla", "Rojo")
mi_carro.arrancar()
mi_carro.detener()
```

---

## 🔢 Variables, Condicionales y Tipos de Datos

**Variables:** nombre que almacena un valor.

**Condicionales:**
- `if`
- `elif`
- `else`

**Tipos de datos:**
- `int`
- `float`
- `str`
- `bool`
- `list`
- `tuple`
- `set`
- `dict`
- `NoneType`

---

## 🧩 Conjuntos en Python

Los **conjuntos** (`set`) son colecciones desordenadas de elementos únicos.

**Ejemplo:**
```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # Unión
print(A & B)  # Intersección
print(A - B)  # Diferencia
print(A ^ B)  # Diferencia simétrica
```

**Comprensión de conjuntos:**
```python
numeros = [1, 2, 2, 3, 4, 4, 5]
unicos = {n for n in numeros if n % 2 == 0}
print(unicos)
```

---
