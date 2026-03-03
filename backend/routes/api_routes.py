from fastapi import APIRouter
from models.models import Indicator  # tus clases de modelos


class bigRouter:
    app = APIRouter()
    def __init__(self):
        return None

    # ruta para listar todos los indicadores
    @app.get("/indicators")
    def get_indicators():
        # simulamos obtener datos del dataset
        data = [
            Indicator(name="Emisiones CO2", category="Ambiente", code="CO2"),
            Indicator(name="Uso de energías renovables", category="Sustentabilidad", code="REN"),
            Indicator(name="Innovación tecnológica", category="Tecnología", code="INN"),
        ]
        return [d.__dict__ for d in data]  # devolvemos como JSON

    # ruta con parámetro para filtrar por categoría
    @app.get("/indicators/{category}")
    def get_indicators_by_category(category: str):
        all_data = [
            Indicator(name="Emisiones CO2", category="Ambiente"),
            Indicator(name="Uso de energías renovables", category="Sustentabilidad"),
            Indicator(name="Innovación tecnológica", category="Tecnología"),
        ]
        filtered = [d.__dict__ for d in all_data if d.category.lower() == category.lower()]
        return filtered


    @app.get("/")
    def iniciar_server():
        return {"hola": "hola"}
