# Introducción a Docker

Docker es una plataforma que permite crear, desplegar y ejecutar aplicaciones dentro de **contenedores**.  
Los contenedores son entornos ligeros y portátiles que incluyen todo lo necesario para que una aplicación funcione, como código, librerías y dependencias.

---

## ¿Para qué sirve Docker?

- Facilita la **portabilidad** de las aplicaciones entre diferentes sistemas y entornos.
- Asegura que la aplicación funcione igual en desarrollo, pruebas y producción.
- Simplifica la gestión de dependencias y configuración.
- Permite ejecutar múltiples aplicaciones aisladas en un solo servidor.

---

## Recordatorio importante

En esta carpeta es necesario descargar y mantener actualizado el archivo `requirements.txt`, que contiene las librerías Python necesarias para el proyecto. Este archivo es usado para instalar las dependencias dentro del contenedor Docker.

Para instalar las dependencias dentro del contenedor o entorno virtual, usa:

```bash
pip install -r requirements.txt
```



# Introducción a Docker

en este curso tambien se vio el uso de doker asi que aqui dejo mas informacion sobre el mismo

Docker es una plataforma que permite crear, distribuir y ejecutar aplicaciones dentro de contenedores. Un contenedor es un paquete liviano y portátil que incluye todo lo necesario para que una aplicación funcione: el sistema operativo, las librerías, el código y sus dependencias.

Docker es una forma de organizar las versiones y dependencias de un proyecto de manera muy similar a cómo funciona WSL cuando usamos entornos virtuales de Python como `venv`. Es decir, podemos mantener dentro de un proyecto una versión específica de Python junto con todas las versiones de las bibliotecas que utilizamos, aisladas y sin interferir con otros proyectos o el sistema global.

---

## Archivos clave en un proyecto Dockerizado

En un proyecto que usa Docker usualmente encontramos dos archivos principales:

- **Dockerfile:** Define cómo se construye la imagen de Docker, qué sistema operativo base usar, qué dependencias instalar, y qué comandos ejecutar al iniciar el contenedor.

- **docker-compose.yml:** Permite definir y orquestar varios servicios (contenedores) que componen una aplicación, configurando redes, volúmenes, variables de entorno, entre otros.

Si quieres conocer más detalles sobre estos archivos, puedes revisar:

- [Documentación Dockerfile](https://docs.docker.com/engine/reference/builder/)
- [Documentación docker-compose.yml](https://docs.docker.com/compose/compose-file/)

---

## Requisitos previos

Antes de empezar, debes tener **Docker Desktop** instalado en tu computador. Esto te permite usar Docker y Docker Compose fácilmente con una interfaz gráfica y también desde la terminal.

Puedes descargar Docker Desktop desde aquí:  
[https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

---

## Pasos para trabajar con Docker en tu proyecto

Asumiendo que ya estás ubicado en la carpeta raíz de tu proyecto (donde están el `Dockerfile` y `docker-compose.yml`), sigue estos comandos en orden:

---

### 1. Construir la imagen Docker

```bash
docker compose build
```

- **Qué hace:** Lee el `Dockerfile` y construye una imagen con todo lo necesario para tu aplicación.  
- Este paso instala dependencias, copia tu código y prepara el entorno dentro del contenedor.

---

### 2. Levantar los servicios y contenedores

```bash
docker compose up
```

- **Qué hace:** Crea y arranca los contenedores definidos en `docker-compose.yml`.  
- Muestra en la consola la salida (logs) de la aplicación.  
- Para detener el proceso presiona `Ctrl+C`.

Si quieres que corra en segundo plano (background):

```bash
docker compose up -d
```

---

### 3. Ver qué contenedores están corriendo

```bash
docker ps
```

- **Qué hace:** Muestra una lista de los contenedores activos, con su nombre, estado y puertos expuestos.

---

### 4. Entrar a un contenedor en ejecución

```bash
docker exec -it <nombre_del_contenedor> bash
```

- **Qué hace:** Abre una terminal interactiva dentro del contenedor, para que puedas ejecutar comandos manualmente o revisar archivos.  
- Reemplaza `<nombre_del_contenedor>` con el que obtuviste en el paso anterior con `docker ps`.

---

## ¿Por qué usar Docker? Beneficios clave

- **Consistencia:** Asegura que tu aplicación siempre corra igual, sin importar dónde esté (tu máquina, otro equipo, o la nube).  
- **Aislamiento:** Cada contenedor es un ambiente separado; tus versiones de Python y librerías no afectan otros proyectos ni el sistema operativo.  
- **Portabilidad:** Las imágenes Docker se pueden mover fácilmente entre máquinas o servidores.  
- **Facilita despliegues:** Simplifica subir tu aplicación a producción o a la nube sin complicaciones de dependencias.  
- **Escalabilidad:** Docker Compose y Kubernetes permiten orquestar múltiples contenedores para aplicaciones complejas.
