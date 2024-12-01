# Utiliser une image Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app/fastapi

# Copier le fichier requirements.txt pour installer les dépendances
COPY app/fastapi/requirements.txt /app/fastapi/requirements.txt
RUN pip install --no-cache-dir -r /app/fastapi/requirements.txt

# Copier le script FastAPI dans le conteneur
COPY app/fastapi/fast.py /app/fastapi/fast.py

# Copier le dossier 'data' pour les modèles dans le conteneur
COPY data /app/fastapi/data

# Exposer le port 8000 pour FastAPI
EXPOSE 8000

# Commande pour démarrer Uvicorn et exécuter FastAPI
CMD ["uvicorn", "fast:app", "--host=0.0.0.0", "--port=8000"]
