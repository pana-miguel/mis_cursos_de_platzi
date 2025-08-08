# Manejo de Archivos en Python y Visualización con Matplotlib

Este documento cubre los conceptos básicos para **leer y escribir archivos en Python** junto con una introducción a la librería **Matplotlib** para visualizar datos de manera gráfica.

---

## 📂 Manejo de Archivos en Python

Python facilita la lectura y escritura de archivos con la función `open()` y el uso del contexto `with` para asegurar el cierre automático del archivo.

### Modos comunes de apertura

- `"r"`: Leer archivo (por defecto).
- `"w"`: Escribir archivo (sobrescribe si existe).
- `"a"`: Añadir contenido al final.
- `"b"`: Modo binario (ej. `"rb"` o `"wb"`).
- `"x"`: Crear archivo nuevo (falla si existe).

### Leer archivos

```python
with open("datos.txt", "r") as f:
    contenido = f.read()
    print(contenido)
```

### Leer línea a línea

```python
with open("datos.txt", "r") as f:
    for linea in f:
        print(linea.strip())
```

###Escribir archivos

```python
with open("salida.txt", "w") as f:
    f.write("Hola, mundo!\n")
```

## 📊 Visualización de Datos con Matplotlib
Matplotlib es una biblioteca muy popular para crear gráficos y visualizar datos en Python.

###Ejemplo básico: graficar una lista de valores

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.title("Ejemplo de gráfico simple")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
```
### Leer datos desde un archivo y graficar
Supongamos que tienes un archivo datos.txt con datos numéricos separados por líneas:

```python
# Leer datos desde archivo
with open("datos.txt", "r") as f:
    datos = [float(linea.strip()) for linea in f]

# Graficar
plt.plot(datos)
plt.title("Datos desde archivo")
plt.show()
```

# Resumen
- Usa open() con with para manejar archivos de forma segura.
- Lee y escribe archivos en modo texto o binario según necesidad.
- Matplotlib permite crear gráficos desde listas, arrays o datos leídos de archivos.
- Combinar manejo de archivos con Matplotlib es muy útil para análisis de datos.

