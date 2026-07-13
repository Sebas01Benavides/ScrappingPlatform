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


def extraer_precio_de_texto(texto):
    match = re.search(r"(\d+[.,]\d{2})", texto)
    if match:
        return f"{float(match.group(1).replace(',', '.')):.2f}"
    return None


def ejecutar_scraping():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    url = "https://www.eneba.com/store/all"
    resultados = []
    downloaded_files = []

    try:
        logging.info("Abriendo listado de Eneba...")
        driver.get(url)
        time.sleep(10)

        downloads = Path("downloads")
        downloads.mkdir(exist_ok=True)

        screenshot_path = downloads / "eneba_listado.png"
        html_path = downloads / "eneba_listado.html"

        driver.save_screenshot(str(screenshot_path))

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        downloaded_files = [
            {
                "nombre": screenshot_path.name,
                "ruta": str(screenshot_path),
                "tipo": "imagen"
            },
            {
                "nombre": html_path.name,
                "ruta": str(html_path),
                "tipo": "html"
            }
        ]

        tarjetas = driver.find_elements(By.CSS_SELECTOR, "a[title][href]")
        logging.info(f"Se detectaron {len(tarjetas)} tarjetas con título.")

        vistos = set()

        for tarjeta in tarjetas:
            titulo = tarjeta.get_attribute("title")
            href_relativo = tarjeta.get_attribute("href")

            if not titulo or not href_relativo:
                continue

            if titulo in vistos:
                continue

            precio = None

            try:
                contenedor = tarjeta.find_element(
                    By.XPATH,
                    "./ancestor::div[contains(@class,'uy1qit') or contains(@class,'igOVC')][1]"
                )
            except Exception:
                contenedor = None

            texto_precio = ""

            if contenedor:
                spans_precio = contenedor.find_elements(
                    By.XPATH,
                    ".//span[contains(text(),'.')]"
                )
                for span in spans_precio:
                    posible = extraer_precio_de_texto(span.text.strip())
                    if posible:
                        texto_precio = posible
                        break

            if not texto_precio:
                continue

            vistos.add(titulo)

            resultados.append({
                "titulo": titulo.strip(),
                "precio": texto_precio,
                "fuente": href_relativo
            })

            logging.info(f"Juego detectado: {titulo.strip()} - {texto_precio}")

            if len(resultados) >= 10:
                break

        logging.info(f"Se extrajeron {len(resultados)} juegos del listado.")

        return {
            "fuente": url,
            "total": len(resultados),
            "items": resultados,
            "downloaded_files": downloaded_files
        }

    except Exception as e:
        logging.exception("Error durante el scraping dinámico: " + str(e))
        return {
            "fuente": url,
            "total": 0,
            "items": [],
            "downloaded_files": downloaded_files
        }

    finally:
        driver.quit()


if __name__ == "__main__":
    resultado = ejecutar_scraping()
    print(resultado)