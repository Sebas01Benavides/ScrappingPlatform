import os
import psycopg2
from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from pathlib import Path

# Carga el .env desde la raíz
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / '.env')

app = Flask(__name__, template_folder='../frontend')

def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/datos', methods=['GET'])
def obtener_datos():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, nombre, precio FROM juegos;")
        rows = cur.fetchall()
        data = [{"id": r[0], "nombre": r[1], "precio": r[2]} for r in rows]
        cur.close()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if conn: conn.close()

if __name__ == '__main__':
    app.run(port=5000, debug=True)