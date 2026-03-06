# Una imagen ligera de Python 3.11 para poder ejecutar la aplicación y reducir el tamaño del cotenedor
FROM python:3.11-slim-bookworm

WORKDIR /app

# Instalar dependencias necesarias
RUN apt-get update && \
    apt-get install -y curl gnupg unixodbc unixodbc-dev build-essential && \
    mkdir -p /etc/apt/keyrings && \
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/keyrings/microsoft.gpg && \
    chmod 644 /etc/apt/keyrings/microsoft.gpg && \
    echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" \
        > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    apt-get install -y --no-install-recommends sqlmap && \
    apt-get install -y --no-install-recommends curl && \
    apt-get install -y --no-install-recommends iputils-ping && \
    apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "seguridad_app.main:app", "--host", "0.0.0.0", "--port", "8000"]