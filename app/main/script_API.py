import streamlit as st
import requests
from applicationinsights import TelemetryClient  # Azure Application Insights

# Initialiser le client Application Insights avec ta clé d'instrumentation
tc = TelemetryClient('77d3cc30-ccb2-48fb-bb52-a7dbaa2eb669')

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
            # Suivi de l'action utilisateur
            tc.track_event('Tweet Analysis', {'tweet': text_input})
            tc.flush()

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
                
                # Suivi de la prédiction reçue
                tc.track_event('Prediction Received', {'tweet': text_input, 'sentiment': sentiment})
                tc.flush()
            else:
                st.write(f"Erreur lors de la communication avec l'API. Code d'erreur : {response.status_code}")
                # Suivi d'une erreur de réponse
                tc.track_event('API Error', {'endpoint': api_url, 'status_code': response.status_code})
                tc.flush()

        except requests.exceptions.RequestException as e:
            st.write(f"Erreur de connexion à l'API : {e}")
            # Suivi d'une exception
            tc.track_exception()
            tc.flush()
    else:
        st.write("Veuillez entrer un tweet pour l'analyser.")

# Vérifier que la prédiction existe dans l'état de session
if 'prediction' in st.session_state and st.session_state['prediction'] is not None:
    # Afficher un formulaire de feedback
    feedback = st.selectbox('La prédiction était-elle correcte ?', ('Sélectionnez une option', 'Oui', 'Non'))
    
    # Si l'utilisateur fournit un feedback, envoyer une requête à l'API de feedback
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
                # Suivi de l'envoi du feedback
                tc.track_event('Feedback Sent', feedback_data)
                tc.flush()
            else:
                st.write(f"Erreur lors de l'envoi du feedback. Code d'erreur : {feedback_response.status_code}")
                # Suivi d'une erreur de feedback
                tc.track_event('Feedback API Error', {'endpoint': feedback_url, 'status_code': feedback_response.status_code})
                tc.flush()
        except requests.exceptions.RequestException as e:
            st.write(f"Erreur de connexion pour envoyer le feedback : {e}")
            # Suivi d'une exception lors de l'envoi du feedback
            tc.track_exception()
            tc.flush()
else:
    st.write("Aucune prédiction effectuée, veuillez soumettre un tweet pour analyser son sentiment.")
