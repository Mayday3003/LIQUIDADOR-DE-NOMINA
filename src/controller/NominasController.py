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
        
    def InsertarNomina(nomina: Nomina):
        cursor = ControladorNominas.ObtenerCursor()
        cursor.execute(f"""insert into nominas (empleado_id, horas_extras, tarifa_hora_extra, otras_deducciones, deduccion_salud, deduccion_pension, total_deducciones, total_devengado, total_a_pagar)
                        values ('{nomina.empleado_id}', '{nomina.horas_extras}', '{nomina.tarifa_hora_extra}', '{nomina.otras_deducciones}', '{nomina.deduccion_salud}', '{nomina.deduccion_pension}',
                        '{nomina.total_deducciones}', '{nomina.total_devengado}', '{nomina.total_a_pagar}')""")
        cursor.connection.commit()
        
    def BuscarNominaPorEmpleado(empleado_id: int):
        cursor = ControladorNominas.ObtenerCursor()

        cursor.execute(f"""
        SELECT empleado_id, horas_extras, tarifa_hora_extra, otras_deducciones,
               deduccion_salud, deduccion_pension, total_deducciones,
               total_devengado, total_a_pagar
        FROM nominas
        WHERE empleado_id = '{empleado_id}'
    """)
        fila = cursor.fetchone()
        if fila is None:
            return None
        resultado = Nomina(empleado_id=fila[0], horas_extras=fila[1], tarifa_hora_extra=fila[2], otras_deducciones=fila[3],
               deduccion_salud=fila[4], deduccion_pension=fila[5], total_deducciones=fila[6],
               total_devengado=fila[7], total_a_pagar=fila[8])
        
        return resultado
    
    def ModificarNomina(nomina: Nomina):
        cursor = ControladorNominas.ObtenerCursor()

        # Usar parámetros en la consulta para evitar inyección SQL
        query = """
        UPDATE nominas
        SET
            horas_extras = %s,
            tarifa_hora_extra = %s,
            otras_deducciones = %s,
            deduccion_salud = %s,
            deduccion_pension = %s,
            total_deducciones = %s,
            total_devengado = %s,
            total_a_pagar = %s
        WHERE empleado_id = %s
        """
        values = (
            nomina.horas_extras,
            nomina.tarifa_hora_extra,
            nomina.otras_deducciones,
            nomina.deduccion_salud,
            nomina.deduccion_pension,
            nomina.total_deducciones,
            nomina.total_devengado,
            nomina.total_a_pagar,
            nomina.empleado_id
        )

        try:
            # Ejecutar la actualización
            cursor.execute(query, values)
            
            # Confirmar la transacción
            cursor.connection.commit()

            # Verificar si se actualizó alguna fila
            if cursor.rowcount == 0:
                print("Empleado no encontrado.")
                return None
            
            # Obtener los datos actualizados
            cursor.execute("SELECT * FROM nominas WHERE empleado_id = %s", (nomina.empleado_id,))
            fila = cursor.fetchone()
            
            if fila:
                return Nomina(
                    empleado_id=fila[0],
                    horas_extras=fila[1],
                    tarifa_hora_extra=fila[2],
                    otras_deducciones=fila[3],
                    deduccion_salud=fila[4],
                    deduccion_pension=fila[5],
                    total_deducciones=fila[6],
                    total_devengado=fila[7],
                    total_a_pagar=fila[8]
                )
            else:
                print("No se encontraron resultados actualizados.")
                return None
        except Exception as e:
            # Manejo de errores
            print(f"Error al modificar la nómina: {e}")
            return None
        
            
    
    