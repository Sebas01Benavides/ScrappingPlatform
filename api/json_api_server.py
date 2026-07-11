from flask import Flask, jsonify
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

@app.route('/datos', methods=['GET'])
def obtener_datos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos;") # Cambia 'productos' por tu tabla real
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)