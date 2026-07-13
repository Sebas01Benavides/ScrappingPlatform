import sys
import time
import logging
import subprocess
from apscheduler.schedulers.background import BackgroundScheduler


logging.basicConfig(
    level=logging.INFO,
    filename="logs/scraper.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def job():
    """Ejecuta el proceso principal de scraping."""
    try:
        logging.info("Scheduler: Ejecutando main.py...")
        subprocess.run([sys.executable, "main.py"], check=True)
        logging.info("Scheduler: Proceso main.py terminado correctamente.")
    except Exception as e:
        logging.error(f"Error en scheduler al ejecutar main.py: {e}")


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", minutes=30)
    scheduler.start()

    logging.info("Scheduler iniciado. Ejecutando cada 30 minutos...")
    print("Scheduler iniciado. Ejecutando cada 30 minutos. Presiona Ctrl+C para salir.")

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Scheduler detenido.")