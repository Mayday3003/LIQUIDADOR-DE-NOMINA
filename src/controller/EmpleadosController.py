import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2
from model.Empleados import Empleado
import secretConfg

class EmpleadosController:
    def ObtenerCursor():
        connection = psycopg2.connect(host=secretConfg.PGHOST, database=secretConfg.PGDATABASE, user=secretConfg.PGUSER, password=secretConfg.PGPASSWORD)
        cursor = connection.cursor()
        return cursor
    
    def CrearTabla():
        cursor = EmpleadosController.ObtenerCursor()
        cursor.execute("""
        CREATE TABLE empleados (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            salario_base DECIMAL NOT NULL
        );
        """)
        cursor.connection.commit()
        
    def EliminarTabla():
        cursor = EmpleadosController.ObtenerCursor()
        cursor.execute("DROP TABLE empleados;")
        cursor.connection.commit()
        
    def Insertar(empleado: Empleado):
        cursor = EmpleadosController.ObtenerCursor()
        cursor.execute(f"""
            INSERT INTO empleados (nombre, salario_base)
            VALUES ('{empleado.nombre}', {empleado.salario_base});
        """)
        cursor.connection.commit()
        
    def BuscarEmpleadoPorID(id) -> Empleado:
        cursor = EmpleadosController.ObtenerCursor()
        cursor.execute(f"""
            SELECT id, nombre, salario_base
            FROM empleados
            WHERE id = {id};
        """)
        fila = cursor.fetchone()
        return Empleado(id=fila[0], nombre=fila[1], salario_base=fila[2])
        
    
        

    
    