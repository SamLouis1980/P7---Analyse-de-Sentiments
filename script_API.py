# -*- coding: utf-8 -*-
import os
import streamlit as st
import numpy as np
import pandas as pd
import re
import nltk
import joblib  # Pour charger le modèle et le vectoriseur
import contractions
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import requests

# Fonction pour télécharger un fichier depuis GitHub
def download_file_from_github(file_url, save_path):
    """
    Télécharge un fichier depuis GitHub et le sauvegarde localement.
    Args:
        file_url (str): URL du fichier GitHub.
        save_path (str): Chemin où sauvegarder le fichier téléchargé.
    """
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Fichier téléchargé et sauvegardé sous : {save_path}")
    else:
        print(f"Erreur de téléchargement du fichier : {file_url}")

# URL des fichiers sauvegardés sur GitHub
model_url = "https://github.com/SamLouis1980/P7---Analyse-de-Sentiments/raw/main/data/log_reg_model.pkl"
vectorizer_url = "https://github.com/SamLouis1980/P7---Analyse-de-Sentiments/raw/main/data/tfidf_vectorizer.pkl"

# Télécharger le modèle et le vectoriseur dans le dossier 'data'
download_file_from_github(model_url, "data/log_reg_model.pkl")
download_file_from_github(vectorizer_url, "data/tfidf_vectorizer.pkl")

# Charger le modèle de régression logistique et le vectoriseur
log_reg_model = joblib.load('data/log_reg_model.pkl')  # Charger le modèle
vectorizer = joblib.load('data/tfidf_vectorizer.pkl')  # Charger le vectoriseur

# Définir les stopwords
stop_words = set(nltk.corpus.stopwords.words('english'))

# Fonction pour nettoyer le texte
def nettoyer_texte(texte):
    """
    Nettoie le texte en supprimant les URL, les mentions, la ponctuation, les chiffres,
    les stop words et en développant les contractions. Ajoute les hashtags extraits
    à la fin du texte.
    """
    texte = texte.lower()
    texte = contractions.fix(texte)
    texte = re.sub(r"http\S+|www\S+|https\S+", '', texte, flags=re.MULTILINE)
    texte = re.sub(r'@\w+', '', texte)
    hashtags = re.findall(r'#(\w+)', texte)
    texte = re.sub(r'#\w+', '', texte)
    texte = re.sub(r'[^\w\s]', '', texte)
    texte = re.sub(r'\d+', '', texte)
    texte = ' '.join([word for word in texte.split() if word not in stop_words])
    texte = re.sub(r'\s+', ' ', texte).strip()
    if hashtags:
        texte = f"{texte} {' '.join(hashtags)}"
    return texte

# Fonction pour préparer le texte avec le vectoriseur
def prepare_input(text):
    cleaned_text = nettoyer_texte(text)
    # Transformer le texte avec le vectoriseur TF-IDF
    text_vector = vectorizer.transform([cleaned_text])  # Retourne un vecteur sparse
    return text_vector

# Fonction de prédiction avec la régression logistique
def predict_sentiment(text):
    input_data = prepare_input(text)  # Transforme le texte en vecteur TF-IDF
    prediction = log_reg_model.predict(input_data)  # Prédiction avec le modèle de régression logistique
    sentiment = "positif" if prediction == 1 else "négatif"
    return sentiment

# Application Streamlit
st.title("Analyse de Sentiment des Tweets")

# Zone de texte pour l'entrée de l'utilisateur
text_input = st.text_area("Entrez le tweet à analyser", "")

# Bouton pour analyser le sentiment
if st.button("Analyser"):
    if text_input:
        sentiment = predict_sentiment(text_input)
        st.write(f"Le sentiment du tweet est : {sentiment}")
    else:
        st.write("Veuillez entrer un tweet pour l'analyser.")

# Fonctionnalité de feedback
feedback = st.radio("Le sentiment prédit est-il correct ?", ('Oui', 'Non'))
