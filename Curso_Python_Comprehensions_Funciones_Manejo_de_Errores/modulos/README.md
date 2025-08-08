# Conjuntos en Python

## ¿Qué es un conjunto?

Un **conjunto** (o *set* en inglés) es una colección desordenada de elementos únicos.  
Los conjuntos son útiles cuando quieres almacenar elementos sin duplicados y realizar operaciones matemáticas como unión, intersección o diferencia.

---

## Características principales

- No permiten elementos repetidos.
- No mantienen un orden específico.
- Son mutables (puedes agregar o eliminar elementos).
- Se usan para operaciones de teoría de conjuntos.

---

## Crear conjuntos

```python
# Crear un conjunto vacío
conjunto_vacio = set()

# Crear un conjunto con elementos
numeros = {1, 2, 3, 4, 5}
```

### Operaciones comunes

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Unión: elementos en A o B
union = A | B  # {1, 2, 3, 4, 5, 6}

# Intersección: elementos en A y B
interseccion = A & B  # {3, 4}

# Diferencia: elementos en A pero no en B
diferencia = A - B  # {1, 2}

# Diferencia simétrica: elementos en A o B pero no en ambos
diferencia_simetrica = A ^ B  # {1, 2, 5, 6}
```

### Métodos útiles

- add(elemento): agrega un elemento.
- remove(elemento): elimina un elemento (error si no existe).
- discard(elemento): elimina un elemento (no da error si no existe).
- clear(): elimina todos los elementos.
- len(conjunto): devuelve el número de elementos.

### Ejemplo 

```python
frutas = {"manzana", "banana", "naranja"}
frutas.add("kiwi")
frutas.discard("banana")
print(frutas)  # Puede mostrar {'manzana', 'naranja', 'kiwi'}
```

# Resumen
Los conjuntos son estructuras ideales para manejar colecciones sin duplicados y realizar operaciones de conjuntos de forma eficiente y sencilla.

