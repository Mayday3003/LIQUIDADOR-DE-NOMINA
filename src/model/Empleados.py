class Empleado:
    """
    Pertenece a la Capa de Reglas de Negocio (Model)

    Representa a un empleado de la empresa.
    """
    
    def __init__(self, empleado_id: str, nombre: str, dni: str, salario_base: float):
        self.empleado_id: str = empleado_id
        self.nombre: str = nombre
        self.dni: str = dni
        self.salario_base: float = salario_base

    def es_igual(self, otro_empleado):
        if not isinstance(otro_empleado, Empleado):
            return False
        return (
            self.empleado_id == otro_empleado.empleado_id and
            self.nombre == otro_empleado.nombre and
            self.dni == otro_empleado.dni and
            self.salario_base == otro_empleado.salario_base
        )





