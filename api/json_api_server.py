import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

app = Flask(__name__, template_folder=str(BASE_DIR / "frontend"))


def get_db_connection():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("No se encontró DATABASE_URL en el .env")
    return psycopg2.connect(database_url)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/datos", methods=["GET"])
def obtener_datos():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, nombre, precio, hash_datos, fuente, fecha_extraccion FROM juegos ORDER BY id DESC"
        )
        rows = cur.fetchall()

        data = []
        for row in rows:
            data.append({
                "id": row[0],
                "nombre": row[1],
                "precio": float(row[2]) if row[2] is not None else None,
                "hash_datos": row[3],
                "fuente": row[4],
                "fecha_extraccion": str(row[5])
            })

        cur.close()
        return jsonify({"status": "success", "data": data})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)