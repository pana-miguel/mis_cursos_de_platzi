# Introducción a pip y Entornos Virtuales en Python

En este curso se utilizo **pip** y los **entornos virtuales** en Python, además de los comandos básicos para usarlos. 

Esto es fundamental para gestionar correctamente las librerías y evitar conflictos entre proyectos.

---

## Enlaces a ejemplos prácticos

esots son ejercisios realizados en el curso de platzi

- [charts con docker](./charts_con_docker/README.md)  
- [flujo de trabajo en python](./flujo_trabajo_python/README.md)  
- [lectura de archivos con pandas](./lectura_pandas/README.md)  
- [web Serves](./web_serves/README.md)  

---

## ¿Qué es pip?

**pip** es el gestor de paquetes oficial de Python. Permite instalar, actualizar y desinstalar librerías y dependencias que tus proyectos necesiten.

---

## Comandos básicos de pip

### Instalar una librería:  

```bash
pip install nombre_paquete
```
### Instalar desde un archivo requirements.txt:

```bash
pip install -r requirements.txt
```

### Listar las librerías instaladas:

```bash
pip list
```

### Actualizar pip:

```bash
pip install --upgrade pip
```

## ¿Qué es un entorno virtual?
Un entorno virtual es un espacio aislado dentro de tu sistema donde puedes instalar librerías de Python sin afectar el sistema global ni otros proyectos. Esto evita conflictos de versiones y facilita la gestión de dependencias.

## Crear y usar un entorno virtual

### Crear un entorno virtual (por ejemplo, llamado venv):

```bash
python -m venv venv
```

### Activar el entorno virtual en linux:

```bash
source venv/bin/activate
```

Cuando el entorno está activo, instala las librerías con pip y se instalarán sólo ahí.

### Para salir o desactivar el entorno:

```bash
deactivate
```