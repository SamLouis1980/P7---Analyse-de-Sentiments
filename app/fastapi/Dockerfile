# Utiliser une image Windows avec Python 3.9 déjà installé
FROM mcr.microsoft.com/windows-cssc/python:3.9-servercore-ltsc2022

# Définir le répertoire de travail dans le conteneur
WORKDIR /app/fastapi

# Copier le fichier requirements.txt pour installer les dépendances
COPY requirements.txt /app/fastapi/requirements.txt

# Installer les dépendances Python
RUN python -m pip install --no-cache-dir -r /app/fastapi/requirements.txt

# Copier le script FastAPI dans le conteneur
COPY fast.py /app/fastapi/fast.py

# Copier le dossier 'data' depuis la racine du projet vers le conteneur
COPY data /app/fastapi/data

CMD ["uvicorn", "fast:app", "--host=0.0.0.0", "--port=${PORT}"]
