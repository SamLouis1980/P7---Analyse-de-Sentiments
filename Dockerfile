# Utiliser une image Linux avec Python 3.9
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur (répertoire racine du projet)
WORKDIR /app

# Assurer que pip est installé
RUN python -m ensurepip --upgrade
RUN python -m pip install --upgrade pip

# Copier le fichier requirements.txt pour installer les dépendances
COPY requirements.txt /app/requirements.txt

# Installer les dépendances Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copier le script Streamlit dans le conteneur
COPY script_API.py /app/script_API.py

# Exposer le port 8501 pour Streamlit (utilisé en local, Heroku l'utilisera dynamiquement)
EXPOSE 8501

# Commande pour démarrer Streamlit avec le port dynamique sur Heroku
CMD ["streamlit", "run", "/app/script_API.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
