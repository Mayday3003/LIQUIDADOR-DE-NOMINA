Entrega 4: Base datos 
Integrantes:
Juan jose cano giraldo
Simon munoz 

PROYECTO

¿Qué es?

El proyecto es una aplicación para la liquidación de nómina que permite calcular de manera automática el pago de empleados, considerando factores como horas trabajadas, salario base y deducciones. Facilita la gestión de pagos y ayuda a reducir errores en los cálculos.

✅ Propósito:

Automatizar el cálculo de nómina.
Generar reportes precisos de los pagos realizados.
Validar datos mediante pruebas unitarias para asegurar la fiabilidad del cálculo.
¿Para qué es?

El objetivo es garantizar que el cálculo del salario neto sea preciso, rápido y conforme a las normativas laborales. La aplicación permitirá a las empresas:
✅ Automatizar el proceso de liquidación de nómina.
✅ Reducir errores humanos en los cálculos.
✅ Generar reportes detallados de los pagos realizados.
✅ Facilitar la gestión de pagos a empleados.

Requisitos para ejecutar correctamente el proyecto
Para que el sistema funcione sin errores, asegúrate de tener lo siguiente:

🔧 1. Python
Versión: Python 3.9 o superior

2. Librerías requeridas
Instala las siguientes dependencias usando pip:

pip install psycopg2

🐘 3. Base de Datos PostgreSQL en Neon.tech
Este proyecto utiliza Neon.tech, una plataforma de base de datos PostgreSQL en la nube.

Cuenta en Neon.tech: Asegúrate de tener una cuenta activa en Neon.tech.

Base de Datos: Crea una base de datos en Neon.tech desde su panel de control.

Credenciales: Obtén las credenciales de acceso a la base de datos desde el panel de Neon.tech, las cuales incluyen:

Host

Puerto

Nombre de la base de datos

Usuario

Contraseña

Otras recomendaciones
Agrega secret_config.py a .gitignore

4. Configuración de Conexión
En el archivo secret_config.py deberás colocar las credenciales de conexión a tu base de datos de Neon.tech. El archivo debe tener el siguiente formato:

PGHOST = "your_neon_host"
PGDATABASE = "your_database_name"
PGUSER = "your_database_user"
PGPASSWORD = "your_database_password"
PGPORT = "5432"  # Puerto por defecto de PostgreSQL

5. Proceso para crear las tablas en la base de datos
Para crear las tablas necesarias en la base de datos, puedes ejecutar las funciones de creación de tablas desde el código o manualmente a través de un cliente SQL de tu preferencia. El código crea las tablas requeridas para empleados y nominas.

🔧 6. Cómo probar la conexión a la base de datos
Antes de ejecutar el proyecto, es importante verificar que puedas conectarte correctamente a la base de datos de Neon.tech utilizando las credenciales en secret_config.py. Puedes usar el siguiente script de prueba:

import psycopg2

import secret_config


def test_connection():

    try:
    
        connection = psycopg2.connect(
        
            host=secret_config.PGHOST,
            
            database=secret_config.PGDATABASE,
            
            user=secret_config.PGUSER,
            
            password=secret_config.PGPASSWORD,
            
            port=secret_config.PGPORT
        )
        print("Conexión exitosa a la base de datos.")
        
        connection.close()
        
    except Exception as e:
    
        print(f"Error al conectar a la base de datos: {e}")

test_connection()

8. Ejecutar el Proyecto
Crea un empleado:

Usa el controlador de empleados (EmpleadosController) para agregar un nuevo empleado a la base de datos.

Inserta la nómina:

Utiliza el controlador de nóminas (NominasController) para insertar una nómina asociada al empleado.

Prueba la funcionalidad:

Si todo está configurado correctamente, la nómina debe ser calculada e insertada en la base de datos.







