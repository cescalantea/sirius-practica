import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    return conn

@app.route("/")
def index():
    return jsonify({
        "servicio": "Sirius API",
        "estado": "activo",
        "ambiente": os.environ.get("AMBIENTE")
    })

@app.route("/eventos")
def get_eventos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM eventos_codigo_azul;")
    filas = cur.fetchall()
    cur.close()
    conn.close()

    eventos = []
    for fila in filas:
        eventos.append({
            "id": fila[0],
            "tipo_paciente": fila[1],
            "ubicacion": fila[2],
            "estado": fila[3],
            "fecha_activacion": str(fila[4])
        })

    return jsonify(eventos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)