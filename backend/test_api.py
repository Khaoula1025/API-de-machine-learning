from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict_risk():

    payload = {
        "age": 50,
        "gender": 0,
        "pressurehight": 21,
        "pressurelow": 9,
        "glucose":11,
        "kcm":11.8,
        "troponin":5.9,
        "impluse":8
    }

    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200