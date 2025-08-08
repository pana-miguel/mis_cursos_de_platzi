#definimos la version de python que vamos a usar  
FROM python:3.11 

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app 

# Copiamos el archivo de requerimientos al contenedor
COPY requerimientos.txt /app/requerimientos.txt 

# Instalamos las dependencias del proyecto
# Usamos --no-cache-dir para evitar almacenar archivos temporales de instalación y mantener la imagen ligera
# Usamos --upgrade para asegurarnos de que todas las dependencias estén actualizadas 
# definimos que el archivo de requerimientos se encuentra en /app/requerimientos.txt
RUN pip install --no-cache-dir --upgrade -r /app/requerimientos.txt 

# Copiamos el resto del código de la aplicación al contenedor
COPY . /app/ 

# Exponemos el puerto 8000 para que la aplicación sea accesible desde fuera del contenedor
# creamos un ciclo infinito para que el contenedor no se detenga inmediatamente

#CMD bash -c "while true; do sleep 1; done"


# Definimos el comando por defecto que se ejecutará al iniciar el contenedor
# En este caso, ejecutamos el archivo main.py con Python
# Esto iniciará la aplicación y la mantendrá en ejecución
#una vez se ejecute y cumpla con lo que tiene que hacer se detendra la ejecucion
CMD ["python", "main.py"]
















