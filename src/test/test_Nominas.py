import unittest
import sys
sys.path.append("src")

from model.nominas import Nomina
from controller.NominasController import ControladorNominas

class test_Nominas(unittest.TestCase):
    
    def setUpClass():
        ControladorNominas.EliminarTabla()
        ControladorNominas.crear_tabla()
    
    def test_insertar_nomina_1(self):
        nomina = Nomina("101", 10, 20000, 10000, 80000, 85000, 175000, 2000000, 1825000)
        ControladorNominas.InsertarNomina(nomina)

    def test_insertar_nomina_2(self):
        nomina = Nomina("102", 5, 18000, 5000, 75000, 79000, 159000, 1800000, 1641000)
        ControladorNominas.InsertarNomina(nomina)

    def test_insertar_nomina_3(self):
        nomina = Nomina("103", 0, 0, 2000, 60000, 70000, 132000, 1500000, 1368000)
        ControladorNominas.InsertarNomina(nomina)
        
    def test_modificar_nomina_1(self):
        nomina = Nomina(
            empleado_id="101",
            horas_extras=10,
            tarifa_hora_extra=25000,
            otras_deducciones=15000,
            deduccion_salud=55000,
            deduccion_pension=55000,
            total_deducciones=125000,
            total_devengado=3100000,
            total_a_pagar=2975000
        )
        ControladorNominas.ModificarNomina(nomina)
        resultado = ControladorNominas.BuscarNominaPorEmpleado("101")
        #self.assertEqual(resultado.horas_extras, "10")

    def test_modificar_nomina_2(self):
        nomina = Nomina(
            empleado_id="102",
            horas_extras=8,
            tarifa_hora_extra=22000,
            otras_deducciones=12000,
            deduccion_salud=52000,
            deduccion_pension=52000,
            total_deducciones=116000,
            total_devengado=3050000,
            total_a_pagar=2934000
        )
        ControladorNominas.ModificarNomina(nomina)
        resultado = ControladorNominas.BuscarNominaPorEmpleado("102")
        #self.assertEqual(resultado.tarifa_hora_extra, "22000")

    def test_modificar_nomina_3(self):
        nomina = Nomina(
            empleado_id="103",
            horas_extras=7,
            tarifa_hora_extra=21000,
            otras_deducciones=11000,
            deduccion_salud=51000,
            deduccion_pension=51000,
            total_deducciones=113000,
            total_devengado=3020000,
            total_a_pagar=2907000
        )
        ControladorNominas.ModificarNomina(nomina)
        resultado = ControladorNominas.BuscarNominaPorEmpleado("103")
        #self.assertEqual(resultado.total_a_pagar,"2907000")
    
if __name__ == '__main__':
    unittest.main()