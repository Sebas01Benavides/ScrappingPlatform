# Guía de inicio

## Requisitos

- Python 3.9 o superior
- PostgreSQL instalado y activo
- Google Chrome y ChromeDriver, si el scraping dinámico usa Selenium
- Acceso a internet
- Variables de entorno configuradas en `.env`

## Instalación rápida

### 1. Crear entorno virtual

powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

### 2. Instalar dependencias

powershell
pip install -r requirements.txt

### 3. Crear `.env`

DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_bd
AZURE_OPENAI_API_KEY=tu_api_key
AZURE_OPENAI_ENDPOINT=https://voiceflip-openai.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
AZURE_OPENAI_API_VERSION=2024-12-01-preview

## Primera ejecución

Para probar una ejecución única:

powershell:
python main.py

Ese archivo carga variables de entorno, ejecuta el scraping y compara el hash del resultado con la base de datos para insertar o actualizar registros. 

## Ejecución programada

Para dejar el proceso automático:

powershell
python scheduler.py


La automatización con APScheduler está contemplada en el proyecto y debe correr periódicamente. 

## Verificación

Revisar:

- La consola, para ver errores inmediatos.
- `logs/scraper.log`, para confirmar ejecución.
- La base de datos PostgreSQL, para validar inserciones o actualizaciones.
- Los JSON expuestos por la API.
- El dashboard web. 

## Flujo general

1. El scraper obtiene datos del sitio objetivo.
2. `main.py` procesa esos datos.
3. Se calcula un hash del resultado.
4. Se compara con PostgreSQL.
5. Si hay cambios, se inserta o actualiza el registro.
6. Los datos pueden exponerse por API JSON y consumirse desde el dashboard.

## Problemas comunes

- Error de conexión a PostgreSQL: revisar `DATABASE_URL`.
- Error al instalar dependencias: revisar `requirements.txt`.
- Error en Selenium: revisar navegador y driver.
- Scheduler no corre: confirmar que `apscheduler` esté instalado y que `scheduler.py` esté en la raíz del proyecto. 

## Evidencia esperada

Para la entrega final conviene mostrar:

- ejecución de `main.py`,
- ejecución de `scheduler.py`,
- actualización de `logs/scraper.log`,
- respuesta de la API,
- dashboard funcionando. 