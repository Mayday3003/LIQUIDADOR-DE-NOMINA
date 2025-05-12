import unittest
import sys
sys.path.append("src")

from model.Empleados import Empleado
from controller.EmpleadosController import EmpleadosController

class test_Empleados(unittest.TestCase):

    def setUpClass():
        """ Se ejecuta una vez antes de las pruebas. Crea la tabla de empleados """
        EmpleadosController.EliminarTabla()
        EmpleadosController.CrearTabla()
        
    def test_insertar(self):
        # Insertar un Usuario en la tabla
        empleado = Empleado(empleado_id="1034990", nombre="Kevin", salario_base="2000000")
        
        EmpleadosController.Insertar(empleado)
        
        #usuario_buscado = EmpleadosController.BuscarEmpleadoPorID(empleado_id="1034990")
        
        #usuario_buscado.es_igual(usuario_prueba)
        
if __name__ == '__main__':
    unittest.main()