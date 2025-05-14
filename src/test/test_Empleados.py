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
        
    def test_modificar_empleado_1(self):
        empleado_original = Empleado(empleado_id="1034990", nombre="Kevin", salario_base=2000000)
        EmpleadosController.Insertar(empleado_original)
        EmpleadosController.EliminarTabla()
        EmpleadosController.CrearTabla()
        empleado_modificado = Empleado(empleado_id="245690", nombre="Alberto", salario_base=500000)
        EmpleadosController.Insertar(empleado_modificado)
        
    def test_modificar_empleado_2(self):
        empleado_original = Empleado(empleado_id="112530", nombre="juan", salario_base=3000000)
        EmpleadosController.Insertar(empleado_original)
        EmpleadosController.EliminarTabla()
        EmpleadosController.CrearTabla()
        empleado_modificado = Empleado(empleado_id="714509", nombre="santiago", salario_base=600000)
        EmpleadosController.Insertar(empleado_modificado)
        
    def test_modificar_empleado_3(self):
        empleado_original = Empleado(empleado_id="154056", nombre="jesus", salario_base=4000000)
        EmpleadosController.Insertar(empleado_original)
        EmpleadosController.EliminarTabla()
        EmpleadosController.CrearTabla()
        empleado_modificado = Empleado(empleado_id="045690", nombre="valentina", salario_base=700000)
        EmpleadosController.Insertar(empleado_modificado)
        
    def test_buscado_1(self):
        empleado_id = "334"
        esperado = Empleado(empleado_id="334", nombre="Esteban", salario_base=5000000)
        EmpleadosController.Insertar(esperado)
        resultado = EmpleadosController.BuscarEmpleadoPorID(empleado_id)
        self.assertTrue(resultado.es_igual(esperado))
        
        #terminar casos de busqueda 
        
if __name__ == '__main__':
    unittest.main()