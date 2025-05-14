import sys
sys.path.append("src")
from controller.NominasController import *
from model.nominas import *

while True:
    print("\n--- MENÚ DE NÓMINAS ---")
    print("¿Qué deseas hacer? Ingresa el número correspondiente:")
    print("1. Insertar datos de nómina")
    print("2. Buscar nómina por cédula (empleado_id)")
    print("3. Modificar nómina")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        empleado_id = int(input("Ingrese cédula del empleado: "))
        horas_extras = int(input("Horas extras: "))
        tarifa_hora_extra = float(input("Tarifa hora extra: "))
        otras_deducciones = float(input("Otras deducciones: "))
        deduccion_salud = float(input("Deducción salud: "))
        deduccion_pension = float(input("Deducción pensión: "))
        total_deducciones = float(input("Total deducciones: "))
        total_devengado = float(input("Total devengado: "))
        total_a_pagar = float(input("Total a pagar: "))

        nomina = Nomina(empleado_id, horas_extras, tarifa_hora_extra,
                        otras_deducciones, deduccion_salud, deduccion_pension,
                        total_deducciones, total_devengado, total_a_pagar)

        ControladorNominas.InsertarNomina(nomina)
        print("Nómina insertada correctamente.")
        
    elif opcion == "2":
        empleado_id = int(input("Ingrese la identificacion del empleado: "))
        resultado = ControladorNominas.BuscarNominaPorEmpleado(empleado_id)
        if resultado:
            print("\nDetalles de la Nómina:")
            print(f"Empleado ID: {resultado.empleado_id}")
            print(f"Horas extras: {resultado.horas_extras}")
            print(f"Tarifa hora extra: {resultado.tarifa_hora_extra}")
            print(f"Otras deducciones: {resultado.otras_deducciones}")
            print(f"Deducción salud: {resultado.deduccion_salud}")
            print(f"Deducción pensión: {resultado.deduccion_pension}")
            print(f"Total deducciones: {resultado.total_deducciones}")
            print(f"Total devengado: {resultado.total_devengado}")
            print(f"Total a pagar: {resultado.total_a_pagar}")
        else:
            print("Nómina no encontrada.")
            
    elif opcion == "3":
        try:
            empleado_id = str(input("Ingrese la cédula del empleado a modificar: "))
            print("\n¿Qué campo deseas modificar?")
            print("1. Horas extras")
            print("2. Tarifa hora extra")
            print("3. Otras deducciones")
            print("4. Deducción salud")
            print("5. Deducción pensión")
            print("6. Total deducciones")
            print("7. Total devengado")
            print("8. Total a pagar")
            
            campo_opcion = input("Opción (1-8): ")
            nuevo_valor = float(input("Nuevo valor: "))

            campos = {
                "1": "horas_extras",
                "2": "tarifa_hora_extra",
                "3": "otras_deducciones",
                "4": "deduccion_salud",
                "5": "deduccion_pension",
                "6": "total_deducciones",
                "7": "total_devengado",
                "8": "total_a_pagar"
            }

            if campo_opcion in campos:
                ControladorNominas.actualizar_campo_nomina(empleado_id, campos[campo_opcion], nuevo_valor)
                print("Dato actualizado correctamente.")
            else:
                print("Opción no válida.")

        except ValueError:
            print("Error: Ingrese valores numéricos.")
        except Exception as e:
            print(f" Error inesperado: {e}")

    elif opcion == "4":
        print("Saliendo del menú de nóminas.")
        break

    else:
        print("Opción inválida. Intente de nuevo.")