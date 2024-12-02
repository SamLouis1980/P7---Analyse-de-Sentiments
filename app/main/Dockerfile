# Utiliser une image Windows avec Python déjà installé
FROM mcr.microsoft.com/windows/python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app/main

# Copier le fichier requirements.txt pour installer les dépendances
COPY app/main/requirements.txt /app/main/requirements.txt
RUN pip install --no-cache-dir -r /app/main/requirements.txt

# Copier le script Streamlit dans le conteneur
COPY script_API.py /app/main/script_API.py

# Commande pour démarrer Streamlit
CMD ["streamlit", "run", "script_API.py", "--server.address", "0.0.0.0", "--server.port", "$PORT"]