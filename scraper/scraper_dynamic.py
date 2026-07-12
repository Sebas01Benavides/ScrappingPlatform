import logging
import re
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


logging.basicConfig(
    level=logging.INFO,
    filename="logs/scraper.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def ejecutar_scraping():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    print("[1] Abriendo navegador...")
    driver = webdriver.Chrome(options=options)

    datos = {
        "titulo": "N/A",
        "precio": "0.00",
        "fuente": "https://www.eneba.com/latam/xbox-halo-campaign-evolved-windows-xbox-series-x-s-xbox-live-key-global"
    }

    try:
        url = "https://www.eneba.com/latam/xbox-halo-campaign-evolved-windows-xbox-series-x-s-xbox-live-key-global"

        print("[2] Entrando al sitio...")
        driver.get(url)

        print("[3] Esperando carga...")
        time.sleep(10)

        titulo = driver.find_element(By.TAG_NAME, "h1")
        datos["titulo"] = titulo.text.strip()
        print("[OK] Título:", datos["titulo"])

        print("[4] Buscando elementos con precio...")
        elementos = driver.find_elements(
            By.XPATH,
            "//*[contains(text(),'$') or contains(text(),'US$')]"
        )

        precios = []

        for e in elementos:
            texto = e.text.strip()

            if texto:
                print("Texto detectado:", texto)
                logging.info("Texto detectado: " + texto)

                match = re.search(r"(\d+[.,]\d{2})", texto)
                if match:
                    precio = float(match.group(1).replace(",", "."))
                    precios.append(precio)

        if len(precios) > 0:
            precio_menor = min(precios)
            datos["precio"] = "{:.2f}".format(precio_menor)
            print("[OK] Precio encontrado:", datos["precio"])
            logging.info("Precio encontrado: " + datos["precio"])
        else:
            print("[X] No se encontró un precio válido.")
            logging.warning("No se encontró un precio válido.")

        downloads = Path("downloads")
        downloads.mkdir(exist_ok=True)

        driver.save_screenshot(str(downloads / "eneba.png"))

        with open(downloads / "pagina.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

    except Exception as e:
        print("[ERROR]", str(e))
        logging.exception("Error durante el scraping dinámico: " + str(e))

    finally:
        print("[5] Cerrando navegador...")
        driver.quit()

    print("[6] Resultado final:", datos)
    return datos


if __name__ == "__main__":
    resultado = ejecutar_scraping()
    print("Resultado del scraping")
    print("----------------------")
    print("Título :", resultado["titulo"])
    print("Precio :", resultado["precio"])