# 🚗 Programación Orientada a Objetos en Python – Ejemplo: Carro

La **Programación Orientada a Objetos (POO)** es un paradigma que organiza el código en torno a **objetos**, que son instancias de **clases**.  
Cada objeto tiene:

- **Atributos** → Representan características o propiedades.
- **Métodos** → Representan comportamientos o acciones.

En Python, la POO ayuda a escribir código más organizado, reutilizable y fácil de mantener.

---

## 🛠 Conceptos Clave

1. **Clase** → Plantilla o modelo que define atributos y métodos.
2. **Objeto** → Instancia creada a partir de una clase.
3. **Atributos** → Variables que almacenan el estado de un objeto.
4. **Métodos** → Funciones dentro de la clase que definen el comportamiento.
5. **Constructor (`__init__`)** → Método especial que inicializa el objeto.
6. **Encapsulación** → Control de acceso a los atributos.
7. **Herencia** → Capacidad de una clase de heredar atributos y métodos de otra.
8. **Polimorfismo** → Capacidad de usar un mismo método con diferentes comportamientos.

---

## 📄 Ejemplo: Clase `Carro`

```python
class Carro:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El {self.marca} {self.modelo} está arrancando.")

    def detener(self):
        print(f"El {self.marca} {self.modelo} se ha detenido.")

# Crear un objeto (instancia de la clase Carro)
mi_carro = Carro("Toyota", "Corolla", "Rojo")

# Usar métodos
mi_carro.arrancar()
mi_carro.detener()
```
# Resultado

```python
El Toyota Corolla está arrancando.
El Toyota Corolla se ha detenido.
```