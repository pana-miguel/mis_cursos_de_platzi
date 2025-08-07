# 📦 Manejo de Paquetes en Python

## 📖 ¿Qué es un paquete en Python?
En Python, un **paquete** es una forma de organizar y estructurar módulos en carpetas, permitiendo que el código sea más ordenado, reutilizable y fácil de mantener.  
Un paquete no es más que una carpeta que contiene un archivo especial llamado `__init__.py` (puede estar vacío o contener código de inicialización).

> 🔹 Un **módulo** es un solo archivo `.py` que contiene código.  
> 🔹 Un **paquete** es un directorio que agrupa varios módulos y/o subpaquetes.

---

## 🎯 ¿Para qué sirve?
Los paquetes permiten:
- Organizar proyectos grandes en partes más pequeñas y manejables.
- Evitar conflictos de nombres en funciones y clases.
- Reutilizar código en diferentes proyectos.
- Facilitar la importación de múltiples módulos relacionados.

---

## 📂 Estructura básica de un paquete
Ejemplo de un paquete llamado `mi_paquete`:


---

## ⚙️ Cómo crear y usar un paquete

### 1️⃣ Crear un paquete
```python
# mi_paquete/modulo1.py
def saludar():
    return "¡Hola desde modulo1!"

# mi_paquete/modulo2.py
def despedir():
    return "Adiós desde modulo2"
```


con los paquetes que vallamos poniendo en nuestro espacio de trabajo si estan en la misma altura con respecto a carpetas o archivos se puede llamar de forma simple como **from .modulo1 import saludar** y asi segun donde tengamos nuestro archivo el . al inicio representa la primera carpeta de donde estemos trabajando y eso significa que modulo 1 esta dentro de esta. 