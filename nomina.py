# excepciones.py (Nuevo archivo para excepciones)
class ErrorValorSalario(Exception):
    """
    Excepción personalizada para valores de salario inválidos.
    """
    def __init__(self, salario):
        super().__init__(f"El valor del salario debe ser mayor que cero. Recibido: {salario}")


class ErrorHorasExtras(Exception):
    """
    Excepción para valores inválidos de horas extras.
    """
    def __init__(self, horas_extras):
        super().__init__(f"No se pueden registrar más de 80 horas extras en un mes según la legislación laboral. Recibido: {horas_extras}")


class ErrorTarifaHoraExtra(Exception):
    """
    Excepción para tarifas de horas extras inválidas.
    """
    def __init__(self, tarifa):
        super().__init__(f"La tarifa de horas extras debe ser mayor que cero. Recibido: {tarifa}")


class ErrorPorcentajeDeduccion(Exception):
    """
    Excepción para porcentajes de deducción fuera del rango 0-100.
    """
    def __init__(self, porcentaje):
        super().__init__(f"El porcentaje de deducción no puede ser mayor al 100%. Recibido: {porcentaje}")


class ErrorValorDeduccion(Exception):
    """
    Excepción para valores de deducción negativos.
    """
    def __init__(self, deduccion):
        super().__init__(f"El valor de la deducción no puede ser negativo. Recibido: {deduccion}")


class ErrorAfiliacion(Exception):
    """
    Excepción para trabajadores sin afiliación a salud y pensión.
    """
    def __init__(self, afiliacion):
        super().__init__("El trabajador debe estar afiliado a salud y pensión para calcular la nómina.")


def calcular_total_devengado(salario_base, horas_extras, tarifa_hora_extra):
    
    if salario_base <= 0:
        raise ErrorValorSalario("El valor del salario debe ser mayor que cero")
    if horas_extras < 0:
        raise ErrorHorasExtras("Las horas extras no pueden ser negativas")
    if horas_extras > 80:
        raise ErrorHorasExtras("Las horas extras no pueden ser mayor a 80")
    if tarifa_hora_extra < 0:
        raise ErrorHorasExtras("La tarifa de hora extra no puede ser negativa")
    
    return salario_base + (horas_extras * tarifa_hora_extra)
    
def calcular_deducciones(salario_base, porcentaje_salud, porcentaje_pension, otras_deducciones):
    
    if porcentaje_salud < 0 or porcentaje_pension < 0:
        raise ErrorPorcentajeDeduccion("Los porcentajes de deducción no pueden ser negativos")
    
    if porcentaje_salud == 0 and porcentaje_pension == 0:
        raise ErrorAfiliacion("Excepción para trabajadores sin afiliación a salud y pensión")
    
    if porcentaje_salud > 100 or porcentaje_pension > 100:
        raise ErrorPorcentajeDeduccion("El porcentaje de deducción no puede ser mayor al 100% del salario")
    
    if otras_deducciones < 0:
        raise ErrorPorcentajeDeduccion("Las otras deducciones no pueden ser negativas")
    
    deduccion_salud = (porcentaje_salud / 100) * salario_base
    deduccion_pension = (porcentaje_pension / 100) * salario_base
    return deduccion_salud + deduccion_pension + otras_deducciones

def calcular_salario_neto(total_devengado, total_deducciones):
    """
    Calcula el salario neto después de aplicar deducciones.

    - Si el total devengado es 0, el salario neto será negativo debido a las deducciones.
    - Si el total devengado es mayor que 0, las deducciones no pueden ser mayores al devengado.
    """
    if total_devengado == 0:
        # Permitir que el salario neto sea negativo si hay deducciones sin devengado
        return -total_deducciones  
    
    if total_deducciones > total_devengado:
        raise ValueError("Las deducciones no pueden ser mayores que el total devengado")
    
    return total_devengado - total_deducciones





    