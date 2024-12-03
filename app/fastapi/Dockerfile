# Utiliser une image Windows avec Python 3.9 déjà installé
FROM mcr.microsoft.com/windows-cssc/python:3.9-servercore-ltsc2022

# Définir le répertoire de travail dans le conteneur
WORKDIR /app/fastapi

# Copier le fichier requirements.txt pour installer les dépendances
COPY app/fastapi/requirements.txt /app/fastapi/requirements.txt

# Installer les dépendances Python
RUN python -m pip install --no-cache-dir -r /app/fastapi/requirements.txt

# Copier le script FastAPI dans le conteneur
COPY app/fastapi/fast.py /app/fastapi/fast.py

# Copier le dossier 'data' depuis la racine du projet vers le conteneur
COPY data /app/fastapi/data

# Définir un port par défaut si PORT n'est pas défini
ENV PORT=8000

# Lancer le serveur Uvicorn avec l'app FastAPI
CMD ["uvicorn", "fast:app", "--host=0.0.0.0", "--port", "8000"]