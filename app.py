from flask import Flask
from src.controller.NominasController import ControladorNominas
from src.view.web.empleados_bp import empleados
from DB import get_connection
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables de entorno desde el archivo .env

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.register_blueprint(empleados)

try:
    conn = get_connection()
    conn.close()
    print("✅ Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

# Elimina las rutas '/' y '/buscar' aquí, ya que están en el blueprint

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
