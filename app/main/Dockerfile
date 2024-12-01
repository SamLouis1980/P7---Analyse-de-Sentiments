# Utiliser une image Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app/main

# Copier le fichier requirements.txt pour installer les dépendances
COPY app/main/requirements.txt /app/main/requirements.txt
RUN pip install --no-cache-dir -r /app/main/requirements.txt

# Copier le script Streamlit dans le conteneur
COPY app/main/script_API.py /app/main/script_API.py

# Exposer le port 8501 pour Streamlit
EXPOSE 8501

# Commande pour démarrer Streamlit
CMD ["streamlit", "run", "script_API.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
