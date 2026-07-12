import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO,
    filename="logs/scraper.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def scrap_estatico(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        titulos = [t.get_text(strip=True) for t in soup.find_all(["h1", "h2"])][:10]

        for titulo in titulos:
            logging.info(f"Encontrado en {url}: {titulo}")

        return {
            "fuente": url,
            "titulos": titulos,
            "total": len(titulos),
            "html_fragment": str(soup)[:1200]
        }

    except Exception as e:
        logging.exception(f"Excepción en scraping estático: {e}")
        return {
            "fuente": url,
            "titulos": [],
            "total": 0,
            "html_fragment": "",
            "error": str(e)
        }


if __name__ == "__main__":
    print(scrap_estatico("https://www.wikipedia.org"))