from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import re
import nltk
import contractions
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os
import csv

# Charger les modèles et le vectoriseur depuis le répertoire du projet
model_path = os.path.join(os.getcwd(), 'data', 'log_reg_model.pkl')
vectorizer_path = os.path.join(os.getcwd(), 'data', 'tfidf_vectorizer.pkl')

with open(model_path, 'rb') as f:
    log_reg_model = pickle.load(f)

with open(vectorizer_path, 'rb') as f:
    vectorizer = pickle.load(f)

# Télécharger les stopwords si nécessaire
nltk.download('stopwords')

# Créer une application FastAPI
app = FastAPI()

# Définir le modèle de la requête
class TextRequest(BaseModel):
    text: str

class FeedbackRequest(BaseModel):
    text: str
    prediction: str
    feedback: str

# Fonction pour nettoyer le texte
def nettoyer_texte(texte):
    texte = texte.lower()
    texte = contractions.fix(texte)
    texte = re.sub(r"http\S+|www\S+|https\S+", '', texte, flags=re.MULTILINE)
    texte = re.sub(r'@\w+', '', texte)
    texte = re.sub(r'#\w+', '', texte)
    texte = re.sub(r'[^\w\s]', '', texte)
    texte = re.sub(r'\d+', '', texte)
    texte = ' '.join([word for word in texte.split() if word not in nltk.corpus.stopwords.words('english')])
    texte = re.sub(r'\s+', ' ', texte).strip()
    return texte

# Fonction pour sauvegarder les feedbacks dans un fichier CSV
def save_feedback_to_csv(feedback_request):
    csv_file_path = 'feedbacks.csv'
    
    # Vérifier si le fichier existe déjà pour ne pas ajouter l'en-tête plusieurs fois
    file_exists = os.path.isfile(csv_file_path)
    
    # Ouvrir le fichier en mode ajout ('a')
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Si le fichier est vide, écrire les en-têtes
        if not file_exists:
            writer.writerow(['Tweet', 'Prédiction', 'Feedback'])
        
        # Ajouter la ligne avec les données du feedback
        writer.writerow([feedback_request.text, feedback_request.prediction, feedback_request.feedback])

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction de sentiment"}

@app.post("/predict")
def predict(request: TextRequest):
    cleaned_text = nettoyer_texte(request.text)
    text_vector = vectorizer.transform([cleaned_text])
    prediction = log_reg_model.predict(text_vector)
    sentiment = "positif" if prediction == 1 else "négatif"
    return {"sentiment": sentiment}

@app.post("/feedback")
def feedback(feedback_request: FeedbackRequest):
    # Enregistrer ou traiter le feedback ici
    print(f"Feedback reçu : {feedback_request.text}, prédiction : {feedback_request.prediction}, feedback : {feedback_request.feedback}")
    
    # Sauvegarder le feedback dans le fichier CSV
    save_feedback_to_csv(feedback_request)

    return {"message": "Feedback reçu avec succès"}