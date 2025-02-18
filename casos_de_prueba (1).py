def calcular_deducciones(salario_base, deduccion_salud_pct, deduccion_pension_pct, otras_deducciones_pct=0):
    deduccion_salud = salario_base * deduccion_salud_pct
    deduccion_pension = salario_base * deduccion_pension_pct
    otras_deducciones = salario_base * otras_deducciones_pct
    total_deducciones = deduccion_salud + deduccion_pension + otras_deducciones
    return total_deducciones

def calcular_total_a_pagar(salario_base, horas_extras=0, tarifa_hora_extra=0, deduccion_salud_pct=0.04, deduccion_pension_pct=0.04, otras_deducciones_pct=0):
    # Calcular el valor de las horas extras
    valor_horas_extras = horas_extras * tarifa_hora_extra
    # Calcular el salario total devengado
    total_devengado = salario_base + valor_horas_extras
    # Calcular las deducciones
    total_deducciones = calcular_deducciones(salario_base, deduccion_salud_pct, deduccion_pension_pct, otras_deducciones_pct)
    # Calcular el total a pagar
    total_a_pagar = total_devengado - total_deducciones
    return total_devengado, total_deducciones, total_a_pagar

# Caso 1
salario_base_1 = 2000000
horas_extras_1 = 0
tarifa_hora_extra_1 = 0
total_devengado_1, total_deducciones_1, total_a_pagar_1 = calcular_total_a_pagar(salario_base_1, horas_extras_1, tarifa_hora_extra_1)

print("Caso 1:")
print(f"Total devengado: ${total_devengado_1:,.2f}")
print(f"Total deducciones: ${total_deducciones_1:,.2f}")
print(f"Total a pagar: ${total_a_pagar_1:,.2f}\n")

# Caso 2
salario_base_2 = 2200000
horas_extras_2 = 10
tarifa_hora_extra_2 = 15000
total_devengado_2, total_deducciones_2, total_a_pagar_2 = calcular_total_a_pagar(salario_base_2, horas_extras_2, tarifa_hora_extra_2)

print("Caso 2:")
print(f"Total devengado: ${total_devengado_2:,.2f}")
print(f"Total deducciones: ${total_deducciones_2:,.2f}")
print(f"Total a pagar: ${total_a_pagar_2:,.2f}\n")

# Caso 3
salario_base_3 = 3000000
horas_extras_3 = 5
tarifa_hora_extra_3 = 20000
otras_deducciones_pct_3 = 0.0833
total_devengado_3, total_deducciones_3, total_a_pagar_3 = calcular_total_a_pagar(salario_base_3, horas_extras_3, tarifa_hora_extra_3, otras_deducciones_pct=otras_deducciones_pct_3)

print("Caso 3:")
print(f"Total devengado: ${total_devengado_3:,.2f}")
print(f"Total deducciones: ${total_deducciones_3:,.2f}")
print(f"Total a pagar: ${total_a_pagar_3:,.2f}")