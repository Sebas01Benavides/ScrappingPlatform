import os
import psycopg2
from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

load_dotenv(dotenv_path=BASE_DIR / ".env")

app = Flask(
    __name__,
    template_folder=str(FRONTEND_DIR),
    static_folder=str(FRONTEND_DIR),
    static_url_path=""
)


def get_db_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/datos", methods=["GET"])
def obtener_datos():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nombre, precio, hash_datos, fuente, fecha_extraccion
            FROM juegos
            ORDER BY id DESC;
        """)
        rows = cur.fetchall()

        data = [
            {
                "id": r[0],
                "nombre": r[1],
                "precio": str(r[2]) if r[2] is not None else "",
                "hash_datos": r[3],
                "fuente": r[4],
                "fecha_extraccion": str(r[5]) if r[5] is not None else ""
            }
            for r in rows
        ]

        cur.close()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    app.run(port=5000, debug=True)