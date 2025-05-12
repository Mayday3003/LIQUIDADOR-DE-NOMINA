class Nomina:
    def __init__(self, empleado_id, horas_extras: int, tarifa_hora_extra: float, otras_deducciones: float, deduccion_salud: float, deduccion_pension: float, total_deducciones: float, total_devengado: float, total_a_pagar: float):   
        self.empleado_id = empleado_id
        self.horas_extras = horas_extras
        self.tarifa_hora_extra = tarifa_hora_extra
        self.otras_deducciones = otras_deducciones
        self.deduccion_salud = deduccion_salud
        self.deduccion_pension = deduccion_pension
        self.total_deducciones = total_deducciones
        self.total_devengado = total_devengado
        self.total_a_pagar = total_a_pagar
        
    def es_igual(self, otra_nomina):  
        assert self.empleado_id == otra_nomina.empleado_id
        assert self.horas_extras == otra_nomina.horas_extras
        assert self.tarifa_hora_extra == otra_nomina.tarifa_hora_extra
        assert self.otras_deducciones == otra_nomina.otras_deducciones
        assert self.deduccion_salud == otra_nomina.deduccion_salud
        assert self.deduccion_pension == otra_nomina.deduccion_pension
        assert self.total_deducciones == otra_nomina.total_deducciones
        assert self.total_devengado == otra_nomina.total_devengado
        assert self.total_a_pagar == otra_nomina.total_a_pagar
    