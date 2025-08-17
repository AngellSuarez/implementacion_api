#repuesta de creación desde endpoint

from rest_framework.test import APIClient
import pytest

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_crear_marca(api_client):
    url = "/api/insumo/marcas/"
    data = {"nombre":"avalon"}
    response = api_client.post(url,data, format="json")
    assert response.status_code == 201 or response.status_code == 200
    assert response.data["nombre"] == "avalon"