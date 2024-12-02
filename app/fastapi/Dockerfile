# Utiliser une image de base Windows Server Core
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Définir le répertoire de travail dans le conteneur
WORKDIR /app/fastapi

# Installer Python (si nécessaire, Windows Server Core ne le fournit pas par défaut)
RUN powershell -Command \
    Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.7/python-3.9.7.exe -OutFile python-installer.exe; \
    Start-Process -Wait -FilePath python-installer.exe /quiet InstallAllUsers=1 PrependPath=1; \
    Remove-Item -Force python-installer.exe

# Vérifier que Python est bien installé
RUN python --version

# Assurer que pip est installé et à jour
RUN python -m ensurepip --upgrade
RUN python -m pip install --upgrade pip

# Copier le fichier requirements.txt pour installer les dépendances
COPY requirements.txt /app/fastapi/requirements.txt

# Installer les dépendances Python
RUN pip install --no-cache-dir -r /app/fastapi/requirements.txt

# Copier le script FastAPI dans le conteneur
COPY app/fastapi/fast.py /app/fastapi/fast.py

# Copier le dossier 'data' depuis la racine du projet vers le conteneur
COPY data /app/fastapi/data

# Exposer le port 8000 pour FastAPI
EXPOSE 8000

# Commande pour démarrer Uvicorn et exécuter FastAPI
CMD ["uvicorn", "fast:app", "--host=0.0.0.0", "--port=8000"]
