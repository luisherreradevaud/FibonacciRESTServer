from service import app
from flask import json
import time

def test_n_Negativo():
    response = app.test_client().get('/phi/-1')
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['respuestaPhi'] == "Solo enteros positivos."
    assert data['respuestaSuma'] == "Solo enteros positivos."
    assert data['respuestaMult'] == "Solo enteros positivos."

def test_n_No_Numerico():
    response = app.test_client().get('/phi/aaa')
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['respuestaPhi'] == "Solo enteros positivos."
    assert data['respuestaSuma'] == "Solo enteros positivos."
    assert data['respuestaMult'] == "Solo enteros positivos."

def test_n_Positivo():
    response = app.test_client().get('/phi/3')
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['respuestaPhi'] == 2
    assert data['respuestaSuma'] == 6
    assert data['respuestaMult'] == 14

def test_n_Positivo_mas():
    response = app.test_client().get('/phi/7')
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['respuestaPhi'] == 13
    assert data['respuestaSuma'] == 28
    assert data['respuestaMult'] == 140

def test_n_Positivo_mas_aun():
    response = app.test_client().get('/phi/9')
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['respuestaPhi'] == 34
    assert data['respuestaSuma'] == 45
    assert data['respuestaMult'] == 285
