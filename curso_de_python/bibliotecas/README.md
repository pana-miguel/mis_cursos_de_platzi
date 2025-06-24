# 📚 Librerías o Bibliotecas de Python

## 🧠 ¿Qué es una librería en Python?

Una **librería** (o **biblioteca**) en Python es un conjunto de módulos que contienen funciones, clases y herramientas ya desarrolladas por otros programadores, listas para ser utilizadas sin tener que escribir el código desde cero.

> En otras palabras, son colecciones de código reutilizable que te ayudan a **resolver problemas específicos** de forma más rápida y eficiente.

---

## 🎯 ¿Para qué sirven las librerías?

- ✅ Ahorran tiempo de desarrollo.
- ✅ Evitan repetir código que ya existe.
- ✅ Permiten trabajar con tareas complejas como análisis de datos, gráficos, inteligencia artificial, desarrollo web y más.
- ✅ Fomentan el uso de buenas prácticas y estándares.

---

## 🌟 Ejemplos de librerías populares en Python

### 1. `NumPy`
- Sirve para trabajar con **matemáticas** y **arrays multidimensionales**.
- Esencial para ciencia de datos y computación numérica.

```python
import numpy as np
a = np.array([1, 2, 3])
```

---

### 2. `Pandas`
- Ideal para **análisis y manipulación de datos estructurados** (como tablas o Excel).
- Usa estructuras como `DataFrame`.

```python
import pandas as pd
df = pd.read_csv("archivo.csv")
```

---

### 3. `Matplotlib`
- Permite crear **gráficos y visualizaciones** de datos.
- Compatible con `NumPy` y `Pandas`.

```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

---

### 4. `Requests`
- Se utiliza para hacer **solicitudes HTTP** fácilmente (como conectarse a APIs).

```python
import requests
response = requests.get("https://api.example.com")
```

---

### 5. `Flask`
- Framework para construir **aplicaciones web** pequeñas y rápidas.

```python
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hola mundo"
```

---

### 6. `TensorFlow` / `PyTorch`
- Bibliotecas para crear y entrenar **modelos de inteligencia artificial y aprendizaje automático**.

```python
import tensorflow as tf
model = tf.keras.Sequential()
```

---

### 7. `FastAPI`
- Framework moderno y rápido para crear **APIs RESTful** en Python.

```python
from fastapi import FastAPI
app = FastAPI()
```

---

## ✅ Recomendación

Aprender a usar las principales bibliotecas de Python es fundamental para convertirte en un programador más eficiente. Cada una resuelve un problema específico y puede acelerar el desarrollo de tus proyectos.
