# Imagen base oficial de Python
FROM python:3.11

# Evitar archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements.txt e instalar dependencias
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar el resto del proyecto
COPY . /app/

# Comando de arranque
CMD ["gunicorn", "tienda.wsgi:application", "--bind", "0.0.0.0:8000"]
