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
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS nominas (
                id SERIAL PRIMARY KEY,
                empleado_id INTEGER REFERENCES empleados(id),
                horas_extras INTEGER,
                tarifa_hora_extra INTEGER,
                otras_deducciones INTEGER,
                deduccion_salud INTEGER,
                deduccion_pension INTEGER,
                total_deducciones INTEGER,
                total_devengado INTEGER,
                total_a_pagar INTEGER
            );
        """)
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
        
        
    
    
   
    

    
