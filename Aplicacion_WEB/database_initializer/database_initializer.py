import pyodbc
import os
import time

CONNECTION_STRING = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=sqlserver;"
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
    for _ in range(30):
        try:
            conn = pyodbc.connect(CONNECTION_STRING, autocommit=True)
            break
        except:
            time.sleep(1)
    else:
        raise Exception("SQL Server no respondió a tiempo")

    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sys.databases WHERE name='FinanzasDB'")
    exists = cursor.fetchone()

    if exists:
        cursor.close()
        conn.close()
        return

    scripts = [
        "01_create_database.sql",
        "02_data.sql",
        "03_create_user.sql",
    ]

    for script in scripts:
        path = os.path.join(SQL_DIR, script)
        run_sql_file(cursor, path)

    cursor.close()
    conn.close()