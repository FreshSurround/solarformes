# 🌱 Solarformes

**Panel interactivo de diseño y visualización de datos de Argentina**

Aplicación web para crear, editar y organizar gráficos dinámicos basados en datos del Banco Mundial. Combina un backend robusto con FastAPI y un frontend modular usando React.js.

---

## 📋 Tabla de Contenidos

- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Personalización](#personalización)
- [Tecnologías](#tecnologías)
- [Licencia](#licencia)

---

## ✨ Características

### 📊 Gráficas Interactivas
- **4 tipos de gráficas**: Línea, Barras, Área, Rosca
- Basadas en Chart.js
- Renderizado en tiempo real
- Fácil configuración

### 📝 Editor de Contenido
- Agregar bloques de texto personalizados
- Editar y eliminar elementos
- Duplicar gráficas y textos

### 🎛️ Interfaz Intuitiva
- Barra lateral con opciones principales
- Área de trabajo tipo Jupyter Notebook
- Modales para configuración
- Diseño clásico con colores pasteles y verdes

### 🔄 Gestión de Proyecto
- Sistema de historial (deshacer)
- Indicador de estado guardado/sin guardar
- Guardar proyecto en navegador
- Exportación a PDF (a través de impresión)

### 📱 Responsivo
- Compatible con desktop y tablet
- Interfaz adaptable
- Navegación intuitiva

---

## 📁 Estructura del Proyecto

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

## 🛠️ Requisitos

### Sistema
- **Python**: 3.8 o superior
- **pip**: Gestor de paquetes Python
- **Navegador**: Moderno (Chrome, Firefox, Safari, Edge)

### Dependencias Python
- FastAPI (servidor web)
- Uvicorn (servidor ASGI)
- Python-multipart (manejo de formularios)

### Frontend
- React 18 (desde CDN)
- Chart.js 3.9 (desde CDN)
- Vanilla JavaScript (ES6+)

---

## 📦 Instalación

### Paso 1: Clonar/Descargar el Proyecto

```bash
cd Solarformes
```

### Paso 2: Crear Entorno Virtual (Recomendado)

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

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Iniciar el Servidor

```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

O en Mac/Linux:
```bash
bash run.sh
```

### Paso 5: Abrir en Navegador

```
http://localhost:8000
```

---

## 🚀 Uso

### Agregar una Gráfica

1. Haz clic en **"📈 Agregar Gráfica"** en la barra lateral
2. Selecciona una métrica:
   - PIB - Crecimiento (%)
   - Inflación (%)
   - Desempleo (%)
   - Población (millones)
3. Elige el tipo de gráfica:
   - **Línea**: Para mostrar tendencias
   - **Barras**: Para comparaciones
   - **Área**: Para magnitudes acumulativas
   - **Rosca**: Para proporciones
4. Haz clic en **"Crear"**

### Agregar Texto

1. Haz clic en **"✏️ Agregar Texto"** en la barra lateral
2. Escribe tu contenido en el modal
3. Haz clic en **"Agregar"**

### Editar Elemento

1. Pasa el mouse sobre el elemento
2. Haz clic en el icono **"✏️"** (solo para texto)
3. Realiza los cambios
4. Haz clic en **"Actualizar"**

### Eliminar Elemento

1. Pasa el mouse sobre el elemento
2. Haz clic en el icono **"🗑️"**

### Duplicar Elemento

1. Pasa el mouse sobre una gráfica
2. Haz clic en el icono **"📋"**

### Deshacer Cambios

1. Haz clic en **"↶ Deshacer"** en la barra lateral
2. Puedes deshacer múltiples acciones

### Guardar Proyecto

1. Haz clic en **"💾 Guardar"** en la barra lateral
2. El indicador de estado cambiará a "Guardado"

### Exportar a PDF

1. Presiona **Ctrl+P** (Windows) o **Cmd+P** (Mac)
2. Selecciona "Guardar como PDF"
3. Elige la ubicación

---

## 📊 Datos Disponibles

### Fuente
**Banco Mundial (World Bank) - Argentina**

### Período
2015 - 2023

### Métricas

#### PIB - Crecimiento (%)
Variación porcentual anual del Producto Interno Bruto
- Incluye años con crecimiento y contracción
- Muestra impacto de eventos económicos

#### Inflación (%)
Tasa de inflación interanual
- Refleja cambios en nivel de precios
- Período con altas variaciones

#### Desempleo (%)
Tasa de desempleo anual
- Porcentaje de población económicamente activa
- Tendencias del mercado laboral

#### Población (millones)
Población total estimada
- Crecimiento demográfico
- Base para análisis per cápita

---

## 🎨 Personalización

### Cambiar Colores

Edita `static/css/style.css` y modifica las variables CSS:

```css
:root {
    --color-primary: #8fbf8f;           /* Verde principal */
    --color-primary-light: #a8d5a8;     /* Verde claro */
    --color-primary-dark: #6b9b6b;      /* Verde oscuro */
    --color-secondary: #e8d4e8;         /* Pastel secundario */
    --color-accent: #d4c5e8;            /* Pastel acento */
    --color-bg: #f5f3f5;                /* Fondo */
    --color-white: #ffffff;             /* Blanco */
    --color-text: #4a4a4a;              /* Texto principal */
    --color-text-light: #7a7a7a;        /* Texto secundario */
}
```

### Agregar Métricas

Edita `main.py` en la sección `ARGENTINA_DATA`:

```python
ARGENTINA_DATA = {
    "nueva_metrica": {
        "label": "Nombre de la Métrica",
        "data": [
            {"year": 2015, "value": 100},
            {"year": 2016, "value": 102},
            # ... más datos
        ]
    },
    # ... métricas existentes
}
```

Luego, la métrica estará disponible en el modal de gráficas.

### Modificar Tipos de Gráficas

En `static/js/config.js`, edita `CONFIG.CHART_TYPES`:

```javascript
CONFIG.CHART_TYPES = [
    { key: 'line', label: 'Línea' },
    { key: 'bar', label: 'Barras' },
    { key: 'area', label: 'Área' },
    { key: 'doughnut', label: 'Rosca' },
    // Agregar más tipos aquí
]
```

### Cambiar Puerto

Si el puerto 8000 está en uso:

```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

---

## 🔧 Tecnologías

### Backend
| Tecnología | Versión | Propósito |
|-----------|---------|----------|
| **FastAPI** | 0.104.1 | Framework web asincrónico |
| **Uvicorn** | 0.24.0 | Servidor ASGI |
| **Python** | 3.8+ | Lenguaje base |

### Frontend
| Tecnología | Versión | Propósito |
|-----------|---------|----------|
| **React** | 18 | Interfaz de usuario |
| **Chart.js** | 3.9 | Visualización de datos |
| **HTML5** | - | Estructura |
| **CSS3** | - | Estilos |
| **JavaScript** | ES6+ | Lógica |

### Arquitectura
- **Patrón**: Componentes React modularizados
- **Comunicación**: API REST
- **Estado**: React Hooks (useState)
- **Historial**: Sistema manual de versiones

---

## 📝 Estructura de Componentes React

### Header
Encabezado de la página con título y descripción.

### Sidebar
Menú lateral con opciones:
- Agregar Gráfica
- Agregar Texto
- Deshacer
- Guardar
- Indicador de estado

### Workspace
Área principal donde se muestran:
- Gráficas interactivas
- Bloques de texto
- Elementos vacios (inicialmente)

### ChartModal
Modal para crear gráficas:
- Seleccionar métrica
- Seleccionar tipo
- Botones Cancelar/Crear

### TextModal
Modal para agregar texto:
- Textarea para contenido
- Botones Cancelar/Agregar

---

## 📋 Endpoints API

### GET `/api/metrics`
Retorna lista de métricas disponibles.

**Respuesta:**
```json
{
    "metrics": [
        {"key": "gdp", "label": "PIB - Crecimiento (%)"},
        {"key": "inflation", "label": "Inflación (%)"},
        {"key": "unemployment", "label": "Desempleo (%)"},
        {"key": "population", "label": "Población (millones)"}
    ]
}
```

### GET `/api/data/{metric_key}`
Retorna datos de una métrica específica.

**Parámetros:**
- `metric_key`: gdp, inflation, unemployment, o population

**Respuesta:**
```json
{
    "key": "gdp",
    "label": "PIB - Crecimiento (%)",
    "data": [
        {"year": 2015, "value": 2.73},
        {"year": 2016, "value": -2.17},
        ...
    ]
}
```

### GET `/api/all-data`
Retorna todos los datos disponibles.

---

## 🐛 Solución de Problemas

### Error: "No module named 'fastapi'"
```bash
pip install -r requirements.txt
```

### Error: "Port 8000 already in use"
Usa otro puerto:
```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

### No cargan estilos o scripts
Asegúrate de usar `http://localhost:8000` (no `127.0.0.1`)

### Las gráficas no se renderean
- Verifica que Chart.js está cargado
- Abre la consola del navegador (F12)
- Busca errores de JavaScript

### ¿Cómo veo los logs del servidor?
El servidor mostrará los logs en la terminal donde lo ejecutaste.

---

## 💡 Tips y Trucos

### Crear Reportes Estructurados
1. Agrega un título con texto
2. Agrega una gráfica
3. Agrega un subtítulo/descripción
4. Repite para diferentes secciones

### Optimizar Navegador
- Usa Chrome o Firefox para mejor rendimiento
- Abre DevTools (F12) para debuggear
- Limpia caché si hay problemas: Ctrl+Shift+Delete

### Personalizar Estilos
Todos los colores pueden cambiar editando `:root` en `style.css`.
Los cambios se aplican instantáneamente.

### Expandir la Aplicación
La estructura modular permite:
- Agregar nuevos componentes fácilmente
- Extender API con más endpoints
- Implementar persistencia (localStorage o base de datos)

---

## 🚀 Próximas Mejoras Posibles

- [ ] Persistencia con localStorage
- [ ] Exportación directa a PDF (sin imprimir)
- [ ] Más tipos de gráficas
- [ ] Importación de CSV personalizado
- [ ] Tema oscuro/claro
- [ ] Análisis estadístico básico
- [ ] Compartir proyectos
- [ ] Historial más avanzado
- [ ] Integración con base de datos
- [ ] Autenticación de usuarios

---

## 📄 Licencia

Este proyecto está bajo la licencia especificada en el archivo `LICENSE`.

---

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📧 Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio.

---

## 🙏 Agradecimientos

- **Banco Mundial** por los datos públicos de Argentina
- **FastAPI** por el excelente framework
- **React** por la librería de UI
- **Chart.js** por las gráficas interactivas

---

## 📈 Estadísticas del Proyecto

- **Líneas de código**: ~1000
- **Archivos Python**: 1 (main.py)
- **Componentes React**: 5
- **Estilos CSS**: 421 líneas
- **Librerías externas**: 3 (React, ReactDOM, Chart.js)

---

**Versión**: 1.0  
**Última actualización**: 2025  
**Estado**: En desarrollo activo ✨

---

Para más información, lee los comentarios en el código fuente.

¡Disfruta creando tus reportes visuales! 📊
