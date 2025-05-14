"""
Connects to a SQL database using pyodbc
"""
import pyodbc
#import pandas as pd
# Línea que permite cargar datos desde word, guardado como csv
import csv


SERVER = 'ALONSO-CNUT0Q60\MSSQLSERVER01'
DATABASE = 'Proyecto_acampos'
USERNAME = 'ALONSO-CNUT0Q60\alons'
PASSWORD = ''

#connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=Yes;' ##;TrustServerCertificate=true
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};TrustServerCertificate=Yes;Trusted_Connection=yes;' ##;TrustServerCertificate=true

conn = pyodbc.connect(connectionString)
print("Connection setup successfully")

from docx import Document
import csv

# Cargar el documento
#doc = Document("C:\\Users\\alons\\OneDrive\\Escritorio\\Datos Proyecto Final.docx")
import re

# Cargar el texto desde un archivo
with open("C:\\Users\\alons\\OneDrive\\Escritorio\\Table Project v3.txt", "r", encoding="utf-8") as file:
    contenido = file.read()

# Expresión regular para identificar múltiples espacios y dividir datos correctamente
lineas = re.split(r'\s{2,}', contenido.strip())

# Estructurar las filas correctamente (cada 8 elementos es una fila completa)
datos_estructurados = [lineas[i:i+8] for i in range(0, len(lineas), 8)]

# Guardar en CSV
with open("datos_v3.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Encabezados de las columnas
    writer.writerow(["PROJNO", "PROJNAME", "DEPT NO", "PR RESPEMP", "STAFF", "PRSTDATE", "PRENDATE", "MAJPROJ"])
    #writer.writerow(["PROJNO"])
    
    # Escribir datos procesados
    writer.writerows(datos_estructurados)

print("Conversión a CSV completada.")