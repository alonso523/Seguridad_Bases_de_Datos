import pyodbc
import os
import time

CONNECTION_STRING = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=sqlserver-qa;"
    "UID=sa;"
    "PWD=Finanzas2024*;"
    "TrustServerCertificate=yes;"
)

SQL_DIR = "sql"

def run_sql_file(cursor, path):
    with open(path, "r", encoding="utf-8") as f:
        sql = f.read()

    statements = sql.split("GO")
    for stmt in statements:
        stmt = stmt.strip()
        if stmt:
            cursor.execute(stmt)

def initialize_database():
    MAX_RETRIES = 30
    WAIT_SECONDS = 2

    # Esperar a que SQL Server esté listo
    for i in range(MAX_RETRIES):
        try:
            conn = pyodbc.connect(CONNECTION_STRING, autocommit=True)
            print("Conexión exitosa a SQL Server")
            break
        except Exception as e:
            print(f"Intento {i+1}/{MAX_RETRIES}: SQL Server no está listo aún...")
            time.sleep(WAIT_SECONDS)
    else:
        raise Exception("SQL Server no respondió a tiempo")

    cursor = conn.cursor()

    # Verificar si la base ya existe
    cursor.execute("SELECT name FROM sys.databases WHERE name='FinanzasDB'")
    exists = cursor.fetchone()

    if exists:
        print("Base de datos ya existe, no se ejecutan scripts.")
        cursor.close()
        conn.close()
        return

    print("Inicializando base de datos...")

    scripts = [
        "01_create_database.sql",
        "02_data.sql",
        "03_create_user.sql",
    ]

    for script in scripts:
        path = os.path.join(SQL_DIR, script)
        print(f"Ejecutando script: {script}")
        run_sql_file(cursor, path)

    cursor.close()
    conn.close()
    print("Base de datos inicializada correctamente.")