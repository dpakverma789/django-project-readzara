#!/bin/bash

echo "Building the project..."
python pip install -r requirements.txt

echo "Make Migration..."
python3.8.10 manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect Static..."
python manage.py collectstatic --noinput --clear