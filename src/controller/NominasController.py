import sys
sys.path.append(".")
sys.path.append("src")

from src.model.nominas import Nomina
from DB import get_connection  # Importa el nuevo método de conexión

class ControladorNominas:
    def ObtenerCursor():
        connection = get_connection()
        cursor = connection.cursor()
        return cursor

    def crear_tabla():
        cursor = ControladorNominas.ObtenerCursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS nominas (
                empleado_id VARCHAR(50) PRIMARY KEY,
                horas_extras NUMERIC(12, 2),
                tarifa_hora_extra NUMERIC(12, 2),
                otras_deducciones NUMERIC(12, 2),
                deduccion_salud NUMERIC(12, 2),
                deduccion_pension NUMERIC(12, 2),
                total_deducciones NUMERIC(12, 2),
                total_devengado NUMERIC(12, 2),
                total_a_pagar NUMERIC(12, 2)
            );
        """)
        cursor.connection.commit()

    def EliminarTabla():
        cursor = ControladorNominas.ObtenerCursor()
        cursor.execute("DROP TABLE IF EXISTS nominas")
        cursor.connection.commit()

    def InsertarNomina(nomina: Nomina):
        cursor = ControladorNominas.ObtenerCursor()
        cursor.execute("""
            INSERT INTO nominas (empleado_id, horas_extras, tarifa_hora_extra, otras_deducciones, deduccion_salud, deduccion_pension, total_deducciones, total_devengado, total_a_pagar)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (nomina.empleado_id, nomina.horas_extras, nomina.tarifa_hora_extra, nomina.otras_deducciones, nomina.deduccion_salud, nomina.deduccion_pension, nomina.total_deducciones, nomina.total_devengado, nomina.total_a_pagar))
        cursor.connection.commit()

    def BuscarNominaPorEmpleado(empleado_id: int):
        cursor = ControladorNominas.ObtenerCursor()
        cursor.execute("""
            SELECT empleado_id, horas_extras, tarifa_hora_extra, otras_deducciones,
                   deduccion_salud, deduccion_pension, total_deducciones,
                   total_devengado, total_a_pagar
            FROM nominas
            WHERE empleado_id = %s
        """, (empleado_id,))
        fila = cursor.fetchone()
        if fila is None:
            return None
        resultado = Nomina(
            empleado_id=fila[0], horas_extras=fila[1], tarifa_hora_extra=fila[2], otras_deducciones=fila[3],
            deduccion_salud=fila[4], deduccion_pension=fila[5], total_deducciones=fila[6],
            total_devengado=fila[7], total_a_pagar=fila[8]
        )
        return resultado

    def actualizar_campo_nomina(empleado_id, campo, nuevo_valor):
        cursor = ControladorNominas.ObtenerCursor()
        campos_validos = [
            "horas_extras",
            "tarifa_hora_extra",
            "otras_deducciones",
            "deduccion_salud",
            "deduccion_pension",
            "total_deducciones",
            "total_devengado",
            "total_a_pagar"
        ]
        if campo not in campos_validos:
            raise ValueError(f"Campo inválido: {campo}")
        query = f"""
        UPDATE nominas
        SET {campo} = %s
        WHERE empleado_id = %s;
        """
        cursor.execute(query, (nuevo_valor, empleado_id))
        cursor.connection.commit()


