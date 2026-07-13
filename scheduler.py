import logging
import subprocess
import sys
import time

from apscheduler.schedulers.background import BackgroundScheduler


logging.basicConfig(
    level=logging.INFO,
    filename="logs/scraper.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def job():
    try:
        logging.info("Scheduler: Ejecutando main.py...")
        subprocess.run([sys.executable, "main.py"], check=True)
        logging.info("Scheduler: Proceso main.py terminado correctamente.")
    except Exception as e:
        logging.exception("Error en scheduler al ejecutar main.py: " + str(e))


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", minutes=30)
    scheduler.start()

    logging.info("Scheduler iniciado. Ejecutando cada 30 minutos...")

    job()

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        logging.info("Scheduler detenido.")