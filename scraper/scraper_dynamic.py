from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Configuración de logs
logging.basicConfig(level=logging.INFO, filename='logs/scraper.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def ejecutar_scraping():
    chrome_options = Options()
    # Mantenemos headless, pero con camuflaje
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    # Prevenir detección de Selenium
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    datos = {"titulo": "N/A", "precio": "0.00"}
    
    try:
        logging.info("Iniciando scraping dinámico con camuflaje...")
        driver.get("https://www.eneba.com/latam/xbox-halo-campaign-evolved-windows-xbox-series-x-s-xbox-live-key-global")
        
        wait = WebDriverWait(driver, 20)
        
        # Extraer título
        titulo_elemento = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        datos["titulo"] = titulo_elemento.text.strip()
        
        # Selector de precio específico para el contenedor de Eneba
        # El precio suele estar dentro de un span con clase que contiene "payment-cost"
        precio_elemento = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "span[class*='payment-cost']")
        ))
        
        # Limpiar el texto: quitar símbolo de moneda y espacios
        raw_price = precio_elemento.text
        # Reemplazamos caracteres no numéricos excepto el punto decimal
        datos["precio"] = "".join(c for c in raw_price if c.isdigit() or c == '.').strip()
            
    except Exception as e:
        logging.error(f"Error en el scraping: {e}")
    finally:
        driver.quit()
        
    return datos