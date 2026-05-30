FROM python:3.12.2-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

WORKDIR /app

# instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copia el entrypoint
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# ejecuta el script al iniciar
ENTRYPOINT ["/app/entrypoint.sh"]