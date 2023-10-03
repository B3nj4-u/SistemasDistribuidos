FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY server.py .
COPY ClienteSeExime.py .
COPY ClienteParaExamen.py .

# Instalar las dependencias necesarias
RUN pip install rpyc

# Exponer el puerto
EXPOSE 12345

# Comando para ejecutar el servidor
CMD ["python", "server.py"]