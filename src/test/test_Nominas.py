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
        buscar_nomina = ControladorNominas.BuscarNominaPorEmpleado(nomina.empleado_id)
        self.assertTrue(buscar_nomina.es_igual(nomina))

    def test_insertar_nomina_2(self):
        nomina = Nomina("102", 5, 18000, 5000, 75000, 79000, 159000, 1800000, 1641000)
        ControladorNominas.InsertarNomina(nomina)
        buscar_nomina = ControladorNominas.BuscarNominaPorEmpleado(nomina.empleado_id)
        self.assertTrue(buscar_nomina.es_igual(nomina))

    def test_insertar_nomina_3(self):
        nomina = Nomina("103", 0, 0, 2000, 60000, 70000, 132000, 1500000, 1368000)
        ControladorNominas.InsertarNomina(nomina)
        buscar_nomina = ControladorNominas.BuscarNominaPorEmpleado(nomina.empleado_id)
        self.assertTrue(buscar_nomina.es_igual(nomina))
        
    def test_modificar_1(self):
        nomina_original = Nomina(
            empleado_id="101",
            horas_extras=10,
            tarifa_hora_extra=20000,
            otras_deducciones=10000,
            deduccion_salud=80000,
            deduccion_pension=85000,
            total_deducciones=175000,
            total_devengado=2000000,
            total_a_pagar=1825000
        )
        ControladorNominas.InsertarNomina(nomina_original)

        ControladorNominas.EliminarTabla()
        ControladorNominas.crear_tabla()
        nomina_modificada = Nomina(
            empleado_id="101",
            horas_extras=15,  
            tarifa_hora_extra=25000,
            otras_deducciones=10000,  
            deduccion_salud=60000,    
            deduccion_pension=60000,  
            total_deducciones=130000,
            total_devengado=3200000,  
            total_a_pagar=3070000    
        )
        ControladorNominas.InsertarNomina(nomina_modificada)
        
        resultado = ControladorNominas.BuscarNominaPorEmpleado("101")
        self.assertTrue(resultado.es_igual(nomina_modificada))
        
        
    def test_modificar_2(self):
        nomina_original = Nomina(
            empleado_id="102",
            horas_extras=5,
            tarifa_hora_extra=18000,
            otras_deducciones=5000,
            deduccion_salud=75000,
            deduccion_pension=79000,
            total_deducciones=159000,
            total_devengado=1800000,
            total_a_pagar=1641000
        )
        ControladorNominas.InsertarNomina(nomina_original)

        nomina_modificada = Nomina(
            empleado_id="102",
            horas_extras=7,            
            tarifa_hora_extra=20000,    
            otras_deducciones=4000,     
            deduccion_salud=70000,      
            deduccion_pension=75000,    
            total_deducciones=145000,   
            total_devengado=1900000,    
            total_a_pagar=1755000       
        )

        ControladorNominas.EliminarTabla()
        ControladorNominas.crear_tabla()
        ControladorNominas.InsertarNomina(nomina_modificada)

        resultado = ControladorNominas.BuscarNominaPorEmpleado("102")
        self.assertTrue(resultado.es_igual(nomina_modificada))
        
    def test_modificar_3(self):
        nomina_original = Nomina(
            empleado_id="103",
            horas_extras=0,
            tarifa_hora_extra=0,
            otras_deducciones=2000,
            deduccion_salud=60000,
            deduccion_pension=70000,
            total_deducciones=132000,
            total_devengado=1500000,
            total_a_pagar=1368000
        )
        ControladorNominas.InsertarNomina(nomina_original)

        nomina_modificada = Nomina(
            empleado_id="103",
            horas_extras=8,
            tarifa_hora_extra=15000,
            otras_deducciones=1000,
            deduccion_salud=65000,
            deduccion_pension=62000,
            total_deducciones=128000,
            total_devengado=1600000,
            total_a_pagar=1472000
        )

        ControladorNominas.EliminarTabla()
        ControladorNominas.crear_tabla()
        ControladorNominas.InsertarNomina(nomina_modificada)

        resultado = ControladorNominas.BuscarNominaPorEmpleado("103")
        self.assertTrue(resultado.es_igual(nomina_modificada))
        
    def test_buscado_1(self):
        empleado_id = "485679"
        esperado = Nomina(empleado_id, 15, 40000, 10000, 80000, 85000, 175000, 2000000, 1825000)
        ControladorNominas.InsertarNomina(esperado)
        resultado = ControladorNominas.BuscarNominaPorEmpleado(empleado_id)
        self.assertTrue(resultado.es_igual(esperado))
        
    def test_buscado_2(self):
        empleado_id = "1034567"
        esperado = Nomina(empleado_id, 5, 18000, 5000, 75000, 79000, 159000, 1800000, 1641000)
        ControladorNominas.InsertarNomina(esperado)
        resultado = ControladorNominas.BuscarNominaPorEmpleado(empleado_id)
        self.assertTrue(resultado.es_igual(esperado))
        
    def test_buscado_3(self):
        empleado_id = "777778"
        esperado = Nomina(empleado_id, 0, 0, 2000, 60000, 70000, 132000, 1500000, 1368000)
        ControladorNominas.InsertarNomina(esperado)
        resultado = ControladorNominas.BuscarNominaPorEmpleado(empleado_id)
        self.assertTrue(resultado.es_igual(esperado))
        
if __name__ == '__main__':
    unittest.main()