import sys
sys.path.append("src")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from model.nomina import *
from kivy.uix.popup import Popup

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

            self.resultado_label.text = f"Salario Neto: ${salario_neto:.2f}"
        except ValueError as err:
            self.resultado_label.text = f"Error: {err}. Ingrese un número válido, por ejemplo, 500000.00"
            self.mostrar_error(str(err))
        except Exception as err:
            self.mostrar_error(str(err))


    def mostrar_error( self, err ):
        """
        Abre una ventana emergente, con un texto y un botón para cerrar
        Parámetros:
        err: Mensaje de error que queremos mostrar en la ventana
        """

        # contenido es el contenedor donde vamos a agregar los widgets de la ventana
        contenido = GridLayout(cols=1)
        # Creamos el Label que contiene el mensaje de error
        contenido.add_widget( Label(text= str(err) ) )
        # Creamos el botón para cerrar la ventana
        cerrar = Button(text="Cerrar" )
        contenido.add_widget( cerrar )
        # Creamos la ventana emergente con el widget Popup de Kivy
        popup = Popup(title="Error",content=contenido)
        # Conectamos el evento del botón con el método dismiss que cierra el popup
        cerrar.bind( on_press=popup.dismiss)
        # Mostramos la ventana emergente
        popup.open()

    def validar(self):
        """
        Verifica que todos los datos ingresados por el usuario sean correctos.
        """
        try:
            # Intentamos convertir los valores a flotantes para asegurarnos de que sean válidos
            float(self.salario_base.text)
            float(self.horas_extras.text)
            float(self.tarifa_hora.text)
            float(self.deduccion_salud.text)
            float(self.deduccion_pension.text)
            float(self.otras_deducciones.text)
        except ValueError:
            # Si ocurre un error, lanzamos una excepción personalizada
            raise ValueError("Todos los campos deben contener números válidos.")
        
if __name__ == "__main__":
    NominaGUI().run()