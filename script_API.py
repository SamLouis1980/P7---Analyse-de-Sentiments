import os
import streamlit as st
import requests

# URL de l'API FastAPI
api_url = "https://analyse-sentiment-app.herokuapp.com/predict"
feedback_url = "https://analyse-sentiment-app.herokuapp.com/feedback"

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
                st.write("Si la prédiction est incorrecte, vous pouvez fournir un feedback ci-dessous.")
            else:
                st.write(f"Erreur lors de la communication avec l'API. Code d'erreur : {response.status_code}")
        
        except requests.exceptions.RequestException as e:
            st.write(f"Erreur de connexion à l'API : {e}")

    else:
        st.write("Veuillez entrer un tweet pour l'analyser.")

# Vérifier que la prédiction existe dans l'état de session
if 'prediction' in st.session_state and st.session_state['prediction'] is not None:
    # Afficher un formulaire de feedback
    feedback = st.selectbox('La prédiction était-elle correcte ?', ('Sélectionnez une option', 'Oui', 'Non'))
    
    # Si l'utilisateur fournit un feedback "Non", envoyer une requête à l'API de feedback
    if feedback != 'Sélectionnez une option':
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
                st.write(f"Erreur lors de l'envoi du feedback. Code d'erreur : {feedback_response.status_code}")
        except requests.exceptions.RequestException as e:
            st.write(f"Erreur de connexion pour envoyer le feedback : {e}")

else:
    st.write("Aucune prédiction effectuée, veuillez soumettre un tweet pour analyser son sentiment.")