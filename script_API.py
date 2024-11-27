# -*- coding: utf-8 -*-
import os
import streamlit as st
import requests
import numpy as np
import pandas as pd
import re
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
import contractions

# Téléchargement des ressources nécessaires pour la lemmatisation
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Définir les stopwords
stop_words = set(nltk.corpus.stopwords.words('english'))

# Initialiser le stemmer
stemmer = PorterStemmer()

# Fonction pour nettoyer le texte
def nettoyer_texte(texte):
    """
    Nettoie le texte en supprimant les URL, les mentions, la ponctuation, les chiffres,
    les stop words et en développant les contractions. Ajoute les hashtags extraits
    à la fin du texte.
    """
    # Convertir en minuscules
    texte = texte.lower()
    # Développer les contractions courantes
    texte = contractions.fix(texte)
    # Retirer les URL
    texte = re.sub(r"http\S+|www\S+|https\S+", '', texte, flags=re.MULTILINE)
    # Retirer les mentions d'utilisateurs
    texte = re.sub(r'@\w+', '', texte)
    # Extraire et conserver les hashtags
    hashtags = re.findall(r'#(\w+)', texte)
    texte = re.sub(r'#\w+', '', texte)
    # Retirer les caractères spéciaux et la ponctuation
    texte = re.sub(r'[^\w\s]', '', texte)
    # Retirer les chiffres
    texte = re.sub(r'\d+', '', texte)
    # Retirer les stop words
    texte = ' '.join([word for word in texte.split() if word not in stop_words])
    # Retirer les espaces multiples et superflus
    texte = re.sub(r'\s+', ' ', texte).strip()
    # Ajouter les hashtags extraits à la fin du texte
    if hashtags:
        texte = f"{texte} {' '.join(hashtags)}"

    return texte

# Fonction de stemmatisation
def stemmer_texte(texte):
    tokens = nltk.word_tokenize(texte)
    return ' '.join([stemmer.stem(token) for token in tokens])

# Calculer la moyenne des embeddings Word2Vec pour chaque tweet
def get_avg_word2vec_embeddings(text_data, model, vector_size):
    embeddings = []
    for tweet in text_data:
        word_vectors = [model.wv[word] for word in tweet if word in model.wv]
        if word_vectors:
            avg_vector = np.mean(word_vectors, axis=0)
        else:
            avg_vector = np.zeros(vector_size)  # Vecteur nul si aucun mot n'est présent dans Word2Vec
        embeddings.append(avg_vector)
    return np.array(embeddings)

# Télécharger le modèle Word2Vec depuis Azure
def download_word2vec_model_from_azure():
    connect_str = "ton_connect_str_azure"  # Remplace par ta chaîne de connexion Azure
    container_name = "projet7"
    blob_name = "word2vec_tweets.model"
    download_file_path = "word2vec_tweets.model"

    # Créer un client BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)

    # Télécharger le fichier
    blob_client = container_client.get_blob_client(blob_name)
    with open(download_file_path, "wb") as file:
        file.write(blob_client.download_blob().readall())

    word2vec_model = Word2Vec.load(download_file_path)
    return word2vec_model

# Charger le modèle Word2Vec
word2vec_model = download_word2vec_model_from_azure()

# Préparer l'entrée pour TensorFlow Lite
def prepare_input(text):
    cleaned_text = nettoyer_texte(text)
    stemmed_text = stemmer_texte(cleaned_text)
    tokenized_text = stemmed_text.split()

    word2vec_vector = get_avg_word2vec_embeddings([tokenized_text], word2vec_model, word2vec_model.vector_size)

    # Reformater l'entrée pour ajouter une dimension batch_size = 1
    word2vec_vector = np.expand_dims(word2vec_vector, axis=0)  # Ajouter la dimension batch_size
    return np.array(word2vec_vector, dtype=np.float32)

# Fonction de prédiction avec TensorFlow Lite (Simulée ici pour simplification)
def predict_sentiment(text):
    input_data = prepare_input(text)
    # Simuler une prédiction avec un modèle pré-entraîné
    # Remplacer par la logique réelle de TensorFlow Lite une fois le modèle chargé
    prediction = np.random.choice([0, 1], p=[0.5, 0.5])  # 0 = négatif, 1 = positif
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

if feedback == 'Non':
    st.write("Merci pour votre retour ! Nous allons améliorer la prédiction.")
