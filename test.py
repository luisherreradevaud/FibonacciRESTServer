from service import app
from flask import json
import time

def test_n_Negativo():
    response = app.test_client().get('/phi/-1')
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['n'] == "Solo enteros positivos."

def test_n_No_Numerico():
    response = app.test_client().get('/phi/aaa')
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['n'] == "Solo enteros positivos."

def test_n_Positivo():
    response = app.test_client().get('/phi/3')
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['n'] == 2
