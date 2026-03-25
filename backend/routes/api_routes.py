from fastapi import APIRouter
#from .models.modelss import Indicator

router = APIRouter()

class bigRouter:
    def __init__(self):
        return None

    @router.get("/indicators")
    def get_indicators(self):
        data = [
            Indicator(name="Emisiones CO2", category="Ambiente", code="CO2"),
            Indicator(name="Uso de energías renovables", category="Sustentabilidad", code="REN"),
            Indicator(name="Innovación tecnológica", category="Tecnología", code="INN"),
        ]
        return [d.__dict__ for d in data]  # devolvemos como JSON

    @router.get("/indicators/{category}")
    def get_indicators_by_category(self, category: str):
        all_data = [
            Indicator(name="Emisiones CO2", category="Ambiente"),
            Indicator(name="Uso de energías renovables", category="Sustentabilidad"),
            Indicator(name="Innovación tecnológica", category="Tecnología"),
        ]
        filtered = [d.__dict__ for d in all_data if d.category.lower() == category.lower()]
        return filtered

    def iniciar_server(self):
        return {"hola2": "hola2"}
