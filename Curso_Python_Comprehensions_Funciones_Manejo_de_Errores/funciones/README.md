
# 📘 Funciones en Python

## 📌 ¿Qué es una función?
Una **función** en Python es un bloque de código reutilizable que se define una vez y se puede ejecutar múltiples veces.  
Se utiliza para organizar el código, evitar repeticiones y mejorar la legibilidad.

---

## 🛠️ Características
- **Reutilizables**: Evitan escribir el mismo código varias veces.
- **Organizadas**: Separan la lógica en bloques.
- **Parámetros y argumentos**: Permiten recibir datos.
- **Retorno de valores**: Pueden devolver resultados.

---

## 🔹 Sintaxis básica
```python
def nombre_funcion(parametros):
    # Bloque de código
    return valor
```

---

## 📝 Tipos de funciones
1. **Funciones sin parámetros y sin retorno**  
   Ejecutan código sin recibir ni devolver datos.
2. **Funciones con parámetros**  
   Reciben datos para trabajar.
3. **Funciones con valor de retorno**  
   Devuelven un resultado al llamador.
4. **Funciones con parámetros por defecto**  
   Usan valores predefinidos si no se pasan argumentos.

---

## 📂 Uso de funciones
Las funciones se usan para:
- Dividir programas grandes en partes pequeñas.
- Evitar duplicación de código.
- Hacer que el código sea más fácil de mantener.

---

## 🔄 Funciones lambda (anónimas)
Son funciones pequeñas de una sola línea que no necesitan nombre.
```python
cuadrado = lambda x: x**2
print(cuadrado(5))  # 25
```

---

## 🎯 Ejemplo práctico
```python
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Miguel"))
```
