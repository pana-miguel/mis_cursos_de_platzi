# 📂 Manejo de Archivos en Python

## 📘 ¿Qué es el manejo de archivos?

El **manejo de archivos** en Python permite **leer, escribir, crear y modificar** archivos directamente desde un programa.  
Es esencial cuando necesitamos **guardar información**, **cargar datos** o **procesar contenido** externo.

---

## 🛠️ ¿Para qué sirve?

- **Guardar datos** de forma persistente.
- **Leer información** almacenada previamente.
- **Procesar archivos** de texto, CSV, JSON, etc.
- **Registrar logs** de un programa.
- **Automatizar tareas** de lectura y escritura.

---

## ⚙️ Sintaxis básica

```python
# Abrir un archivo
archivo = open("nombre.txt", "modo")

# Leer o escribir datos

# Cerrar archivo
archivo.close()
```

# 📌 Modos comunes de apertura

### Modo	Descripción
- "r"	Lectura (por defecto, el archivo debe existir).
- "w"	Escritura (crea o sobrescribe el archivo).
- "a"	Agregar contenido al final del archivo.
- "x"	Crear un archivo nuevo (error si ya existe).
- "b"	Modo binario (imágenes, PDFs, etc.).
- "t"	Modo texto (por defecto).