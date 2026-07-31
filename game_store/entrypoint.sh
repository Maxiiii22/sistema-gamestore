#!/bin/sh
set -e
# Verificamos si no existe la base de datos dentro de /app/data
if [ ! -f /app/data/db.sqlite3 ]; then
    echo "Reconstruyendo base de datos desde la plantilla local..."
    mkdir -p /app/data                     # Asegura que la carpeta exista en caliente
    cp /tmp/db_plantilla.sqlite3 /app/data/db.sqlite3
fi
echo "Ejecutando Migraciones a la BD SQLite..."
python manage.py migrate --noinput
echo "Migraciones completadas." 
echo "Sistema listo."
exec "$@"