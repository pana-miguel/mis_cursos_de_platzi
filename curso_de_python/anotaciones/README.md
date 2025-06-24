# 🐍 Anotaciones en Python

## 📌 ¿Qué son?

Las **anotaciones** en Python son una forma de agregar **información sobre los tipos de datos** que se espera usar en variables, parámetros de funciones o valores de retorno.

> ⚠️ No afectan directamente el comportamiento del programa, pero son muy útiles para documentar, depurar y trabajar con herramientas de análisis estático como `mypy`.

---

## 🎯 ¿Para qué sirven?

- ✅ Hacer el código más **legible** y fácil de entender.
- ✅ Mejorar el **autocompletado** y sugerencias en editores de texto.
- ✅ Detectar errores con herramientas como `mypy` o linters.
- ✅ Facilitar el trabajo en equipo y mantener una base de código clara.

---

## 🧠 Ejemplos de tipos de anotaciones

### 1. Tipos simples

```python
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}"
```

### 2. Listas

```python
from typing import List

def promedio(numeros: List[float]) -> float:
    return sum(numeros) / len(numeros)
```

### 3. Diccionarios

```python
from typing import Dict

def contar_ventas(ventas: Dict[str, int]) -> int:
    return sum(ventas.values())
```

### 4. Tipos opcionales (pueden ser `None`)

```python
from typing import Optional

def obtener_nombre(nombre: Optional[str]) -> str:
    return nombre or "Desconocido"
```

### 5. Funciones que no devuelven nada

```python
def mostrar_mensaje(mensaje: str) -> None:
    print(mensaje)
```

---

## ❓ Preguntas rápidas

| Pregunta                    | Respuesta                                                        |
|----------------------------|------------------------------------------------------------------|
| ¿Qué son?                  | Marcas que indican tipos de datos esperados.                    |
| ¿Para qué sirven?          | Para documentar, evitar errores y mejorar el editor.             |
| ¿Es obligatorio usarlas?   | No, son opcionales.                                              |
| ¿Python las usa directamente? | No, pero puedes usar herramientas que las aprovechen.            |

---

## ✅ Recomendación

Si trabajas en proyectos más grandes o colaborativos, usar anotaciones te ayuda a mantener el código más limpio, claro y menos propenso a errores.
