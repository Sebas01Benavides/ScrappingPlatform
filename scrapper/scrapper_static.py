import requests
from bs4 import BeautifulSoup
import logging
import os

# Asegurar que la carpeta logs exista
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configuración de logs
logging.basicConfig(level=logging.INFO, filename='logs/scraper.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def scrap_estatico(url):
    # Cabecera para simular un navegador real y evitar errores 403
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            titulos = soup.find_all('h2')
            
            for t in titulos:
                print(f"Encontrado: {t.text.strip()}")
            
            logging.info(f"Scraping estatico exitoso en {url}")
        else:
            logging.error(f"Error {response.status_code} al conectar a {url}")
            
    except Exception as e:
        logging.error(f"Excepción inesperada: {e}")

if __name__ == "__main__":
    # Prueba con Wikipedia
    scrap_estatico("https://www.wikipedia.org")