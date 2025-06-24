# Métodos Mágicos en Python

## 1. Inicialización y Representación

- `__init__`: Inicializa una nueva instancia.  
- `__new__`: Controla la creación de una instancia antes de inicializarla.  
- `__del__`: Ejecuta lógica al eliminar una instancia.  
- `__repr__`: Devuelve una representación formal del objeto.  
- `__str__`: Devuelve una representación informal legible del objeto.

## 2. Operadores Aritméticos

- `__add__`: Suma (+).  
- `__sub__`: Resta (-).  
- `__mul__`: Multiplicación (*).  
- `__truediv__`: División (/).  
- `__floordiv__`: División entera (//).  
- `__mod__`: Módulo (%).  
- `__pow__`: Potencia (**).  
- `__neg__`: Negativo (-obj).

## 3. Operadores de Comparación

- `__eq__`: Igualdad (==).  
- `__ne__`: Desigualdad (!=).  
- `__lt__`: Menor que (<).  
- `__le__`: Menor o igual que (<=).  
- `__gt__`: Mayor que (>).  
- `__ge__`: Mayor o igual que (>=).

## 4. Contenedores e Iteradores

- `__getitem__`: Acceso por índice (obj[i]).  
- `__setitem__`: Asignación por índice (obj[i] = valor).  
- `__delitem__`: Eliminación por índice (del obj[i]).  
- `__len__`: Tamaño (len(obj)).  
- `__iter__`: Devuelve un iterador para el objeto.  
- `__next__`: Devuelve el siguiente elemento del iterador.  
- `__contains__`: Verifica si un elemento está contenido (x in obj).

## 5. Representaciones Numéricas

- `__int__`: Conversión a entero (int(obj)).  
- `__float__`: Conversión a flotante (float(obj)).  
- `__bool__`:
