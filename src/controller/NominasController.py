import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2
from model.nominas import Nomina 
import secretConfg

class ControladorNominas:
    
    def ObtenerCursor():
        connection = psycopg2.connect(host=secretConfg.PGHOST, database=secretConfg.PGDATABASE, user=secretConfg.PGUSER, password=secretConfg.PGPASSWORD)
        cursor = connection.cursor()
        return cursor
    
    def crear_tabla():
        """ Crea la tabla de nóminas en la BD """
        cursor = ControladorNominas.ObtenerCursor()
        
        with open("sql/crear-Nominas.sql", "r") as archivo:
            consulta = archivo.read()
            
        cursor.execute(consulta)
        cursor.connection.commit()
        
    def EliminarTabla():
        """ Borra la tabla de nóminas de la BD """
        cursor = ControladorNominas.ObtenerCursor()

        cursor.execute("DROP TABLE IF EXISTS nominas")
        cursor.connection.commit()
        
    def InsertarNomina(empleado_id, horas_extras, tarifa_hora_extra, otras_deducciones, deduccion_salud, deduccion_pension):
        """ Recibe los valores necesarios y los inserta en la tabla de nóminas """
        cursor = ControladorNominas.ObtenerCursor()

        # Obtener el salario base del empleado desde la tabla empleados
        cursor.execute("""SELECT salario_base FROM empleados WHERE id = %s""", (empleado_id,))
        resultado = cursor.fetchone()

        # Si no se encuentra el empleado
        if resultado is None:
            print(f"Empleado con ID {empleado_id} no encontrado.")
            return

        salario_base = resultado[0]

        # Calcular total de deducciones y total devengado
        total_deducciones = deduccion_salud + deduccion_pension + otras_deducciones
        total_devengado = salario_base + (horas_extras * tarifa_hora_extra)
        total_a_pagar = total_devengado - total_deducciones

        # Insertar los datos en la tabla de nominas
        cursor.execute("""
            INSERT INTO nominas (empleado_id, horas_extras, tarifa_hora_extra, otras_deducciones, 
                                 deduccion_salud, deduccion_pension, total_deducciones, 
                                 total_devengado, total_a_pagar)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (empleado_id, horas_extras, tarifa_hora_extra, otras_deducciones, deduccion_salud, 
              deduccion_pension, total_deducciones, total_devengado, total_a_pagar))
        
        # Confirmar los cambios en la base de datos
        cursor.connection.commit()
        print("Nómina insertada correctamente.")   #EN PROCESO
        
    def BuscarNominaPorEmpleado(empleado_id: int):
        """ Busca una nómina de un empleado por su ID """
        cursor = ControladorNominas.ObtenerCursor()

        cursor.execute("""
            SELECT * FROM nominas WHERE empleado_id = %s
        """, (empleado_id,))
        
        fila = cursor.fetchone()
        if fila:
            return Nomina(
                id=fila[0], empleado_id=fila[1], horas_extras=fila[2],
                tarifa_hora_extra=fila[3], otras_deducciones=fila[4],
                deduccion_salud=fila[5], deduccion_pension=fila[6],
                total_deducciones=fila[7], total_devengado=fila[8],
                total_a_pagar=fila[9]
            )
        return None
    
import psycopg2
import sys
sys.path.append("..")  # Añadimos el directorio raíz del proyecto al sys.path
import secretConfg

def probar_conexion():
    """Verifica si la conexión a la base de datos es exitosa."""
    try:
        # Intentamos establecer la conexión
        connection = psycopg2.connect(
            host=secretConfg.PGHOST,
            database=secretConfg.PGDATABASE,
            user=secretConfg.PGUSER,
            password=secretConfg.PGPASSWORD
        )
        print("Conexión exitosa a la base de datos.")
        connection.close()  # Cerramos la conexión después de la prueba
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

# Llamamos a la función para probar la conexión
probar_conexion()
        

    
    
   
    

    
