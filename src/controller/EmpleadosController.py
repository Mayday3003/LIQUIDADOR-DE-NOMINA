import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2
from model.Empleados import Empleado
import secretConfg

class EmpleadosController:
    
    def CrearTabla():
        cursor = EmpleadosController.ObtenerCursor()
        
        with open( "sql/crear-Empleado.sql", "r") as archivo:
            consulta = archivo.read()
            
        cursor.execute(consulta)
        cursor.connection.commit()
            
    def EliminarTabla():
        cursor = EmpleadosController.ObtenerCursor()
        cursor.execute("""DROP TABLE IF EXISTS empleados""")
        cursor.connection.commit()
        
    def Insertar(empleado: Empleado):
        cursor = EmpleadosController.ObtenerCursor()
        cursor.execute(f"""insert into empleados (empleado_id, nombre, salario_base)
                        values ('{empleado.empleado_id}', '{empleado.nombre}', '{empleado.salario_base}')""")
        
        cursor.connection.commit()
        
    def BuscarEmpleadoPorID(empleado_id):   
        cursor = EmpleadosController.ObtenerCursor()
        cursor.execute(f"""select empleado_id, nombre, salario_base
        from empleados where empleado_id = '{empleado_id}'""")
        
        fila = cursor.fetchone()
        print(f"Fila obtenida: {fila}")  # Para depuración
        
        if fila:  # Si la consulta devuelve una fila válida
            # Convertir salario_base de Decimal a float
            salario_base = float(fila[2])  # fila[2] es el salario_base
            resultado = Empleado(fila[0], fila[1], salario_base)
            return resultado
        else:
            print(f"No se encontró el empleado con ID {empleado_id}")  # Mensaje si no se encuentra
            return None
        
    def actualizar_campo_empleado(empleado_id, campo, nuevo_valor):
        cursor = EmpleadosController.ObtenerCursor()
        
        campos_validos = [
        "empleado_id",
        "nombre",
        "salario_base"]
        
        if campo not in campos_validos:
                raise ValueError(f"Campo inválido: {campo}")

        # Consulta dinámica (campo ya fue validado)
        query = f"""
        UPDATE empleados
        SET {campo} = %s
        WHERE empleado_id = %s;
        """
        cursor.execute(query, (nuevo_valor, empleado_id))
        cursor.connection.commit()
        

    def ObtenerCursor():
        connection = psycopg2.connect(host=secretConfg.PGHOST, database=secretConfg.PGDATABASE, user=secretConfg.PGUSER, password=secretConfg.PGPASSWORD)
        cursor = connection.cursor()
        return cursor
    
        

    
    