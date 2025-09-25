from main import calcc_dosis
from fastapi.testclient import TestClient
from main import app  # Asegúrate de importar tu app FastAPI

# Configurar el TestClient
client = TestClient(app)

def test_calcc_dosis_with_validation():
    # Test exitoso
    response = client.get("/calcc_dosis/pesos/dosis/", params={
        "peso": 10,
        "dosis": 30,
        "pres_ml": 50,
        "interval": 3
    })

    assert response.status_code == 200
    data = response.json()
    assert "dosis_calculada" in data
    assert data["dosis_calculada"] == 2.0

def test_calcc_dosis_invalid_zero_params():
    # Test con parámetros cero
    response = client.get("/calcc_dosis/pesos/dosis/", params={
        "peso": 0,  # Inválido
        "dosis": 100,
        "pres_ml": 50,
        "interval": 2
    })

    assert response.status_code == 400