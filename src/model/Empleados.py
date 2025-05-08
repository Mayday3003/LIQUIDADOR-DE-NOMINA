class Empleado:
    """
    Pertenece a la Capa de Reglas de Negocio (Model)

    Representa a un empleado de la empresa.
    """
    
    def __init__(self, id_empleado: int, nombre: str, salario_base: float):
         self.id_empleado = id_empleado
         self.nombre = nombre
         self.salario_base = salario_base
         
    def es_igual(self, otro_empleado):
        assert self.id_empleado == otro_empleado.id_empleado
        assert self.nombre == otro_empleado.nombre
        assert self.salario_base == otro_empleado.salario_base
        
   
    


