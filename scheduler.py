import time
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

def job():
    print("Iniciando ciclo de scraping...")
    # Ajustado a tus nombres de archivo y carpeta
    subprocess.run(["python", "scrapper/scrapper_static.py"])
    subprocess.run(["python", "scrapper/scrapper_dynamic.py"])
    print("Ciclo de scraping finalizado.")

scheduler = BlockingScheduler()
# Ejecución cada 30 minutos
scheduler.add_job(job, 'interval', minutes=30)

print("Scheduler iniciado. Presiona Ctrl+C para salir.")
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass