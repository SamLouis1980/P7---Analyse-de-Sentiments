# Utiliser une image Windows avec Python 3.9
mcr.microsoft.com/windows-cssc/python:3.9-servercore-ltsc2022

# Définir le répertoire de travail dans le conteneur (répertoire racine du projet)
WORKDIR /app

# Assurer que pip est installé
RUN python -m ensurepip --upgrade
RUN python -m pip install --upgrade pip

# Copier le fichier requirements.txt pour installer les dépendances
COPY app/main/requirements.txt /app/requirements.txt

# Installer les dépendances Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copier le script Streamlit dans le conteneur
COPY app/main/script_API.py /app/script_API.py

# Définir un port par défaut si PORT n'est pas défini
ENV PORT=8501

# Lancer Streamlit
CMD ["streamlit", "run", "/app/script_API.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
