import sys
sys.path.append("src")
from controller.EmpleadosController import *
from model.Empleados import *

while True:
    print("\n--- MENÚ DE EMPLEADOS ---")
    print("¿Qué deseas hacer? Ingresa el número correspondiente:")
    print("1. Insertar empleado")
    print("2. Buscar empleado por ID")
    print("3. Modificar empleado")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        empleado_id = input("Ingrese ID del empleado: ")
        nombre = input("Nombre del empleado: ")
        salario_base = int(float(input("Salario base: ")))

        empleado = Empleado(empleado_id, nombre, salario_base)
        EmpleadosController.Insertar(empleado)
        print("Empleado insertado correctamente.")
        
    elif opcion == "2":
        empleado_id = input("Ingrese el ID del empleado: ")
        resultado = EmpleadosController.BuscarEmpleadoPorID(empleado_id)
        if resultado:
            print("\nDetalles del Empleado:")
            print(f"ID: {resultado.empleado_id}")
            print(f"Nombre: {resultado.nombre}")
            print(f"Salario base: {resultado.salario_base}")
        else:
            print("Empleado no encontrado.")
            
    elif opcion == "3":  #corregir opcion 3
        try:
            empleado_id = input("Ingrese el ID del empleado a modificar: ")
            print("\n¿Qué campo deseas modificar?")
            print("1. Nombre")
            print("2. Salario base")

            campo_opcion = input("Opción (1-2): ")
            campos = {
                "1": "nombre",
                "2": "salario_base"
            }

            if campo_opcion in campos:
                nuevo_valor = input("Nuevo valor: ")
                if campos[campo_opcion] == "salario_base":
                    nuevo_valor = float(nuevo_valor) 

                EmpleadosController.actualizar_campo_empleado(empleado_id, campos[campo_opcion], nuevo_valor)
                print(" Dato actualizado correctamente.")
            else:
                print("Opción no válida.")

        except ValueError:
            print("Error: Ingrese valores numéricos.")
        except Exception as e:
            print(f" Error inesperado: {e}")

    elif opcion == "4":
        print("👋 Saliendo del menú de empleados.")
        break

    else:
        print(" Opción inválida. Intente de nuevo.")
        