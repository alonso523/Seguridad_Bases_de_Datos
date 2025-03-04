"""
Connects to a SQL database using pyodbc
"""
import pyodbc

SERVER = 'ALONSO-CNUT0Q60\MSSQLSERVER01'
DATABASE = 'AdventureWorks2022'
USERNAME = 'ALONSO-CNUT0Q60\alons'
PASSWORD = ''

#connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};TrustServerCertificate=Yes;' ##;TrustServerCertificate=true
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};TrustServerCertificate=Yes;Trusted_Connection=yes;' ##;TrustServerCertificate=true

conn = pyodbc.connect(connectionString)
print("Connection setup successfully")

SQL_QUERY = """
SELECT 
	ProductID,
	Name,
	ProductNumber,
	SafetyStockLevel,
	'UPPER STOCK'	AS CONDITION_STOCK
 FROM [Production].[Product]
 WHERE SafetyStockLevel >= 500
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(f"{r.ProductID}\t{r.Name}\t{r.ProductNumber}\t{r.SafetyStockLevel}\t{r.CONDITION_STOCK}")