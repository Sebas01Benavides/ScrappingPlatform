from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utils.logger_config import setup_logger

logger = setup_logger("scrapper_static")

def ejecutar_scraping():
    driver = None
    try:
        logger.info("Iniciando scraping con Selenium...")
        driver = webdriver.Chrome()
        driver.get("https://www.eneba.com/latam/xbox-halo-campaign-evolved-windows-xbox-series-x-s-xbox-live-key-global?enb_campaign=Main%20Search&enb_content=search%20dropdown%20-%20products&enb_medium=product%20card&enb_source=https%3A%2F%2Fwww.eneba.com%2F&enb_term=2")
        
        time.sleep(5)
        
        titulo_juego = driver.find_element(By.TAG_NAME, "h1")
        logger.info(f"Título extraído: {titulo_juego.text}")

    except Exception as e:
        logger.error(f"Error en el scraper: {e}")
        
    finally:
        if driver:
            driver.quit()
            logger.info("Navegador cerrado.")

if __name__ == "__main__":
    ejecutar_scraping()