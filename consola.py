import nomina
from nomina import calcular_total_devengado, calcular_deducciones, calcular_salario_neto
from nomina import ErrorValorSalario, ErrorHorasExtras, ErrorTarifaHoraExtra, ErrorPorcentajeDeduccion, ErrorValorDeduccion, ErrorAfiliacion

# Obtener los datos de entrada
try:
    salario_base = float(input("Ingrese el salario base: "))
    horas_extra = int(input("Ingrese las horas extras trabajadas: "))
    tarifa_hora_extra = float(input("Ingrese la tarifa correspondiente: "))
    porcentaje_salud = float(input("Ingrese la deducción por salud (%): ")) / 100
    porcentaje_pension = float(input("Ingrese la deducción por pensión (%): ")) / 100
    otras_deducciones = float(input("Ingrese otras deducciones: "))

    # Realizar el proceso
    total_devengado = calcular_total_devengado(salario_base, horas_extra, tarifa_hora_extra)
    total_deducciones = calcular_deducciones(salario_base, porcentaje_salud, porcentaje_pension, otras_deducciones)
    total_a_pagar = calcular_salario_neto(total_devengado, total_deducciones)

    # Mostrar los datos de salida
    print(f"\n--- Resumen de Nómina ---")
    print(f"Total devengado: ${total_devengado:,.2f}")
    print(f"Total deducciones: ${total_deducciones:,.2f}")
    print(f"Salario neto a pagar: ${total_a_pagar:,.2f}")

except (ErrorValorSalario, ErrorHorasExtras, ErrorTarifaHoraExtra, ErrorPorcentajeDeduccion, ErrorValorDeduccion, ErrorAfiliacion) as err:
    print(f"\n[ERROR] No se pudo calcular la nómina: {err}")

except ValueError as err:
    print(f"\n[ERROR] Entrada inválida. Asegúrese de ingresar valores numéricos correctos. Detalle: {err}")

except Exception as err:
    print(f"\n[ERROR] Ocurrió un error inesperado: {err}")
