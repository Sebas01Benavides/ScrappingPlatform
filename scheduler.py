from utils.logger_config import setup_logger
import subprocess

logger = setup_logger("scheduler")

def job():
    try:
        logger.info("Scheduler ejecutando proceso...")
        # Llama a tu script de forma segura
        subprocess.run(["python", "scrapper/scrapper_static.py"], check=True)
        logger.info("Proceso terminado correctamente.")
    except Exception as e:
        logger.error(f"Error en scheduler: {e}")

if __name__ == "__main__":
    job()