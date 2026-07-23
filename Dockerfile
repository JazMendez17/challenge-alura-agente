# Dockerfile para deploy en OCI
# Usa Python slim pa' que sea ligero

FROM python:3.11-slim

WORKDIR /app

# Copiar archivos de dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer puerto
EXPOSE 8080

# Comando para correr con gunicorn (produccion)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "4", "app.app:app"]
