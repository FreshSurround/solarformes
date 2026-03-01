# main.py
from config.serial_config import Settings
from utils.logger import get_logger
from models.models import Indicator
from routes.api_routes import get_indicators
import pandas as pd
import numpy as np
from auth import *

# Inicialización
config = Settings()
# Inicializamos logger
logger = get_logger("MainApp")

# Crear un indicador de prueba
test_indicator = Indicator(name="Ambiente_CO2", category="Ambiente", code="CO2")

# Mostrar que todo anda bien
logger.info("Aplicación iniciada correctamente.")
logger.info(f"Indicador de prueba: {test_indicator.name} = {test_indicator.code} ({test_indicator.category})")
#print(config.DATABASE_PATH)
##print("======================")
##print(get_indicators())
#

#df = pd.read_csv("Databases/WorldBank/Pais/arg/API_ARG_DS2_en_csv_v2_2866.csv", usecols=['Country Name','Country Code','Indicator Code'])

df = pd.read_csv("Databases/WorldBank/Pais/arg/API_ARG_DS2_en_csv_v2_2866.csv", nrows=10)

indicators = [Indicator(name=row['Country Name'],
    category=row['Indicator Code'],
    code=row['Country Code'])
    for _, row in df.iterrows()]

print(*[f"{indicators[i]}\n" for i in np.linspace(0, 9, 10, dtype="int")])

print("Sistema corriendo. Revisa el log para detalles.")
