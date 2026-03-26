# 🌱 Solarformes

**Panel interactivo de diseño y visualización de datos de Argentina**

Web application for creating, organizing, and exporting data visualizations based on public datasets (e.g., World Bank). Built with a FastAPI backend and a modular React frontend.

---

## Demo

<video src="assets/'Solarformes0-1.mp4'" autoplay loop muted playsinline width="600"></video>

---

## Key Features

- Create and manage charts (line, bar, area, doughnut)
- Add, edit, duplicate, and delete text or chart elements
- Undo actions and save project state
- Export reports to PDF (via browser print) (on development)
- Modular layout with sidebar + workspace

---

## Estructura del Proyecto

```
Solarformes/
├── LICENSE                          Licencia del proyecto
├── main.py                          Servidor FastAPI
├── README.md                        Este archivo
├── requirements.txt                 Dependencias Python
│
└── static/                          Archivos servidos al navegador
    │
    ├── index.html                   Página principal
    │
    ├── css/
    │   └── style.css                Estilos (colores pasteles/verdes)
    │
    ├── external/                    Librerías externas
    │   ├── react.js                 React 18 minificado
    │   ├── reactDOM.js              ReactDOM minificado
    │   └── chart.js                 Chart.js minificado
    │
    └── js/                          Scripts de aplicación
        │
        ├── config.js                Configuración y constantes
        ├── api.js                   Cliente para consumir API
        ├── app.js                   Aplicación React principal
        │
        └── components/              Componentes React reutilizables
            ├── Header.js            Encabezado
            ├── Sidebar.js           Menú lateral
            ├── Workspace.js         Área de trabajo
            ├── ChartModal.js        Modal para gráficas
            └── TextModal.js         Modal para texto
```

---

### Tech Stack
Backend: FastAPI, Uvicorn, Python 3.8+
Frontend: React 18 (CDN), Chart.js, Vanilla JS
Architecture: REST API + modular React components

---

## Instalation

First clone the repository

```bash
git clone https://github.com/FreshSurround/Solarformes
cd Solarformes
```
Then create the virtual envirioment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
Install dependencies

```bash
pip install -r requirements.txt
```
Run the server

```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Or simply do:

```bash
bash run.sh
```
Open in browser
```
http://localhost:8000
```

---

## Data
Source: World Bank (Argentina)
Period: 2015–2023
Metrics: GDP growth, inflation, unemployment, population

---

## Personalization
Colors: edit static/css/style.css
Chart types: edit CONFIG.CHART_TYPES in config.js

style.css
```css
:root {
    --color-primary: #8fbf8f;           
    --color-primary-light: #a8d5a8;     
    --color-primary-dark: #6b9b6b;      
    --color-secondary: #e8d4e8;         
    --color-accent: #d4c5e8;            
    --color-bg: #f5f3f5;                
    --color-white: #ffffff;             
    --color-text: #4a4a4a;              
    --color-text-light: #7a7a7a;        
}
```
config.js:
```javascript
CONFIG.CHART_TYPES = [
    { key: 'line', label: 'Línea' },
    { key: 'bar', label: 'Barras' },
    { key: 'area', label: 'Área' },
    { key: 'doughnut', label: 'Rosca' },
]
```

If 8000 is in use:

```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8001
```
---

## API
GET /api/metrics → list available metrics
GET /api/data/{metric} → data for a metric
GET /api/all-data → all datasets

---

## LICENSE

See [Licence](License)
