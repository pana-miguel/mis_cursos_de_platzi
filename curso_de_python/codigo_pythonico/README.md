# Código Pythonico

## ¿Qué es código pythonico?

El término **"código pythonico"** se refiere a escribir código en Python de una manera que sigue las convenciones, estilos y prácticas recomendadas por la comunidad Python. Es un código que no solo funciona, sino que también es **claro, legible, elegante y eficiente**.

El código pythonico aprovecha las características propias de Python para ser expresivo y fácil de entender, en lugar de usar formas demasiado complicadas o similares a otros lenguajes.

---

## ¿Cuándo se usa código pythonico?

Se debe usar siempre que escribas Python, para que tu código:

- Sea fácil de leer y mantener por otros (y por ti mismo en el futuro).
- Aproveche las funcionalidades y librerías estándar de Python.
- Evite redundancias y expresiones complicadas innecesarias.

---

## Ejemplos de código pythonico

### 1. Uso de comprensiones de listas en lugar de bucles tradicionales

```python
# No pythonico
cuadrados = []
for x in range(10):
    cuadrados.append(x ** 2)

# Pythonico
cuadrados = [x ** 2 for x in range(10)]
```
### 2. Uso de desempaquetado múltiple

```python
# No pythonico
coordenadas = (10, 20)
x = coordenadas[0]
y = coordenadas[1]

# Pythonico
x, y = coordenadas
```

### 3. Uso de funciones integradas y expresiones generadoras

```python
# No pythonico
suma = 0
for n in range(1, 101):
    suma += n

# Pythonico
suma = sum(range(1, 101))
```

### 4. Uso de manejo de excepciones para controlar errores.

```python
# No pythonico
if key in dict:
    value = dict[key]
else:
    value = None

# Pythonico
try:
    value = dict[key]
except KeyError:
    value = None
```

