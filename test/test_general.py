import unittest
import sys
import os

# Agrega el directorio raíz del proyecto al sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from src.model.Empleados import Empleado
from src.controller.EmpleadosController import EmpleadosController
from src.model.nominas import Nomina
from src.controller.NominasController import ControladorNominas
from src.model.nomina import calcular_total_devengado, calcular_deducciones, calcular_salario_neto

class TestGeneral(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Se ejecuta una vez antes de todas las pruebas."""
        EmpleadosController.EliminarTabla()
        EmpleadosController.CrearTabla()
        ControladorNominas.EliminarTabla()
        ControladorNominas.crear_tabla()

    def setUp(self):
        """Se ejecuta antes de cada prueba para limpiar las tablas."""
        EmpleadosController.EliminarTabla()
        EmpleadosController.CrearTabla()
        ControladorNominas.EliminarTabla()
        ControladorNominas.crear_tabla()

    def test_insertar_empleado(self):
        """Prueba la inserción de un empleado."""
        empleado = Empleado(empleado_id="1", nombre="Juan", dni="123456789", salario_base=2000000)
        EmpleadosController.Insertar(empleado)
        buscado = EmpleadosController.BuscarEmpleadoPorID("1")
        self.assertIsNotNone(buscado)
        self.assertEqual(buscado.nombre, "Juan")

    def test_modificar_empleado(self):
        """Prueba la modificación de un empleado."""
        empleado = Empleado(empleado_id="2", nombre="Ana", dni="987654321", salario_base=2500000)
        EmpleadosController.Insertar(empleado)
        EmpleadosController.ActualizarCampoEmpleado("2", "nombre", "Ana María")
        modificado = EmpleadosController.BuscarEmpleadoPorID("2")
        self.assertEqual(modificado.nombre, "Ana María")

    def test_eliminar_empleado(self):
        """Prueba la eliminación de un empleado."""
        empleado = Empleado(empleado_id="3", nombre="Carlos", dni="456789123", salario_base=3000000)
        EmpleadosController.Insertar(empleado)
        EmpleadosController.Eliminar("3")
        eliminado = EmpleadosController.BuscarEmpleadoPorID("3")
        self.assertIsNone(eliminado)

    def test_insertar_nomina(self):
        """Prueba la inserción de una nómina."""
        nomina = Nomina("1", 10, 20000, 10000, 80000, 85000, 175000, 2000000, 1825000)
        ControladorNominas.InsertarNomina(nomina)
        buscada = ControladorNominas.BuscarNominaPorEmpleado("1")
        self.assertIsNotNone(buscada)
        self.assertEqual(buscada.empleado_id, "1")

    def test_modificar_nomina(self):
        """Prueba la modificación de una nómina."""
        nomina = Nomina("2", 5, 15000, 5000, 75000, 79000, 159000, 1800000, 1641000)
        ControladorNominas.InsertarNomina(nomina)
        ControladorNominas.actualizar_campo_nomina("2", "horas_extras", 8)
        modificada = ControladorNominas.BuscarNominaPorEmpleado("2")
        self.assertEqual(modificada.horas_extras, 8)

    def test_eliminar_nomina(self):
        """Prueba la eliminación de una nómina."""
        nomina = Nomina("3", 0, 0, 2000, 60000, 70000, 132000, 1500000, 1368000)
        ControladorNominas.InsertarNomina(nomina)
        ControladorNominas.EliminarTabla()
        eliminada = ControladorNominas.BuscarNominaPorEmpleado("3")
        self.assertIsNone(eliminada)

    def test_calculo_total_devengado(self):
        """Prueba el cálculo del total devengado."""
        total_devengado = calcular_total_devengado(2000000, 10, 20000)
        self.assertEqual(total_devengado, 2200000)

    def test_calculo_deducciones(self):
        """Prueba el cálculo de deducciones."""
        deducciones = calcular_deducciones(2000000, 4, 4, 10000)
        self.assertEqual(deducciones, 180000)

    def test_calculo_salario_neto(self):
        """Prueba el cálculo del salario neto."""
        salario_neto = calcular_salario_neto(2200000, 180000)
        self.assertEqual(salario_neto, 2020000)

if __name__ == '__main__':
    unittest.main()
