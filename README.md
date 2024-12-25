# Projet P7 - Analyse de Sentiments

## Description
Ce projet vise à développer une solution d'analyse de sentiments basée sur des tweets. 
Les principales étapes incluent :
- Développement d'une API pour la prédiction de sentiments.
- Mise en place d'une interface Streamlit pour tester l'API et collecter les retours utilisateurs.
- Conteneurisation et déploiement avec Docker et Heroku.
- Suivi des performances et gestion des feedbacks.

---

## Organisation des Fichiers
Voici la structure du projet et une description des différents fichiers et répertoires :

### Racine du Projet
- **`Procfile`** : Fichier de configuration pour déploiement Heroku.
- **`docker-compose.yml`** : Orchestration des conteneurs (API et interface).
- **`runtime.txt`** : Spécifie la version de Python pour le déploiement Heroku.
- **`heroku.yml`** : Configuration pour le déploiement via Heroku.
- **`allure-results/`** : Contient les fichiers de résultats générés par Pytest pour l'exécution des tests unitaires.

### Dossier `app/`
- **`fastapi/`** : Contient les fichiers liés à l'API FastAPI.
  - **`Dockerfile`** : Fichier de conteneurisation pour l'API.
  - **`Procfile`** : Configuration pour exécuter l'API avec Heroku.
  - **`requirements.txt`** : Dépendances nécessaires pour l'API.
  - **`fast.py`** : Code de l'API FastAPI pour la prédiction de sentiments.

- **`main/`** : Contient les fichiers de l'interface utilisateur Streamlit.
  - **`Dockerfile`** : Fichier de conteneurisation pour l'interface.
  - **`script_API.py`** : Interface Streamlit pour tester l'API.
  - **`requirements.txt`** : Dépendances nécessaires pour l'interface.

### Dossier `data/`
- **`feedbacks.csv`** : Fichier contenant les retours utilisateurs collectés via l'interface Streamlit.
- **`log_reg_model.pkl`** : Modèle de régression logistique sauvegardé au format pickle.
- **`tfidf_vectorizer.pkl`** : Modèle TF-IDF vectorizer sauvegardé au format pickle.

### Dossier `tests/`
- **`test_fast.py`** : Script pour tester les fonctionnalités de l'API FastAPI.
- **`test_script_API.py`** : Script pour tester l'interface Streamlit.

---

## Instructions pour Exécuter le Projet

### Option 1 : Exécution Locale
1. Cloner le dépot Github :
   ```bash
   git clone <[lien_du_dépôt](https://github.com/SamLouis1980/P7---Analyse-de-Sentiments)>
   cd P7---Analyse-de-Sentiments

2. Installer les dépendances
   cd app/fastapi
   pip install -r requirements.txt
   cd app/main
   pip install -r requirements.txt

3. Exécuter l'API
   cd app/fastapi
   uvicorn fast:app --reload

4. Lancer l'interface streamlit
   cd app/main
   streamlit run script_API.py

### Option 2 : Exécution avec Docker
1. docker-compose up --build
2. Accéder à l'API et l'interface :
   API FastAPI : http://localhost:8000
   Interface Streamlit : http://localhost:8501

### Dépendances
Les principales bibliothèques utilisées dans ce projet incluent :

numpy
pandas
matplotlib
scikit-learn
tensorflow
transformers
mlflow
fastapi
streamlit
pytest

Toutes les dépendances peuvent être installées à partir des fichiers requirements.txt correspondants.

### Tests Unitaires
Les tests unitaires sont définis dans le répertoire tests/ :
API FastAPI : test_fast.py
Interface Streamlit : test_script_API.py
Pour exécuter les tests et générer les résultats avec Allure :
pytest --alluredir=allure-results

### Contact
Pour toute question ou assistance, veuillez me contacter à : [samylouis.engineer@gmail.com]
