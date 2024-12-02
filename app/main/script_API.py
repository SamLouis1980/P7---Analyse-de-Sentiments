import os
import streamlit as st
import requests

# URL de l'API FastAPI
api_url = "http://backend:8000/predict"
feedback_url = "http://backend:8000/feedback"

# Application Streamlit
st.title("Analyse de Sentiment des Tweets")

# Zone de texte pour l'entrée de l'utilisateur
text_input = st.text_area("Entrez le tweet à analyser", "")

# Bouton pour analyser
if st.button("Analyser"):
    if text_input:
        try:
            # Envoyer la requête à l'API pour obtenir la prédiction
            response = requests.post(api_url, json={"text": text_input})
            
            # Vérifier que la requête a réussi
            if response.status_code == 200:
                result = response.json()
                sentiment = result['sentiment']
                st.session_state['prediction'] = sentiment  # Sauvegarder la prédiction
                
                # Afficher la prédiction
                st.write(f"Le sentiment du tweet est : {sentiment}")
            else:
                st.write("Erreur lors de la communication avec l'API. Code d'erreur : {}".format(response.status_code))
        
        except requests.exceptions.RequestException as e:
            st.write("Erreur de connexion à l'API : {}".format(e))

    else:
        st.write("Veuillez entrer un tweet pour l'analyser.")

# Ajouter un feedback utilisateur
if st.session_state.get('prediction') is not None:
    feedback = st.selectbox('La prédiction était-elle correcte ?', ('Sélectionnez une option', 'Oui', 'Non'))
    
    # Si l'utilisateur fournit un feedback "Non", envoyer une requête à l'API de feedback
    if feedback == 'Non':
        try:
            feedback_data = {
                'text': text_input,
                'prediction': st.session_state['prediction'],
                'feedback': feedback
            }
            feedback_response = requests.post(feedback_url, json=feedback_data)
            
            if feedback_response.status_code == 200:
                st.write("Merci pour votre retour ! Votre feedback a été envoyé.")
            else:
                st.write("Erreur lors de l'envoi du feedback. Code d'erreur : {}".format(feedback_response.status_code))
        except requests.exceptions.RequestException as e:
            st.write("Erreur de connexion pour envoyer le feedback : {}".format(e))