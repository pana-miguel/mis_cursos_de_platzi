# 🐍 Funciones en Python

## 📘 ¿Qué es una función?

Una **función** en Python es un bloque de código reutilizable que realiza una tarea específica.  
Se define una sola vez y se puede **llamar** las veces que sea necesario.

> Una función ayuda a **organizar el código**, hacerlo más **legible** y **evitar repetición**.

---

## 🛠️ ¿Para qué sirven las funciones?

- **Reutilizar código** sin escribirlo varias veces.
- **Organizar** programas grandes en partes pequeñas.
- **Facilitar mantenimiento** y depuración.
- **Mejorar legibilidad**.
- **Reducir errores** por repetición de código.

---

## ⚙️ Sintaxis básica

```python
def nombre_funcion(parámetros):
    """Docstring: Descripción breve de la función."""
    # Bloque de código
    return valor
```

# Ejemplo 1: Función simple sin parámetros

```python
python
Copiar
Editar
def saludar():
    """Muestra un saludo por consola."""
    print("Hola, bienvenido a Python!")

saludar()
```

# Resultado 

```python
Hola, bienvenido a Python!
```