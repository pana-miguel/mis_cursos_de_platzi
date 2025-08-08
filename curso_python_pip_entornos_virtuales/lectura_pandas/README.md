# Introducción a Pandas

**Pandas** es una biblioteca de Python muy popular para el análisis y manipulación de datos. Permite trabajar fácilmente con datos en forma de tablas (dataframes), facilitando tareas como leer archivos, limpiar datos, realizar cálculos y resumir información.

---

## ¿Para qué sirve Pandas?

- Leer y escribir datos en diferentes formatos (CSV, Excel, JSON, etc.).
- Manipular y transformar datos de manera rápida y sencilla.
- Realizar análisis estadísticos y agrupamientos.
- Filtrar y limpiar datos incompletos o erróneos.
- Preparar datos para visualización o modelado.

---

## leer un archivo CSV y mostrar los primeros datos

```python
import pandas as pd

# Cargar datos desde un archivo CSV
df = pd.read_csv('datos.csv')

# Mostrar las primeras 5 filas
print(df.head())
