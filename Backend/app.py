from flask import Flask, jsonify
from flask_cors import CORS

# Crear la aplicación Flask
app = Flask(__name__)
CORS(app)

# Configuración para evitar problemas con acentos (opcional)
app.config['JSON_AS_ASCII'] = False

# -----------------------------------
# 🔹 Datos simulados (en formato JSON)
# -----------------------------------
estudiantes = [
    {"id": 1, "nombre": "Gabriela Lanchimba", "edad": 20, "carrera": "Ingenieria en Software", "semestre": 4},
    {"id": 2, "nombre": "Fernanda Alcusir", "edad": 20, "carrera": "Ingenieria Industrial", "semestre": 4},
    {"id": 3, "nombre": "Anthony Bedoya", "edad": 20, "carrera": "Diseno Grafico", "semestre": 4},
    {"id": 4, "nombre": "Nahim Marulanda", "edad": 21, "carrera": "Ingenieria en Software", "semestre": 3}
]

# ===================================================
# 1️⃣ GET / → Ruta principal (descripcion general)
# ===================================================
@app.route('/')
def home():
    return jsonify({
        "descripcion": "Bienvenido al Web Service del Instituto. Aqui puedes consultar informacion de estudiantes.",
        "endpoints": {
            "GET /api/saludo": "Devuelve un saludo especial",
            "GET /api/estudiantes": "Lista todos los estudiantes",
            "GET /api/estudiantes/<id>": "Obtiene un estudiante por su ID",
            "GET /api/estudiantes/carrera/<carrera>": "Filtra estudiantes por carrera"
        }
    })

# ===================================================
# 2️⃣ GET /api/saludo → Mensaje de saludo (endpoint propio)
# ===================================================
@app.route('/api/saludo', methods=['GET'])
def saludo():
    return jsonify({
        "saludo": " Holaaa Ing y guaguas! Bienvenidos al Web Service Flask",
        "mensaje": "Este es el endpoint de saludo , donde empieza todo la chamba!"
    })

# ===================================================
# 3️⃣ GET /api/estudiantes → Lista todos los estudiantes
# ===================================================
@app.route('/api/estudiantes', methods=['GET'])
def listar_estudiantes():
    return jsonify(estudiantes)

# ===================================================
# 4️⃣ GET /api/estudiantes/<id> → Obtener estudiante por ID
# ===================================================
@app.route('/api/estudiantes/<int:id>', methods=['GET'])
def obtener_estudiante(id):
    estudiante = next((e for e in estudiantes if e["id"] == id), None)
    if estudiante:
        return jsonify(estudiante)
    else:
        return jsonify({"error": f"No se encontro ningun estudiante con ID {id}"}), 404

# ===================================================
# 5️⃣ GET /api/estudiantes/carrera/<carrera> → Filtrar por carrera
# ===================================================
@app.route('/api/estudiantes/carrera/<string:carrera>', methods=['GET'])
def filtrar_por_carrera(carrera):
    filtrados = [e for e in estudiantes if e["carrera"].lower() == carrera.lower()]
    if filtrados:
        return jsonify(filtrados)
    else:
        return jsonify({"mensaje": f"No se encontraron estudiantes en la carrera '{carrera}'"}), 404

# ===================================================
# Ejecutar el servidor
# ===================================================
if __name__ == '__main__':
    app.run(port=3000, debug=True)
