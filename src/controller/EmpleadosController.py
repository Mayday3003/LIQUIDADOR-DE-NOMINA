import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2
from model.Empleados import Empleado
from DB import get_connection
from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno desde el archivo .env

class EmpleadosController:
    
    @staticmethod
    def CrearTabla():
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

    @staticmethod
    def EliminarTabla():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS empleados")
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def Insertar(empleado: Empleado):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO empleados (id, nombre, dni, sueldo, deducciones, neto)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (empleado.empleado_id, empleado.nombre, empleado.dni, empleado.salario_base, 0, empleado.salario_base))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def BuscarEmpleadoPorID(empleado_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, nombre, dni, sueldo FROM empleados WHERE id = %s", (empleado_id,))
        fila = cur.fetchone()
        cur.close()
        conn.close()
        if fila:
            return Empleado(
                empleado_id=fila["id"],
                nombre=fila["nombre"],
                dni=fila["dni"],
                salario_base=fila["sueldo"]
            )
        return None

    @staticmethod
    def ActualizarCampoEmpleado(empleado_id, campo, nuevo_valor):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"UPDATE empleados SET {campo} = %s WHERE id = %s", (nuevo_valor, empleado_id))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def Eliminar(empleado_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM empleados WHERE id = %s", (empleado_id,))
        conn.commit()
        cur.close()
        conn.close()




