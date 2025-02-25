class ErrorValorSalario(Exception):
    """Excepción personalizada cuando el salario base es menor o igual a cero."""
    
def calcular_total_devengado(salario_base, horas_extras, tarifa_hora_extra):
    
    if salario_base <= 0:
        raise ErrorValorSalario("El valor del salario debe ser mayor que cero")
    
    return  salario_base + (horas_extras * tarifa_hora_extra)

def calcular_deducciones(salario_base, porcentaje_salud, porcentaje_pension, otras_deducciones):
    deduccion_salud = (porcentaje_salud / 100) * salario_base
    deduccion_pension = (porcentaje_pension / 100) * salario_base
    return deduccion_salud + deduccion_pension + otras_deducciones

def calcular_salario_neto(total_devengado, total_deducciones):
    return total_devengado - total_deducciones





    