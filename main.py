from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json
import os

app = FastAPI()

# Datos de Argentina - Banco Mundial
ARGENTINA_DATA = {
    "gdp": {
        "label": "PIB - Crecimiento (%)",
        "data": [
            {"year": 2015, "value": 2.73},
            {"year": 2016, "value": -2.17},
            {"year": 2017, "value": 2.87},
            {"year": 2018, "value": -2.54},
            {"year": 2019, "value": -2.09},
            {"year": 2020, "value": -9.95},
            {"year": 2021, "value": 10.67},
            {"year": 2022, "value": 5.07},
            {"year": 2023, "value": -1.04},
        ]
    },
    "inflation": {
        "label": "Inflación (%)",
        "data": [
            {"year": 2015, "value": 27.20},
            {"year": 2016, "value": 40.54},
            {"year": 2017, "value": 24.76},
            {"year": 2018, "value": 47.63},
            {"year": 2019, "value": 53.59},
            {"year": 2020, "value": 42.00},
            {"year": 2021, "value": 50.93},
            {"year": 2022, "value": 99.85},
            {"year": 2023, "value": 138.79},
        ]
    },
    "unemployment": {
        "label": "Desempleo (%)",
        "data": [
            {"year": 2015, "value": 6.91},
            {"year": 2016, "value": 8.60},
            {"year": 2017, "value": 8.24},
            {"year": 2018, "value": 9.24},
            {"year": 2019, "value": 9.79},
            {"year": 2020, "value": 11.54},
            {"year": 2021, "value": 10.42},
            {"year": 2022, "value": 9.73},
            {"year": 2023, "value": 8.66},
        ]
    },
    "population": {
        "label": "Población (millones)",
        "data": [
            {"year": 2015, "value": 43.58},
            {"year": 2016, "value": 43.90},
            {"year": 2017, "value": 44.22},
            {"year": 2018, "value": 44.51},
            {"year": 2019, "value": 44.78},
            {"year": 2020, "value": 45.01},
            {"year": 2021, "value": 45.21},
            {"year": 2022, "value": 45.37},
            {"year": 2023, "value": 45.51},
        ]
    }
}

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.get("/api/metrics")
async def get_metrics():
    """Retorna lista de métricas disponibles"""
    return {
        "metrics": [
            {"key": "gdp", "label": ARGENTINA_DATA["gdp"]["label"]},
            {"key": "inflation", "label": ARGENTINA_DATA["inflation"]["label"]},
            {"key": "unemployment", "label": ARGENTINA_DATA["unemployment"]["label"]},
            {"key": "population", "label": ARGENTINA_DATA["population"]["label"]},
        ]
    }

@app.get("/api/data/{metric_key}")
async def get_metric_data(metric_key: str):
    """Retorna datos de una métrica específica"""
    if metric_key not in ARGENTINA_DATA:
        return {"error": "Métrica no encontrada"}, 404
    
    metric = ARGENTINA_DATA[metric_key]
    return {
        "key": metric_key,
        "label": metric["label"],
        "data": metric["data"]
    }

@app.get("/api/all-data")
async def get_all_data():
    """Retorna todos los datos disponibles"""
    return ARGENTINA_DATA
