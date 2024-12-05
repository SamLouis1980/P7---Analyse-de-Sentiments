import pytest
from app.fastapi.fast import nettoyer_texte

def test_nettoyer_texte_urls():
    texte = "Voici un lien http://example.com à supprimer"
    result = nettoyer_texte(texte)
    assert "http://example.com" not in result

def test_nettoyer_texte_mentions():
    texte = "Salut @user, comment ça va ?"
    result = nettoyer_texte(texte)
    assert "@user" not in result

def test_nettoyer_texte_hashtags():
    texte = "Regarde #python, c'est génial !"
    result = nettoyer_texte(texte)
    assert "#python" not in result

def test_nettoyer_texte_stopwords():
    texte = "This is a test with stopwords"
    result = nettoyer_texte(texte)
    assert "is" not in result

from fastapi.testclient import TestClient
from app.fastapi.fast import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur l'API de prédiction de sentiment"}

def test_predict_endpoint():
    payload = {"text": "Je suis très heureux aujourd'hui"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "sentiment" in response.json()

def test_feedback_endpoint():
    payload = {
        "text": "Je suis très heureux aujourd'hui",
        "prediction": "positif",
        "feedback": "Oui"
    }
    response = client.post("/feedback", json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Feedback reçu avec succès"}