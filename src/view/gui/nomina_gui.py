import sys
sys.path.append("src")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from model.nomina import *

# Fondo claro
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class NominaGUI(App):

    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.formulario = GridLayout(cols=2, row_force_default=True, row_default_height=50, spacing=10, size_hint_y=None)
        self.formulario.bind(minimum_height=self.formulario.setter('height'))

        def agregar_entrada(texto):
            self.formulario.add_widget(Label(text=texto, color=(0.2, 0.2, 0.2, 1), font_size=16))
            entrada = TextInput(multiline=False, background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))
            self.formulario.add_widget(entrada)
            return entrada

        self.salario_base = agregar_entrada("Salario base:")
        self.horas_extras = agregar_entrada("Horas extras:")
        self.tarifa_hora = agregar_entrada("Tarifa por hora extra:")
        self.deduccion_salud = agregar_entrada("Deducción por salud (%):")
        self.deduccion_pension = agregar_entrada("Deducción por pensión (%):")
        self.otras_deducciones = agregar_entrada("Otras deducciones:")

        self.formulario.add_widget(Label(text="Resultado:", color=(0.2, 0.2, 0.2, 1), font_size=16))
        self.resultado_label = Label(text="", color=(0.1, 0.3, 0.6, 1), font_size=16)
        self.formulario.add_widget(self.resultado_label)

        scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.8))
        scroll.add_widget(self.formulario)

        boton_calcular = Button(text="Calcular", size_hint=(1, None), height=50,
                                background_color=(0.2, 0.6, 0.9, 1), color=(1, 1, 1, 1), font_size=18)
        boton_calcular.bind(on_press=self.calcular_total_a_pagar)

        main_layout.add_widget(scroll)
        main_layout.add_widget(boton_calcular)

        return main_layout

    def calcular_total_a_pagar(self, instance):
        try:
            self.validar()
            salario_base = float(self.salario_base.text)
            horas_extras = float(self.horas_extras.text)
            tarifa_hora_extra = float(self.tarifa_hora.text)
            porcentaje_salud = float(self.deduccion_salud.text)
            porcentaje_pension = float(self.deduccion_pension.text)
            otras_deducciones = float(self.otras_deducciones.text)

            total_devengado = calcular_total_devengado(salario_base, horas_extras, tarifa_hora_extra)
            total_deducciones = calcular_deducciones(salario_base, porcentaje_salud, porcentaje_pension, otras_deducciones)
            salario_neto = calcular_salario_neto(total_devengado, total_deducciones)

            self.resultado_label.text = f"Salario Neto: ${salario_neto:,.2f}"
        except ValueError as err:
            self.resultado_label.text = f"Error: {err}"
            self.mostrar_error(str(err))
        except Exception as err:
            self.mostrar_error(str(err))

    def mostrar_error(self, err):
        contenido = BoxLayout(orientation='vertical', padding=10, spacing=10)
        contenido.add_widget(Label(text=str(err)))
        cerrar = Button(text="Cerrar", size_hint_y=None, height=40)
        contenido.add_widget(cerrar)

        popup = Popup(title="Error", content=contenido, size_hint=(None, None), size=(400, 200), auto_dismiss=False)
        cerrar.bind(on_press=popup.dismiss)
        popup.open()

    def validar(self):
        try:
            float(self.salario_base.text)
            float(self.horas_extras.text)
            float(self.tarifa_hora.text)
            float(self.deduccion_salud.text)
            float(self.deduccion_pension.text)
            float(self.otras_deducciones.text)
        except ValueError:
            raise ValueError("Todos los campos deben contener números válidos.")
        
if __name__ == "__main__":
    NominaGUI().run()