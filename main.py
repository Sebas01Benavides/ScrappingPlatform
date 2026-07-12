import hashlib, json, logging, os, psycopg2
from dotenv import load_dotenv
from scraper.scraper_dynamic import ejecutar_scraping

load_dotenv()
logging.basicConfig(level=logging.INFO, filename='logs/scraper.log', format='%(asctime)s - %(message)s')

def main():
    datos = ejecutar_scraping()
    print(f"Datos recibidos: {datos}")
    nuevo_hash = hashlib.sha256(json.dumps(datos, sort_keys=True).encode()).hexdigest()
    
    conn = psycopg2.connect(os.getenv("DATABASE_URL")) # Asegúrate de tener esta variable en .env
    cur = conn.cursor()
    
    # 1. Obtenemos el hash actual de la BD
    cur.execute("SELECT hash_datos FROM juegos WHERE nombre = %s", (datos["titulo"],))
    resultado = cur.fetchone()
    
    # 2. Lógica de comparación (Sección 8)
    if not resultado:
        cur.execute("INSERT INTO juegos (nombre, hash_datos) VALUES (%s, %s)", (datos["titulo"], nuevo_hash))
        logging.info(f"Nuevo registro insertado: {datos['titulo']}")
    elif resultado[0] != nuevo_hash:
        cur.execute("UPDATE juegos SET hash_datos = %s WHERE nombre = %s", (nuevo_hash, datos["titulo"]))
        logging.info(f"Registro actualizado: {datos['titulo']}")
        
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()