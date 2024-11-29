# fast.py

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import re
import nltk
import contractions
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Charger les modèles et le vectoriseur
with open('data/log_reg_model.pkl', 'rb') as f:
    log_reg_model = pickle.load(f)

with open('data/tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Charger les stopwords une fois et les garder en mémoire
stopwords_set = set(nltk.corpus.stopwords.words('english'))

# Créer une application FastAPI
app = FastAPI()

# Définir le modèle de la requête
class TextRequest(BaseModel):
    text: str

# Fonction pour nettoyer le texte
def nettoyer_texte(texte):
    texte = texte.lower()
    texte = contractions.fix(texte)
    texte = re.sub(r"http\S+|www\S+|https\S+", '', texte, flags=re.MULTILINE)
    texte = re.sub(r'@\w+', '', texte)
    texte = re.sub(r'#\w+', '', texte)
    texte = re.sub(r'[^\w\s]', '', texte)
    texte = re.sub(r'\d+', '', texte)
    texte = ' '.join([word for word in texte.split() if word not in stopwords_set])
    texte = re.sub(r'\s+', ' ', texte).strip()
    return texte

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction de sentiment"}

# Route pour effectuer la prédiction
@app.post("/predict")
def predict(request: TextRequest):
    cleaned_text = nettoyer_texte(request.text)
    text_vector = vectorizer.transform([cleaned_text])
    prediction = log_reg_model.predict(text_vector)
    sentiment = "positif" if prediction == 1 else "négatif"
    return {"sentiment": sentiment}
