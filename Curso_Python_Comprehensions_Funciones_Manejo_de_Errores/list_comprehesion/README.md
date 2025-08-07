# 📚 List Comprehensions en Python (Listas y Diccionarios)

En Python, las **List Comprehensions** y **Dictionary Comprehensions** son formas concisas y legibles de crear listas y diccionarios a partir de iterables, aplicando transformaciones y filtrados.

---

## 🔹 List Comprehensions (en listas)

Permiten generar listas de forma compacta.

**Sintaxis:**
```python
[expresion for elemento in iterable if condicion]
```

**Características:**
- Más legibles que los bucles tradicionales para operaciones simples.
- Pueden incluir condiciones (`if`) para filtrar elementos.

**Ejemplo:**
```python
# Lista de cuadrados de números del 0 al 4
cuadrados = [x**2 for x in range(5)]
# cuadrados = [0, 1, 4, 9, 16]

# Lista con solo números pares del 0 al 9
pares = [x for x in range(10) if x % 2 == 0]
# pares = [0, 2, 4, 6, 8]
```

---

## 🔹 Dictionary Comprehensions (en diccionarios)

Permiten generar diccionarios de forma compacta.

**Sintaxis:**
```python
{clave: valor for elemento in iterable if condicion}
```

**Características:**
- Crean diccionarios aplicando operaciones sobre iterables.
- Pueden filtrar elementos con condiciones.

**Ejemplo:**
```python
# Diccionario con números y su cuadrado
cuadrados_dict = {x: x**2 for x in range(5)}
# cuadrados_dict = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Diccionario solo con pares
pares_dict = {x: x**2 for x in range(10) if x % 2 == 0}
# pares_dict = {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

---

## ✅ Ventajas
- Código más compacto y legible.
- Fácil de combinar filtrado y transformación.
- Mejor rendimiento que un bucle `for` tradicional en operaciones simples.

---

## ⚠️ Cuándo evitarlos
- Cuando la lógica es compleja y afecta la legibilidad.
- Cuando se anidan más de dos niveles.

---

📌 **Resumen:**
- **List Comprehension:** crea listas en una sola línea.
- **Dictionary Comprehension:** crea diccionarios en una sola línea.
