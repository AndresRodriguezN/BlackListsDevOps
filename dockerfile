# Empezar corriendo una imagen de python 
FROM python:3.11.1-bullseye
# Copiar requerimientos para ejecutar el programa
COPY ./src/requirements.txt /app/requirements.txt
# Cambiar de directorio de trabajo a donde esta el ejectuable del API
WORKDIR /app
# Instalar requerimientos de la app
RUN pip install -r requirements.txt
# Expone el puerto por defecto de flask
EXPOSE 5000
# Copiar el contenido del directorio actual en la imagen de docker
COPY ./src /app
# Archivo principal donde corre el API
CMD ["flask","run","--host=0.0.0.0" ]
