from flask import Flask, jsonify
from utils.logger_config import setup_logger

app = Flask(__name__)
logger = setup_logger("api_server")

@app.route('/datos', methods=['GET'])
def obtener_datos():
    try:
        logger.info("Solicitud recibida en /datos")
        # Aquí va tu lógica de consulta a Postgres
        return jsonify({"status": "success", "data": []})
    except Exception as e:
        logger.error(f"Error en API: {e}")
        return jsonify({"error": "Error interno"}), 500

if __name__ == '__main__':
    app.run(port=5000)