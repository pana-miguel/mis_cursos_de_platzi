# ¿Qué es un Web Server?

Un **Web Server** (servidor web) es un software o hardware que recibe solicitudes (requests) desde un navegador u otro cliente y responde enviando recursos web, como páginas HTML, imágenes, archivos CSS, JavaScript, o datos generados dinámicamente.

---

## Funciones principales

- **Recibir solicitudes HTTP/HTTPS:** Atiende las peticiones que llegan a través de internet o una red local.
- **Servir contenido web:** Envía archivos estáticos o ejecuta aplicaciones para generar contenido dinámico.
- **Gestionar conexiones:** Maneja múltiples conexiones simultáneas de usuarios.
- **Seguridad:** Implementa protocolos para proteger la información y controlar el acceso.

---

## Ejemplos populares

- Apache HTTP Server
- Nginx
- Microsoft IIS
- Servidores embebidos en frameworks como Flask o Django (Python)

---

## ¿Para qué sirve un Web Server?

Permite que los usuarios accedan a sitios web y aplicaciones web de manera rápida y confiable, haciendo posible la comunicación entre clientes (navegadores) y servidores donde se alojan los recursos.

---

## Ejemplo simple en Python con Flask

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola, mundo! Este es un Web Server simple.'

if __name__ == '__main__':
    app.run(debug=True)
```

Este código crea un servidor web básico que responde con un mensaje al acceder a la raíz (/).