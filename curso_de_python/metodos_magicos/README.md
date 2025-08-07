# ✨ Métodos Mágicos en Python

## 📖 ¿Qué son?
Los **métodos mágicos** (o *special methods*) en Python son funciones especiales que comienzan y terminan con **doble guion bajo** (`__metodo__`).  
Se usan para definir comportamientos personalizados de los objetos, como la inicialización, la representación en cadena, las operaciones aritméticas, la comparación, etc.

---

## 🎯 ¿Para qué sirven?
- Controlar cómo se comporta un objeto con operadores (`+`, `-`, `*`, etc.).
- Personalizar la creación, inicialización y destrucción de objetos.
- Definir cómo se comparan, representan o iteran los objetos.
- Integrar clases con las funciones y estructuras nativas de Python.

---

## 📋 Lista de métodos mágicos comunes

### 🏗️ Creación y ciclo de vida del objeto
- `__new__` → Crea una nueva instancia de la clase.
- `__init__` → Inicializa la instancia recién creada.
- `__del__` → Destructor del objeto (se llama antes de eliminarlo).

---

### 🖊️ Representación de objetos
- `__str__` → Representación legible para humanos.
- `__repr__` → Representación oficial para desarrolladores.
- `__format__` → Formateo con `format()` y f-strings.
- `__bytes__` → Conversión a bytes.
- `__hash__` → Devuelve el hash del objeto.

---

### 🔍 Comparación y evaluación
- `__eq__` → Igualdad (`==`).
- `__ne__` → Desigualdad (`!=`).
- `__lt__` → Menor que (`<`).
- `__le__` → Menor o igual (`<=`).
- `__gt__` → Mayor que (`>`).
- `__ge__` → Mayor o igual (`>=`).
- `__bool__` → Valor booleano del objeto.

---

### ➕ Operaciones aritméticas
- `__add__` → Suma (`+`).
- `__sub__` → Resta (`-`).
- `__mul__` → Multiplicación (`*`).
- `__truediv__` → División real (`/`).
- `__floordiv__` → División entera (`//`).
- `__mod__` → Módulo (`%`).
- `__pow__` → Potencia (`**`).
- `__matmul__` → Producto matricial (`@`).

---

### 🔄 Operaciones aritméticas inversas
- `__radd__`, `__rsub__`, `__rmul__`, `__rtruediv__`, etc. → Operaciones cuando el operando izquierdo no es compatible.

---

### 🧮 Operadores de asignación
- `__iadd__` → Suma y asigna (`+=`).
- `__isub__` → Resta y asigna (`-=`).
- `__imul__` → Multiplica y asigna (`*=`).
- `__itruediv__` → Divide y asigna (`/=`).

---

### 📦 Acceso a elementos
- `__getitem__` → Obtener un elemento (`obj[key]`).
- `__setitem__` → Asignar un valor (`obj[key] = valor`).
- `__delitem__` → Eliminar un elemento (`del obj[key]`).
- `__contains__` → Operador `in`.

---

### 🔁 Iteración
- `__iter__` → Retorna un iterador.
- `__next__` → Retorna el siguiente elemento.

---

### 🛠️ Atributos
- `__getattr__` → Acceso a atributos inexistentes.
- `__getattribute__` → Acceso a cualquier atributo.
- `__setattr__` → Asignación de atributos.
- `__delattr__` → Eliminación de atributos.
- `__dir__` → Lista de atributos disponibles.

---

### 🏭 Contexto y gestión de recursos
- `__enter__` → Entrar en un contexto (`with`).
- `__exit__` → Salir de un contexto.

---

### ⚡ Sobrecarga de llamadas y conversión
- `__call__` → Permite llamar un objeto como función.
- `__len__` → Longitud (`len(obj)`).
- `__reversed__` → Reversión (`reversed(obj)`).
- `__index__` → Representación entera para índices.
- `__int__`, `__float__`, `__complex__` → Conversión a tipos numéricos.
- `__round__` → Redondeo (`round(obj)`).
- `__trunc__`, `__floor__`, `__ceil__` → Operaciones matemáticas de truncado y redondeo.

---

## ✅ Conclusión
Los métodos mágicos permiten que las clases personalicen su comportamiento y se integren de forma natural con las funcionalidades y operadores de Python.
