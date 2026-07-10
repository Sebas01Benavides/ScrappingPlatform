from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Iniciar el navegador de la forma más básica
driver = webdriver.Chrome()

try:
    # Navegar a una página específica (Eneba y Halo, por ejemplo)
    driver.get("https://www.eneba.com/latam/xbox-halo-campaign-evolved-windows-xbox-series-x-s-xbox-live-key-global?enb_campaign=Main%20Search&enb_content=search%20dropdown%20-%20products&enb_medium=product%20card&enb_source=https%3A%2F%2Fwww.eneba.com%2F&enb_term=2")
    
    # Pausa básica de 5 segundos para dejar que el JavaScript de la página cargue
    time.sleep(5) 
    
    # Imprimir el título de la pestaña para confirmar que no fuimos bloqueados
    print("Conectado a la pestaña:", driver.title)
    
    # Buscar el nombre del juego usando la etiqueta HTML <h1>
    titulo_juego = driver.find_element(By.TAG_NAME, "h1")
    print("El título extraído es:", titulo_juego.text)

except Exception as e:
    print("Ocurrió un error durante la extracción:", e)

finally:
    # Cerrar el navegador para no dejar procesos abiertos
    driver.quit()