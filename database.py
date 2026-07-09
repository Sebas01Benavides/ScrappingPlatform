import psycopg2
import os
from dotenv import load_dotenv

# Esto busca el archivo .env en la raíz y carga las variables
load_dotenv()

def get_db_connection():
    try:
        # Se conecta usando las variables definidas en tu .env
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")
        return None