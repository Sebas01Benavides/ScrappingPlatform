import hashlib
import json
import logging
import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv

from scraper.scraper_dynamic import ejecutar_scraping
from scraper.scraper_static import scrap_estatico
from llm.llm_selector import obtener_selector


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
DOWNLOADS_DIR = BASE_DIR / "downloads"

DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
DOWNLOADS_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_DIR / "scraper.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_connection():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("No se encontró DATABASE_URL en el archivo .env")
    return psycopg2.connect(database_url)


def save_json(filename, data):
    filepath = DATA_DIR / filename
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def guardar_log_db(conn, estado, mensaje):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO logs_ejecucion (estado, mensaje) VALUES (%s, %s)",
            (estado, mensaje)
        )


def procesar_juego(conn, datos):
    nuevo_hash = hashlib.sha256(
        json.dumps(datos, sort_keys=True).encode("utf-8")
    ).hexdigest()

    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, hash_datos FROM juegos WHERE nombre = %s",
            (datos["titulo"],)
        )
        resultado = cur.fetchone()

        if not resultado:
            cur.execute(
                """
                INSERT INTO juegos (nombre, precio, hash_datos, fuente)
                VALUES (%s, %s, %s, %s)
                """,
                (
                    datos["titulo"],
                    datos.get("precio"),
                    nuevo_hash,
                    datos.get("fuente")
                )
            )
            logging.info(f"Nuevo registro insertado: {datos['titulo']}")
            return "insertado"

        if resultado[1] != nuevo_hash:
            cur.execute(
                """
                UPDATE juegos
                SET precio = %s, hash_datos = %s, fuente = %s
                WHERE id = %s
                """,
                (
                    datos.get("precio"),
                    nuevo_hash,
                    datos.get("fuente"),
                    resultado[0]
                )
            )
            logging.info(f"Registro actualizado: {datos['titulo']}")
            return "actualizado"

        logging.info(f"Sin cambios para: {datos['titulo']}")
        return "sin_cambios"


def main():
    conn = None

    try:
        logging.info("Iniciando proceso principal de scraping...")

        resultado_estatico = scrap_estatico("https://www.wikipedia.org")
        resultado_dinamico = ejecutar_scraping()

        selector_resultado = obtener_selector(
            resultado_estatico.get("html_fragment", ""),
            "el selector CSS de los títulos h2 de la página"
        )

        selector_final = None
        if isinstance(selector_resultado, dict):
            selector_final = selector_resultado.get("selector")
        else:
            selector_final = selector_resultado

        save_json("results.json", {
            "static": resultado_estatico,
            "dynamic": resultado_dinamico,
            "selector_llm": selector_resultado
        })

        save_json("files.json", resultado_dinamico.get("downloaded_files", []))

        save_json("events.json", {
            "status": "running",
            "message": "Proceso ejecutado"
        })

        conn = get_connection()
        accion = procesar_juego(conn, resultado_dinamico)

        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO resultados_scraping (fuente, titulo, url_origen)
                VALUES (%s, %s, %s)
                """,
                (
                    resultado_dinamico.get("fuente"),
                    resultado_dinamico.get("titulo"),
                    resultado_dinamico.get("fuente")
                )
            )

        guardar_log_db(conn, "EXITO", f"Proceso completado: {accion}")
        conn.commit()

        save_json("events.json", {
            "status": "success",
            "db_action": accion,
            "selector_sugerido": selector_final,
            "selector_resultado": selector_resultado
        })

        logging.info("Proceso finalizado correctamente.")

    except Exception as e:
        logging.exception(f"Error en main.py: {e}")

        save_json("events.json", {
            "status": "error",
            "message": str(e)
        })

        if conn:
            conn.rollback()
            try:
                guardar_log_db(conn, "ERROR", str(e))
                conn.commit()
            except Exception:
                pass

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()