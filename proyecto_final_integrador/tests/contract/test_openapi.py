from fastapi.testclient import TestClient

from proyecto_final_integrador.main import app

client = TestClient(app)


# PRUEBA DE CONTRATO DE API (Swagger/OpenAPI):
def test_openapi_contract() -> None:
    response = client.get("/openapi.json")

    assert response.status_code == 200

    data = response.json()

    assert "/health" in data["paths"]
    assert "/auth/login" in data["paths"]
    assert "/orders" in data["paths"]

    assert "post" in data["paths"]["/orders"]
    assert "get" in data["paths"]["/orders"]
