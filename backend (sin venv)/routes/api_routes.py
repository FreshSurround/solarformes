from fastapi import APIRouter
from models.models import Indicator  # tus clases de modelos

router = APIRouter()

# ruta para listar todos los indicadores
@router.get("/indicators")
def get_indicators():
    # simulamos obtener datos del dataset
    data = [
        Indicator(name="Emisiones CO2", category="Ambiente", code="CO2"),
        Indicator(name="Uso de energías renovables", category="Sustentabilidad", code="REN"),
        Indicator(name="Innovación tecnológica", category="Tecnología", code="INN"),
    ]
    return [d.__dict__ for d in data]  # devolvemos como JSON

# ruta con parámetro para filtrar por categoría
@router.get("/indicators/{category}")
def get_indicators_by_category(category: str):
    all_data = [
        Indicator(name="Emisiones CO2", category="Ambiente"),
        Indicator(name="Uso de energías renovables", category="Sustentabilidad"),
        Indicator(name="Innovación tecnológica", category="Tecnología"),
    ]
    filtered = [d.__dict__ for d in all_data if d.category.lower() == category.lower()]
    return filtered
