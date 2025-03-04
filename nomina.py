# excepciones.py (Nuevo archivo para excepciones)
class ErrorValorSalario(Exception):
    """Error cuando el salario base no es válido."""
    pass

class ErrorHorasExtras(Exception):
    """Error cuando las horas extras son inválidas."""
    pass

class ErrorTarifaHoraExtra(Exception):
    """Error cuando la tarifa de hora extra es inválida."""
    pass

class ErrorPorcentajeDeduccion(Exception):
    """Error cuando los porcentajes de deducción son inválidos."""
    pass

class ErrorValorDeduccion(Exception):
    """Error cuando las otras deducciones son inválidas."""
    pass

class ErrorAfiliacion(Exception):
    """Error cuando el usuario no tiene afiliación a salud ni pensión."""
    pass

# Constantes para evitar números mágicos
LIMITE_HORAS_EXTRA = 80
PORCENTAJE_MAXIMO_DEDUCCION = 100

def calcular_total_devengado(salario_base, horas_extras, tarifa_hora_extra):
    
    if salario_base <= 0:
        raise ErrorValorSalario("El valor del salario debe ser mayor que cero")
    if horas_extras < 0:
        raise ErrorHorasExtras("Las horas extras no pueden ser negativas")
    if horas_extras > LIMITE_HORAS_EXTRA:
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





    