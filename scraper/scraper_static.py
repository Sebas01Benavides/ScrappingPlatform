import requests
from bs4 import BeautifulSoup
import logging

# Configuración de logs estandarizada
logging.basicConfig(level=logging.INFO, filename='logs/scraper.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def scrap_estatico(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extraer títulos según necesidad del proyecto
            titulos = soup.find_all('h2')
            for t in titulos:
                logging.info(f"Encontrado en {url}: {t.text.strip()}")
        else:
            logging.error(f"Error {response.status_code} al conectar a {url}")
            
    except Exception as e:
        logging.error(f"Excepción en scraping estático: {e}")

if __name__ == "__main__":
    scrap_estatico("https://www.wikipedia.org")