import sys 
sys.path.append("src")
from model.nomina import calcular_total_devengado, calcular_deducciones, calcular_salario_neto

def pedir_numero(mensaje, tipo=float, min_val=None, max_val=None):
    while True:
        try:
            valor = tipo(input(mensaje))
            if (min_val is not None and valor < min_val) or (max_val is not None and valor > max_val):
                print(f"❌ El valor debe estar entre {min_val} y {max_val}.")
            else:
                return valor
        except ValueError:
            print("❌ Entrada inválida. Intente de nuevo.")

# Solicitar datos
salario_base = pedir_numero("Ingrese el salario base: ", min_val=1)
horas_extras = pedir_numero("Ingrese horas extras: ", int, 0, 80)
tarifa_hora_extra = pedir_numero("Ingrese la tarifa por hora extra: ", min_val=0)
porcentaje_salud = pedir_numero("Ingrese porcentaje de salud: ", min_val=0, max_val=100)
porcentaje_pension = pedir_numero("Ingrese porcentaje de pensión: ", min_val=0, max_val=100)
otras_deducciones = pedir_numero("Ingrese otras deducciones: ", min_val=0)

try:
    total_devengado = calcular_total_devengado(salario_base, horas_extras, tarifa_hora_extra)
    total_deducciones = calcular_deducciones(salario_base, porcentaje_salud, porcentaje_pension, otras_deducciones)
    salario_neto = calcular_salario_neto(total_devengado, total_deducciones)
    print(f"\n✅ Salario Neto: {salario_neto:.2f}")
except Exception as err:
    print(f"❌ Error: {err}")
