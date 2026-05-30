#!/bin/sh
set -e

# crea el proyecto si no existe
if [ ! -f "manage.py" ]; then
    echo "Nuevo proyecto Django..."
    django-admin startproject backend .
fi

# intenta crear migraciones
python manage.py makemigrations --noinput || true

# ejecuta migrate
echo "Migraciones..."
python manage.py migrate --noinput

# crea superusuario si no existe
export DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:-admin}
export DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-admin@example.com}
export DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:-adminpass}

echo "Creando superusuario..."
python manage.py shell -c "from django.contrib.auth import get_user_model; import os; User=get_user_model(); u=os.getenv('DJANGO_SUPERUSER_USERNAME'); e=os.getenv('DJANGO_SUPERUSER_EMAIL'); p=os.getenv('DJANGO_SUPERUSER_PASSWORD'); User.objects.filter(username=u).exists() or User.objects.create_superuser(u, e, p)"

# levanta el servidor
echo "Iniciando Django..."
exec python manage.py runserver 0.0.0.0:8000