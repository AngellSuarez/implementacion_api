import pytest
from insumo.models import Marca

@pytest.mark.django_db
def test_creacion_marca():
    marca = Marca.objects.create(
        nombre = "avon"
    )
    assert marca.pk is not None