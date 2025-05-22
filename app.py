from flask import Flask, render_template, request
from src.controller.NominasController import ControladorNominas
from blueprints.empleados_bp import empleados
from DB import get_connection

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.register_blueprint(empleados)

try:
    conn = get_connection()
    conn.close()
    print("✅ Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    empleado_id = request.form.get('empleado_id')
    resultado = ControladorNominas.BuscarNominaPorEmpleado(empleado_id)
    if resultado:
        return render_template('buscar.html', nomina=resultado)
    else:
        return render_template('buscar.html', error="No se encontró la nómina para el empleado.")

if __name__ == '__main__':
    app.run(debug=True)
