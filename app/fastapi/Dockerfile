# Utiliser une image de base Windows Server Core avec Python déjà inclus
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Définir le répertoire de travail dans le conteneur
WORKDIR /app/fastapi

# Installer Chocolatey (si non déjà installé) et Python 3.9
RUN powershell -Command \
    Set-ExecutionPolicy Bypass -Scope Process -Force; \
    Invoke-WebRequest https://community.chocolatey.org/install.ps1 -OutFile install.ps1; \
    PowerShell -NoProfile -ExecutionPolicy Bypass -Command "& .\install.ps1"; \
    Remove-Item -Force install.ps1; \
    choco install python --version=3.9.7 -y

# Vérification de Python
RUN python --version

# Copier le fichier requirements.txt pour installer les dépendances
COPY requirements.txt /app/fastapi/requirements.txt

# Installer les dépendances Python
RUN python -m pip install --no-cache-dir -r /app/fastapi/requirements.txt

# Copier le script FastAPI dans le conteneur
COPY app/fastapi/fast.py /app/fastapi/fast.py

# Copier le dossier 'data' depuis la racine du projet vers le conteneur
COPY data /app/fastapi/data

# Exposer le port 8000 pour FastAPI
EXPOSE 8000

# Commande pour démarrer Uvicorn et exécuter FastAPI
CMD ["uvicorn", "fast:app", "--host=0.0.0.0", "--port=8000"]
