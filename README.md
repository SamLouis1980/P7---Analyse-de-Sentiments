#  Analyse de sentiments sur Twitter – Air Paradis

## Contexte

Dans le cadre d'une mission pour **Air Paradis**, compagnie aérienne active sur les réseaux sociaux, le cabinet **MIC (Marketing Intelligence Consulting)** a été chargé de développer un prototype d’IA permettant de **prédire le sentiment associé à un tweet**.  
Ce projet vise à anticiper les bad buzz potentiels, en s’appuyant sur des données Open Source, et à présenter une **démarche complète intégrant les principes du MLOps**.

Le livrable principal est une **API déployée sur le Cloud** qui reçoit un tweet et renvoie un score de sentiment, intégrée à une **interface de test locale**.

## Objectif

- Développer trois approches de modélisation :
  - Un modèle classique simple (Logistic Regression, Naive Bayes…)
  - Un modèle sur mesure avancé (réseaux de neurones profonds)
  - Une approche basée sur BERT pour comparer les performances
- Intégrer une gestion des expérimentations via **MLFlow**
- Déployer le modèle avancé sous forme d’**API dans le Cloud** (Azure WebApp, Heroku, etc.)
- Créer une **interface locale** pour interagir avec l’API (Streamlit ou notebook)
- Implémenter une démarche **MLOps complète** avec suivi de la performance en production (traces et alertes via **Azure Application Insight**)
- Produire un **article de blog** résumant la démarche et les enseignements

## Technologies utilisées

- `pandas`, `numpy`, `matplotlib`, `seaborn`, `re`, `contractions`, `nltk`
- `scikit-learn`, `xgboost`, `lightgbm`, `tensorflow`, `keras`, `torch`
- `transformers`, `BERT`, `Word2Vec`, `FastText`, `USE`
- `MLFlow`, `pyngrok`, `Streamlit`, `Azure Application Insight`
- `Flask` ou `FastAPI` (pour l’API de prédiction)
- `Git`, `GitHub`, `subprocess`, `API REST`, `tests unitaires`

## Organisation des Fichiers
Voici la structure du projet et une description des différents fichiers et répertoires :

### Livrables
- dossier_code/                          # Scripts de préparation, traitement et modélisation
- API.py                                 # API de prédiction déployée dans le Cloud
- interface_test_API.py                  # Interface locale (Streamlit / notebook) pour tester l'API
- notebook_modelisation.ipynb            # Notebook de modélisation avec tracking MLFlow
- blog.pdf                               # Article de blog (~2000 mots) sur la démarche
- presentation.pptx                      # Présentation complète de la mission

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

### Tests Unitaires
Les tests unitaires sont définis dans le répertoire tests/ :

API FastAPI : test_fast.py

Interface Streamlit : test_script_API.py

Pour exécuter les tests et générer les résultats avec Allure :

pytest --alluredir=allure-results

