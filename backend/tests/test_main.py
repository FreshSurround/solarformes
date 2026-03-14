from fastapi.testclient import TestClient
from .maintest import app

test_client = TestClient(app)

def test_main():
    respuesta = test_client.get("/")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"test": "corriendo correctamente"}
