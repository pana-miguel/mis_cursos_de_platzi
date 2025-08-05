# 🧩 Módulos en Python

## 📘 ¿Qué es un módulo?

Un **módulo en Python** es un archivo que contiene definiciones de funciones, clases o variables que puedes reutilizar en otros archivos de código.

> Es una forma de **organizar y reutilizar el código**.

Un módulo es simplemente **un archivo `.py`**. Por ejemplo, `matematica.py` puede ser un módulo.

---

## ✅ ¿Para qué sirve un módulo?

- Reutilizar código sin copiar y pegar.
- Organizar programas grandes en archivos más pequeños y manejables.
- Separar funcionalidades (por ejemplo: lógica, operaciones matemáticas, entrada/salida, etc.).
- Compartir tu código con otros.

---

## 🛠️ Cómo se crea un módulo en Python

Simplemente, creas un archivo `.py` con funciones, clases o variables.

### 📄 Ejemplo: `saludos.py`

```python
# saludos.py

def saludar(nombre):
    return f"Hola, {nombre}!"

def despedir(nombre):
    return f"Adiós, {nombre}!"

