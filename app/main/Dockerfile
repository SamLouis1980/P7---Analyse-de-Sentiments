# Utiliser une image Windows avec Python 3.9
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur (répertoire racine du projet)
WORKDIR /app/main

# Assurer que pip est installé
RUN python -m ensurepip --upgrade
RUN python -m pip install --upgrade pip

# Copier le fichier requirements.txt pour installer les dépendances
COPY ./main/requirements.txt /app/main/requirements.txt

# Installer les dépendances Python
RUN python -m pip install --no-cache-dir -r /app/main/requirements.txt

# Copier le script Streamlit dans le conteneur
COPY /app/main/script_API.py /app/main/script_API.py

# Définir un port par défaut si PORT n'est pas défini
ENV PORT=8501

# Lancer Streamlit
CMD ["streamlit", "run", "script_API.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
