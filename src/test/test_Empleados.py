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
        
    def test_insertar_1(self):
        empleado = Empleado(empleado_id="1034990", nombre="Kevin", salario_base=2000000)
        EmpleadosController.Insertar(empleado)
        usuario_buscado = EmpleadosController.BuscarEmpleadoPorID(empleado_id="1034990")
        usuario_buscado.es_igual(empleado)
        
    def test_insertar_2(self):
        empleado = Empleado(empleado_id="112530", nombre="juan", salario_base=3000000)
        EmpleadosController.Insertar(empleado)
        usuario_buscado = EmpleadosController.BuscarEmpleadoPorID(empleado_id="112530")
        usuario_buscado.es_igual(empleado)
        
    def test_insertar_3(self):
        empleado = Empleado(empleado_id="154056", nombre="jesus", salario_base=4000000)
        EmpleadosController.Insertar(empleado)
        usuario_buscado = EmpleadosController.BuscarEmpleadoPorID(empleado_id="154056")
        usuario_buscado.es_igual(empleado)
        
        
if __name__ == '__main__':
    unittest.main()