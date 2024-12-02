# Utiliser une image Windows avec Python 3.9 déjà installé
FROM mcr.microsoft.com/windows-cssc/python:3.9-servercore-ltsc2022

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

# Exposer le port 8501 pour Streamlit
EXPOSE 8501

# Commande pour démarrer Streamlit
CMD ["streamlit", "run", "script_API.py", "--server.address", "0.0.0.0", "--server.port", "8501"]