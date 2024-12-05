from unittest.mock import patch
import requests
import pytest

@patch("requests.post")
def test_api_connection(mock_post):
    # Simule une réponse réussie de l'API
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"sentiment": "positif"}
    
    response = requests.post("http://backend:8000/predict", json={"text": "Un tweet positif"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positif"

import streamlit as st
from unittest.mock import patch

@patch("streamlit.text_area")
@patch("streamlit.button")
def test_streamlit_ui(mock_button, mock_text_area):
    # Simule l'entrée utilisateur
    mock_text_area.return_value = "Un tweet positif"
    mock_button.return_value = True
    
    # Appelle les fonctions Streamlit
    text_input = st.text_area("Entrez le tweet à analyser", "")
    button_clicked = st.button("Analyser")
    
    assert text_input == "Un tweet positif"
    assert button_clicked is True