# Utiliser une image Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt pour installer les dépendances
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le script FastAPI dans le conteneur
COPY fast.py /app/fast.py

# Exposer le port 8000 pour FastAPI
EXPOSE 8000

# Commande pour démarrer Uvicorn et exécuter FastAPI
CMD ["uvicorn", "fast:app", "--host=0.0.0.0", "--port=8000"]
