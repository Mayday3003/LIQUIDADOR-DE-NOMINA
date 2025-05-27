Entrega 5: Pagina web
Integrantes:  
Mariana Lopera  
Pedro Hernandez  

PROYECTO

¿Qué es?

El proyecto es una aplicación para la liquidación de nómina que permite calcular de manera automática el pago de empleados, considerando factores como horas trabajadas, salario base y deducciones. Facilita la gestión de pagos y ayuda a reducir errores en los cálculos.

✅ Propósito:

- Automatizar el cálculo de nómina.  
- Generar reportes precisos de los pagos realizados.  
- Validar datos mediante pruebas unitarias para asegurar la fiabilidad del cálculo.

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

```
pip install psycopg2 flask
```

🐘 3. Base de Datos PostgreSQL en Neon.tech  
Este proyecto utiliza Neon.tech, una plataforma de base de datos PostgreSQL en la nube.

- Cuenta en Neon.tech: Asegúrate de tener una cuenta activa en Neon.tech.  
- Base de Datos: Crea una base de datos en Neon.tech desde su panel de control.  
- Credenciales: Obtén las credenciales de acceso a la base de datos desde el panel de Neon.tech, las cuales incluyen:  
  Host, Puerto, Nombre de la base de datos, Usuario, Contraseña.

Otras recomendaciones  
Agrega secret_config.py a .gitignore

4. Configuración de Conexión  
En el archivo secret_config.py deberás colocar las credenciales de conexión a tu base de datos de Neon.tech. El archivo debe tener el siguiente formato:

```python
PGHOST = "your_neon_host"
PGDATABASE = "your_database_name"
PGUSER = "your_database_user"
PGPASSWORD = "your_database_password"
PGPORT = "5432"  # Puerto por defecto de PostgreSQL
```

5. Proceso para crear las tablas en la base de datos  
Para crear las tablas necesarias en la base de datos, puedes ejecutar las funciones de creación de tablas desde el código o manualmente a través de un cliente SQL de tu preferencia. El código crea las tablas requeridas para empleados y nóminas.

🔧 6. Cómo probar la conexión a la base de datos  
Antes de ejecutar el proyecto, es importante verificar que puedas conectarte correctamente a la base de datos de Neon.tech utilizando las credenciales en secret_config.py. Puedes usar el siguiente script de prueba:

```python
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
```

8. Ejecutar el Proyecto

### Como aplicación de consola

- Crea un empleado:  
Usa el controlador de empleados (EmpleadosController) para agregar un nuevo empleado a la base de datos.

- Inserta la nómina:  
Utiliza el controlador de nóminas (NominasController) para insertar una nómina asociada al empleado.

- Prueba la funcionalidad:  
Si todo está configurado correctamente, la nómina debe ser calculada e insertada en la base de datos.

### Como aplicación Web

1. Instalar dependencias adicionales necesarias para la aplicación web (ya incluidas arriba):

```
pip install flask
```

2. Ejecutar el servidor web:

```
flask run
```

3. Acceder a la aplicación web:  
Abre un navegador web y navega a la siguiente URL:

```
http://127.0.0.1:5000
```
4.Despliegue en Render.com:

Para desplegar su aplicación Flask en Render.com , tena en cuenta lo siguiente:

Cree un archivo requirements.txt en la raiz de su proyecto, donde liste los modulos que deben instalarse par apoder ejecutar su aplicación.
Asegúrese de al menos incluir

flask
psycopg2
El Build Command de su aplicación será el sugerido por Render:

pip install -r requirements.txt

Render requiere que la aplicación ejecute en el puerto 10000 por defecto, y que escuche en la dirección IP 0.0.0.0, para ello, especifique el siguiente Start Command para su aplicación:
flask run -p 10000 -h 0.0.0.0

Para los parámetros de conexión a la base de datos, Ingrese al menú Environnment -> Secret Files y cree un nuevo Secret File llamado SecretConfig.py y ponga dentro de él las variables de conexión de su base de datos

- Link del deploy:
- https://liquidador-de-nomina-iv98.onrender.com

5. Funcionalidades disponibles en la aplicación web:

- Gestión de empleados: agregar, modificar, eliminar y buscar empleados.  
- Gestión de nóminas: insertar y consultar nóminas asociadas a empleados.  
- Formularios web para facilitar la interacción con la base de datos.

6. Requisitos adicionales:

- Asegúrate de que la base de datos PostgreSQL esté corriendo y accesible con las credenciales configuradas en `secret_config.py`.  
- El archivo `secret_config.py` debe estar correctamente configurado con los datos de conexión a la base de datos.

## Cambios recientes 

- Actualización de la estructura MVC del proyecto para mejorar la organización y mantenimiento del código.  
- Eliminación del archivo `blueprints/empleados_bp.py` como parte de la reestructuración.

- Merge de la rama principal del repositorio remoto para mantener el proyecto actualizado.  
- Actualización del archivo `.env` para configuración del entorno.

### Objetivos de los cambios

- Mejorar la estructura del proyecto para facilitar futuras implementaciones y mantenimiento.  
- Mantener el proyecto sincronizado con la rama principal remota.  
- Actualizar configuraciones necesarias para el correcto funcionamiento del entorno de desarrollo.

### Comandos para ejecutar el proyecto

- Asegúrate de tener instaladas las dependencias con:

```
pip install psycopg2 flask
```

- Ejecuta el proyecto con:

```
flask run
```

### Requisitos para los cambios

- Python 3.9 o superior.  
- Base de datos PostgreSQL en Neon.tech configurada correctamente.  
- Archivo `secret_config.py` con las credenciales de conexión a la base de datos.
