# db.py
import os
from psycopg2 import connect, OperationalError
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# Carga las variables de entorno desde .env
load_dotenv()

def get_connection():
    url = os.getenv("DATABASE_URL")
    if not url:
        raise ValueError("No se encontró la variable DATABASE_URL en el entorno.")
    try:
        conn = connect(dsn=url, cursor_factory=RealDictCursor)
        conn.autocommit = True
        return conn
    except OperationalError as e:
        print("Error al conectar:", e)
        raise

if __name__ == "__main__":
    # Prueba la conexión
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT NOW() AS fecha;")
    resultado = cur.fetchone()
    print("Conexión exitosa. Hora en servidor:", resultado["fecha"])
    conn.close()
