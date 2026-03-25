from .config.serial_config import Settings
from .utils.logger import get_logger
from .models.modelss import Indicator
from .routes.api_routes import bigRouter
import pandas as pd
import numpy as np
from fastapi import FastAPI
from .auth import *

from fastapi.responses import HTMLResponse

config = Settings()
logger = get_logger("MainApp")

app = FastAPI()
@app.get("/")
def iniciar():
    return {"hola": "hola"}

router = bigRouter()
router.iniciar_server()

# Crear un indicador de prueba
test_indicator = Indicator(name="Ambiente_CO2", category="Ambiente", code="CO2")

# Mostrar que todo anda bien
logger.info("Aplicación iniciada correctamente.")
logger.info(f"Indicador de prueba: {test_indicator.name} = {test_indicator.code} ({test_indicator.category})")
print(f"\nPATH segun config = {config.DATABASE_PATH}\n")
##print("======================")
#

#df = pd.read_csv("Databases/WorldBank/Pais/arg/API_ARG_DS2_en_csv_v2_2866.csv", usecols=['Country Name','Country Code','Indicator Code'])

df = pd.read_csv("backend/Databases/WorldBank/Pais/arg/API_ARG_DS2_en_csv_v2_2866.csv", nrows=10)

indicators = [Indicator(name=row['Country Name'],
    category=row['Indicator Code'],
    code=row['Country Code'])
    for _, row in df.iterrows()]

#print(*[f"{indicators[i]}\n" for i in np.linspace(0, 9, 10, dtype="int")])
#print("Sistema corriendo. Revisa el log para detalles.")

@app.get("/", response_class=HTMLResponse)
def ui():
    return """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Carga de Datos</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Segoe UI', sans-serif; background: #f0f2f5; min-height: 100vh; padding: 2rem; }
    h1  { color: #1a1a2e; margin-bottom: 1.5rem; font-size: 1.6rem; }
    h2  { color: #16213e; margin-bottom: 1rem; font-size: 1.1rem; }

    .card {
      background: white; border-radius: 12px; padding: 1.5rem;
      box-shadow: 0 2px 12px rgba(0,0,0,.08); margin-bottom: 1.5rem;
    }

    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: .75rem; }
    label { display: block; font-size: .8rem; color: #555; margin-bottom: .25rem; font-weight: 600; }
    input, textarea {
      width: 100%; padding: .55rem .75rem; border: 1.5px solid #dde; border-radius: 8px;
      font-size: .95rem; transition: border .2s;
    }
    input:focus, textarea:focus { outline: none; border-color: #4f46e5; }
    textarea { grid-column: span 2; resize: vertical; min-height: 70px; }

    .btn-row { margin-top: 1rem; display: flex; gap: .75rem; }
    button {
      padding: .6rem 1.4rem; border: none; border-radius: 8px;
      font-weight: 600; cursor: pointer; font-size: .9rem; transition: opacity .2s;
    }
    button:hover { opacity: .85; }
    .btn-primary { background: #4f46e5; color: white; }
    .btn-clear   { background: #e5e7eb; color: #374151; }

    #toast {
      position: fixed; bottom: 1.5rem; right: 1.5rem;
      background: #10b981; color: white; padding: .75rem 1.25rem;
      border-radius: 10px; font-weight: 600; display: none;
      box-shadow: 0 4px 12px rgba(0,0,0,.15);
    }
    #toast.error { background: #ef4444; }

    table { width: 100%; border-collapse: collapse; font-size: .88rem; }
    th { background: #f8f9fa; color: #555; text-align: left; padding: .6rem .8rem; border-bottom: 2px solid #eee; }
    td { padding: .6rem .8rem; border-bottom: 1px solid #f0f0f0; vertical-align: top; }
    tr:hover td { background: #fafafe; }
    .del-btn {
      background: #fee2e2; color: #dc2626; border: none; border-radius: 6px;
      padding: .3rem .7rem; cursor: pointer; font-size: .8rem; font-weight: 600;
    }
    .del-btn:hover { background: #fca5a5; }
    .empty { text-align: center; color: #aaa; padding: 2rem; }
    .badge { font-size: .7rem; color: #888; }
  </style>
</head>

<body>
    <h1>📋 Carga de Datos — Base Local</h1>
</body>
</html>
"""
