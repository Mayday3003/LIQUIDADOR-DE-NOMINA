import unittest
import sys
sys.path.append("src")

from model.Empleados import Empleado
from controller.EmpleadosController import EmpleadosController

class TestEmpleados(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Se ejecuta una vez antes de todas las pruebas. Crea la tabla de empleados."""
        EmpleadosController.EliminarTabla()
        EmpleadosController.CrearTabla()

    def setUp(self):
        """Se ejecuta antes de cada prueba. Limpia la tabla de empleados."""
        EmpleadosController.EliminarTabla()
        EmpleadosController.CrearTabla()

    def test_insertar_empleado(self):
        empleado = Empleado(empleado_id="1034990", nombre="Kevin", dni="123456789", salario_base=2000000)
        EmpleadosController.Insertar(empleado)
        usuario_buscado = EmpleadosController.BuscarEmpleadoPorID(empleado_id="1034990")
        self.assertIsNotNone(usuario_buscado)
        self.assertTrue(usuario_buscado.es_igual(empleado))

    def test_modificar_empleado(self):
        empleado_original = Empleado(empleado_id="112530", nombre="Juan", dni="987654321", salario_base=3000000)
        EmpleadosController.Insertar(empleado_original)
        EmpleadosController.ActualizarCampoEmpleado(empleado_id="112530", campo="nombre", nuevo_valor="Santiago")
        empleado_modificado = EmpleadosController.BuscarEmpleadoPorID(empleado_id="112530")
        self.assertIsNotNone(empleado_modificado)
        self.assertEqual(empleado_modificado.nombre, "Santiago")

    def test_eliminar_empleado(self):
        empleado = Empleado(empleado_id="154056", nombre="Jesús", dni="456789123", salario_base=4000000)
        EmpleadosController.Insertar(empleado)
        EmpleadosController.Eliminar(empleado_id="154056")
        usuario_buscado = EmpleadosController.BuscarEmpleadoPorID(empleado_id="154056")
        self.assertIsNone(usuario_buscado)

    def test_buscar_empleado_no_existente(self):
        usuario_buscado = EmpleadosController.BuscarEmpleadoPorID(empleado_id="999999")
        self.assertIsNone(usuario_buscado)

if __name__ == '__main__':
    unittest.main()
