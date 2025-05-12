class Empleado:
    """
    Pertenece a la Capa de Reglas de Negocio (Model)

    Representa a un empleado de la empresa.
    """
    
    def __init__(self, empleado_id: str, nombre: str, salario_base: float):
         self.empleado_id: str = empleado_id
         self.nombre: str = nombre
         self.salario_base: float = salario_base
         
    def es_igual(self, otro_empleado):
        assert self.empleado_id == otro_empleado.empleado_id
        assert self.nombre == otro_empleado.nombre
        assert self.salario_base == otro_empleado.salario_base
        
   
    


