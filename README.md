# 📊 DataViz - Panel de Datos Argentina

Aplicación web para crear reportes visuales con datos del Banco Mundial usando FastAPI, React.js y Chart.js.

## 📁 Estructura del Proyecto

```
dataviz-app/
├── main.py                 # Servidor FastAPI
├── requirements.txt        # Dependencias Python
├── run.sh                 # Script para iniciar servidor
└── static/
    ├── index.html         # Página principal
    ├── css/
    │   └── style.css      # Estilos (colores pasteles/verdes)
    └── js/
        ├── config.js      # Configuración y constantes
        ├── api.js         # Funciones para consumir API
        ├── app.js         # Aplicación React principal
        └── components/
            ├── Sidebar.js      # Menú lateral
            ├── Header.js       # Encabezado
            ├── ChartModal.js   # Modal de gráficas
            ├── TextModal.js    # Modal de texto
            └── Workspace.js    # Área de trabajo
```

## 🚀 Instalación y Ejecución

### Requisitos
- Python 3.8+
- pip (gestor de paquetes Python)
- Navegador moderno

### Pasos

1. **Clonar/Descargar el proyecto**
```bash
cd dataviz-app
```

2. **Crear entorno virtual (opcional pero recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Iniciar servidor**
```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

O usar el script:
```bash
bash run.sh
```

5. **Abrir en navegador**
```
http://localhost:8000
```

## 🎨 Características

### Backend (FastAPI)
- ✅ API REST para servir datos
- ✅ Endpoints de métricas de Argentina
- ✅ Datos del Banco Mundial (PIB, Inflación, Desempleo, Población)
- ✅ Servir archivos estáticos

### Frontend (React + HTML)
- ✅ Interfaz clásica con colores pasteles y verdes
- ✅ Componentes React modularizados
- ✅ Gráficas interactivas con Chart.js
- ✅ Modal para crear gráficas y texto
- ✅ Sistema de historial (deshacer)
- ✅ Indicador de estado del proyecto

## 📖 Uso

### Agregar Gráfica
1. Haz clic en "📈 Agregar Gráfica"
2. Selecciona una métrica (PIB, Inflación, etc.)
3. Elige tipo: Línea, Barras, Área o Rosca
4. Haz clic en "Crear"

### Agregar Texto
1. Haz clic en "✏️ Agregar Texto"
2. Escribe tu contenido
3. Haz clic en "Agregar"

### Editar/Eliminar
- Pasa mouse sobre elementos
- Usa los botones ✏️ (editar) o 🗑 (eliminar)

### Duplicar
- Haz clic en 📋 sobre una gráfica

### Deshacer
- Haz clic en "↶ Deshacer" en el menú

### Guardar
- Haz clic en "💾 Guardar"

## 🎨 Diseño

### Paleta de Colores
- Verde principal: #8fbf8f
- Verde claro: #a8d5a8
- Verde oscuro: #6b9b6b
- Pastel secundario: #e8d4e8
- Pastel acento: #d4c5e8
- Fondo: #f5f3f5

### Estilo
- Clásico y elegante
- Interfaz intuitiva
- Responsive (funciona en mobile)
- Sin diseño ultra-moderno

## 📊 Datos Disponibles

**Fuente:** Banco Mundial (World Bank)
**País:** Argentina
**Período:** 2015-2023

- **PIB**: Crecimiento porcentual anual
- **Inflación**: Tasa de inflación anual
- **Desempleo**: Tasa de desempleo anual
- **Población**: Total en millones

## 🔧 Personalización

### Agregar Más Métricas
Edita `main.py` en la sección `ARGENTINA_DATA`:

```python
"nuevo_indicador": {
    "label": "Nombre del Indicador",
    "data": [
        {"year": 2023, "value": 100},
        ...
    ]
}
```

### Cambiar Colores
Edita las variables CSS en `static/css/style.css`:

```css
:root {
    --color-primary: #tu-color;
    ...
}
```

### Modificar Tipos de Gráficas
En `static/js/config.js`, edita `CONFIG.CHART_TYPES`

## 🛠 Tecnologías

- **Backend**: FastAPI, Python 3
- **Frontend**: React.js 18, HTML5, CSS3
- **Gráficas**: Chart.js 3.9
- **Estilos**: CSS personalizado (sin frameworks)

## 📝 Notas Importantes

1. Los datos se guardan en memoria del navegador
2. Para persistencia, implementa localStorage o base de datos
3. Chart.js se carga desde CDN
4. React se carga desde CDN (no es build con webpack)

## 🚀 Próximas Mejoras

- [ ] Persistencia con localStorage
- [ ] Exportar a PDF
- [ ] Más tipos de gráficas
- [ ] Importar CSV personalizado
- [ ] Tema oscuro/claro
- [ ] Análisis estadístico

## 📄 Licencia

Libre para uso personal y educativo.

---

**Versión:** 1.0  
**Última Actualización:** 2025
