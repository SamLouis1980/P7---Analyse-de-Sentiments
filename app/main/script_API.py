import os
import streamlit as st
import requests

# URL de l'API FastAPI
api_url = "http://backend:8000/predict"

# Application Streamlit
st.title("Analyse de Sentiment des Tweets")

# Zone de texte pour l'entrée de l'utilisateur
text_input = st.text_area("Entrez le tweet à analyser", "")

# Bouton pour analyser le sentiment
if st.button("Analyser"):
    if text_input:
        # Envoyer une requête POST à l'API FastAPI
        response = requests.post(api_url, json={"text": text_input})
        
        if response.status_code == 200:
            result = response.json()
            sentiment = result['sentiment']
            st.write(f"Le sentiment du tweet est : {sentiment}")

            # Ajout de la fonction de feedback
            feedback = st.radio("Le sentiment est-il correct ?", ('Correct', 'Incorrect'))

            # Si un feedback est donné
            if feedback:
                # Enregistrer le feedback (ici dans un fichier CSV)
                with open('feedback.csv', 'a') as f:
                    f.write(f"{text_input},{sentiment},{feedback}\n")
                st.write("Merci pour votre feedback !")
        else:
            st.write("Erreur lors de la communication avec l'API.")
    else:
        st.write("Veuillez entrer un tweet pour l'analyser.")