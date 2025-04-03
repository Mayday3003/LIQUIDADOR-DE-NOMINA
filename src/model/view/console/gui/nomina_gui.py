import sys
sys.path.append("src")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from model.nomina import *

class NominaGUI(App):
    
    def build(self):
        self.contenedor = GridLayout(rows=8, cols=2)

        self.contenedor.add_widget(Label(text="Ingrese el salario base: "))
        self.salario_base = TextInput()
        self.contenedor.add_widget(self.salario_base)

        self.contenedor.add_widget(Label(text="Ingrese las horas extras: "))
        self.horas_extras = TextInput()
        self.contenedor.add_widget(self.horas_extras)

        self.contenedor.add_widget(Label(text="Ingrese la tarifa por hora extra: "))
        self.tarifa_hora = TextInput()
        self.contenedor.add_widget(self.tarifa_hora)

        self.contenedor.add_widget(Label(text="Ingrese la deducción por salud: "))
        self.deduccion_salud = TextInput()
        self.contenedor.add_widget(self.deduccion_salud)

        self.contenedor.add_widget(Label(text="Ingrese la deducción por pensión: "))
        self.deduccion_pension = TextInput()
        self.contenedor.add_widget(self.deduccion_pension)

        self.contenedor.add_widget(Label(text="Otras deducciones: "))
        self.otras_deducciones = TextInput()
        self.contenedor.add_widget(self.otras_deducciones)

        self.contenedor.add_widget(Label(text="Resultado: "))
        self.resultado_label = Label(text="")
        self.contenedor.add_widget(self.resultado_label)

        boton_calcular = Button(text="Calcular")
        boton_calcular.bind(on_press=self.calcular_total_a_pagar)
        self.contenedor.add_widget(boton_calcular)

        return self.contenedor

    def calcular_total_a_pagar(self, instance):
        salario_base = float(self.salario_base.text)
        horas_extras = float(self.horas_extras.text)
        tarifa_hora_extra = float(self.tarifa_hora.text)
        porcentaje_salud = float(self.deduccion_salud.text)
        porcentaje_pension = float(self.deduccion_pension.text)
        otras_deducciones = float(self.otras_deducciones.text)

        total_devengado = calcular_total_devengado(salario_base, horas_extras, tarifa_hora_extra)
        total_deducciones = calcular_deducciones(salario_base, porcentaje_salud, porcentaje_pension, otras_deducciones)
        salario_neto = calcular_salario_neto(total_devengado, total_deducciones)

        self.resultado_label.text = f"Salario Neto: ${salario_neto:.2f}"

        print("\n===== Cálculo de Nómina =====")
        print(f"Salario Base: ${salario_base:.2f}")
        print(f"Horas Extras: {horas_extras} x ${tarifa_hora_extra:.2f} = ${horas_extras * tarifa_hora_extra:.2f}")
        print(f"Total Devengado: ${total_devengado:.2f}")
        print(f"Deducción Salud ({porcentaje_salud}%): ${porcentaje_salud / 100 * salario_base:.2f}")
        print(f"Deducción Pensión ({porcentaje_pension}%): ${porcentaje_pension / 100 * salario_base:.2f}")
        print(f"Otras Deducciones: ${otras_deducciones:.2f}")
        print(f"Total Deducciones: ${total_deducciones:.2f}")
        print(f"Salario Neto: ${salario_neto:.2f}")
        print("============================\n")

if __name__ == "__main__":
    NominaGUI().run()