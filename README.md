# Plataforma de Scraping, API y Dashboard

Proyecto desarrollado en Python para realizar scraping de datos, almacenar cambios en PostgreSQL, exponer resultados en formato JSON mediante Flask y visualizar la información en un dashboard web. Además, incluye un scheduler con APScheduler para ejecutar el proceso automáticamente cada 30 minutos.

## Tecnologías usadas

- Python 3.9+
- Selenium / BeautifulSoup
- PostgreSQL
- Flask
- HTML, CSS, JavaScript
- APScheduler
- Azure OpenAI para generación/adaptación de selectores

## Estructura del proyecto
├── scraper/
│   ├── scraper_dynamic.py
│   └── scraper_static.py
├── data/
│   ├── results.json
│   ├── files.json
│   └── events.json
├── api/
│   └── json_api_server.py
├── llm/
│   └── llm_selector.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── main.js
│   ├── results.js
│   ├── files.js
│   └── calendar.js
├── logs/
│   └── scraper.log
├── downloads/
├── docs/
│   └── guia_inicio.md
├── scheduler.py
├── main.py
├── requirements.txt
├── .env
└── README.md

La estructura base anterior coincide con la organización solicitada en el pdf del proyecto.

## Configuración local

1. Clonar el repositorio.
2. Crear y activar un entorno virtual.
3. Instalar dependencias desde "requirements.txt"
4. Crear el archivo ".env" y agregar las credenciales.
5. Verificar que PostgreSQL esté activo.
6. Ejecutar "main.py" o "scheduler.py".

## Instalación

### Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

### Linux / macOS

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Variables de entorno

Crear un archivo .env en la raíz del proyecto con valores como estos:

DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_bd
AZURE_OPENAI_API_KEY=tu_api_key
AZURE_OPENAI_ENDPOINT=https://voiceflip-openai.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
AZURE_OPENAI_API_VERSION=2024-12-01-preview

Según el pdf del proyecto se pide usar `.env` para proteger claves y considera PostgreSQL y Azure OpenAI dentro de las tecnologías obligatorias.
## Ejecución manual

Para correr el flujo principal una vez:

desde powershell:
python main.py

main.py ejecuta el scraping, calcula un hash de los datos y compara contra la base de datos para insertar o actualizar registros cuando detecta cambios. 

## Ejecución automática

Para iniciar el scheduler:
powershell
python scheduler.py

El proyecto solicita un worker-scheduler que ejecute el proceso cada 30 minutos, y APScheduler es una de las opciones válidas para cumplirlo.

## Logs

Los eventos del scraping y del scheduler se registran en:

logs/scraper.log

El enunciado también exige manejo de logs y excepciones.

## Diseño de la solución

- main.py centraliza la ejecución del scraping y la persistencia. 
- El scraper obtiene datos estructurados del sitio objetivo. 
- PostgreSQL guarda los registros y permite detectar cambios por hash. 
- Flask expone los datos como API JSON para el frontend.
- El dashboard consume esos JSON con JavaScript. 
- Un módulo LLM genera o adapta selectores CSS/XPath dinámicamente. 

## Automatización

El archivo scheduler.py ejecuta main.py una vez al iniciar y luego repite la ejecución cada 30 minutos.

## Entregables incluidos

- Código fuente completo.
- requirements.txt.
- README.md.
- docs/guia_inicio.md.
- Script de automatización scheduler.py.
- Carpeta downloads/.
- Logs en logs/.
- Script del LLM para selectores.