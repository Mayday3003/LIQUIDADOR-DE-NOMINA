from flask import Blueprint, render_template, request, redirect, url_for, flash
from DB import get_connection

empleados = Blueprint('empleados', __name__)

def calcular_neto(sueldo, deducciones):
    return float(sueldo) - float(deducciones)

@empleados.route('/')
def index():
    return render_template('index.html')

@empleados.route('/buscar', methods=['GET', 'POST'])
def buscar():
    empleados_encontrados = []
    criterio = ""
    if request.method == 'POST':
        criterio = request.form.get('criterio', '').strip()
        query = """
            SELECT id, nombre, dni, sueldo, deducciones, neto
            FROM empleados
            WHERE nombre ILIKE %s OR dni ILIKE %s
            ORDER BY nombre
        """
        like_criterio = f"%{criterio}%"
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, (like_criterio, like_criterio))
        empleados_encontrados = cur.fetchall()
        cur.close()
        conn.close()
    return render_template('buscar.html', empleados=empleados_encontrados, criterio=criterio)

@empleados.route('/insertar', methods=['GET', 'POST'])
def insertar():
    errores = {}
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        dni = request.form.get('dni', '').strip()
        sueldo = request.form.get('sueldo', '').strip()
        deducciones = request.form.get('deducciones', '0').strip() or '0'

        if not nombre:
            errores['nombre'] = "El nombre es obligatorio."
        if not dni:
            errores['dni'] = "El DNI es obligatorio."
        if not sueldo or not sueldo.replace('.', '', 1).isdigit() or float(sueldo) < 0:
            errores['sueldo'] = "El sueldo debe ser un número mayor o igual a 0."
        if not deducciones.replace('.', '', 1).isdigit() or float(deducciones) < 0:
            errores['deducciones'] = "Las deducciones deben ser un número mayor o igual a 0."

        if not errores:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT 1 FROM empleados WHERE dni = %s", (dni,))
            if cur.fetchone():
                errores['dni'] = "El DNI ya existe."
            cur.close()
            conn.close()

        if not errores:
            neto = float(sueldo) - float(deducciones)
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO empleados (nombre, dni, sueldo, deducciones, neto) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                (nombre, dni, sueldo, deducciones, neto)
            )
            nuevo_id = cur.fetchone()["id"]  
            conn.commit()
            cur.close()
            conn.close()
            flash(f"Empleado {nombre} creado con ID {nuevo_id}")
            return redirect(url_for('empleados.buscar'))
        else:
            return render_template('insertar.html', errores=errores, form=request.form)
    return render_template('insertar.html', errores=errores, form={})

@empleados.route('/modificar/<int:empleado_id>', methods=['GET', 'POST'])
def modificar(empleado_id):
    errores = {}
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, dni, sueldo, deducciones FROM empleados WHERE id = %s", (empleado_id,))
    empleado = cur.fetchone()
    if not empleado:
        cur.close()
        conn.close()
        flash("Empleado no encontrado.")
        return redirect(url_for('empleados.buscar'))
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        dni = request.form.get('dni', '').strip()
        sueldo = request.form.get('sueldo', '').strip()
        deducciones = request.form.get('deducciones', '0').strip() or '0'

        # Validaciones
        if not nombre:
            errores['nombre'] = "El nombre es obligatorio."
        if not dni:
            errores['dni'] = "El DNI es obligatorio."
        if not sueldo or not sueldo.replace('.', '', 1).isdigit() or float(sueldo) < 0:
            errores['sueldo'] = "El sueldo debe ser un número mayor o igual a 0."
        if not deducciones.replace('.', '', 1).isdigit() or float(deducciones) < 0:
            errores['deducciones'] = "Las deducciones deben ser un número mayor o igual a 0."

        if not errores:
            cur.execute("SELECT id FROM empleados WHERE dni = %s AND id != %s", (dni, empleado_id))
            if cur.fetchone():
                errores['dni'] = "El DNI ya existe en otro empleado."

        if not errores:
            neto = calcular_neto(sueldo, deducciones)
            cur.execute(
                "UPDATE empleados SET nombre=%s, dni=%s, sueldo=%s, deducciones=%s, neto=%s WHERE id=%s",
                (nombre, dni, sueldo, deducciones, neto, empleado_id)
            )
            conn.commit()
            cur.close()
            conn.close()
            flash("Empleado modificado correctamente.")
            return redirect(url_for('empleados.buscar'))
        else:
            cur.close()
            conn.close()
            return render_template('modificar.html', errores=errores, form=request.form, empleado_id=empleado_id)
    cur.close()
    conn.close()
    return render_template('modificar.html', errores=errores, form=empleado, empleado_id=empleado_id)

@empleados.route('/eliminar/<int:empleado_id>', methods=['POST'])
def eliminar(empleado_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT nombre, dni FROM empleados WHERE id = %s", (empleado_id,))
    empleado = cur.fetchone()
    if not empleado:
        cur.close()
        conn.close()
        flash("Empleado no encontrado.")
        return redirect(url_for('empleados.buscar'))
    cur.execute("DELETE FROM empleados WHERE id = %s", (empleado_id,))
    conn.commit()
    cur.close()
    conn.close()
    flash(f"Empleado {empleado['nombre']} (DNI: {empleado['dni']}) eliminado correctamente.")
    return redirect(url_for('empleados.buscar'))

@empleados.route('/eliminar', methods=['GET', 'POST'])
def eliminar_manual():
    if request.method == 'POST':
        empleado_id = request.form.get('empleado_id')
        if empleado_id:
            return redirect(url_for('empleados.eliminar', empleado_id=empleado_id))
    return render_template('eliminar.html')

@empleados.route('/crear_tablas', methods=['POST'])
def crear_tablas():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                dni VARCHAR(20) NOT NULL UNIQUE,
                sueldo NUMERIC(12,2) NOT NULL,
                deducciones NUMERIC(12,2) DEFAULT 0,
                neto NUMERIC(12,2) NOT NULL
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        flash("Tablas creadas correctamente.")
    except Exception as e:
        flash(f"Error al crear tablas: {e}")
    return redirect(url_for('empleados.index'))
