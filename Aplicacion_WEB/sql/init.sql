-- Crear base de datos
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'FinanzasDB')
BEGIN
    CREATE DATABASE FinanzasDB;
END
GO

-- Cambiar al contexto de la base
USE FinanzasDB;
GO

-- Crear login
IF NOT EXISTS (SELECT name FROM sys.sql_logins WHERE name = 'finanzas_user')
BEGIN
    CREATE LOGIN finanzas_user WITH PASSWORD = 'Finanzas2024*';
END
GO

-- Crear usuario dentro de la base
IF NOT EXISTS (SELECT name FROM sys.database_principals WHERE name = 'finanzas_user')
BEGIN
    CREATE USER finanzas_user FOR LOGIN finanzas_user;
END
GO

-- Dar permisos
ALTER ROLE db_owner ADD MEMBER finanzas_user;
GO

-- Crear base de datos si no existe
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'FinanzasDB')
BEGIN
    CREATE DATABASE FinanzasDB;
END
GO

USE FinanzasDB;
GO

---------------------------------------------------------
-- Crear tabla CATEGORIAS
---------------------------------------------------------
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='categorias' AND xtype='U')
BEGIN
    CREATE TABLE categorias (
        id INT PRIMARY KEY,
        nombre NVARCHAR(100) NOT NULL,
        descripcion NVARCHAR(255)
    );
END
GO

---------------------------------------------------------
-- Crear tabla TRANSACCIONES
---------------------------------------------------------
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='transacciones' AND xtype='U')
BEGIN
    CREATE TABLE transacciones (
        id INT PRIMARY KEY,
        descripcion NVARCHAR(255) NOT NULL,
        monto DECIMAL(18,2) NOT NULL,
        fecha DATE NOT NULL,
        tipo NVARCHAR(50) NOT NULL,
        categoria_id INT NOT NULL,
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
    );
END
GO

---------------------------------------------------------
-- Insertar datos en CATEGORIAS
---------------------------------------------------------
INSERT INTO categorias (id, nombre, descripcion) VALUES
(1, 'Alimentación', 'Compras de comida y restaurantes'),
(2, 'Transporte', 'Gasolina, Uber, autobús'),
(3, 'Servicios', 'Luz, agua, internet'),
(4, 'Salud', 'Medicinas, consultas'),
(5, 'Ingresos', 'Salario y otros ingresos');
GO

---------------------------------------------------------
-- Insertar datos en TRANSACCIONES
---------------------------------------------------------
INSERT INTO transacciones (id, descripcion, monto, fecha, tipo, categoria_id) VALUES
(1, 'Compra supermercado', 35000.00, '2026-02-23', 'GASTO', 1),
(2, 'Gasolina', 15000.00, '2026-02-26', 'Gasto', 2),
(1003, 'Pago de Internet', 25000.00, '2026-03-01', 'gasto', 3),
(1004, 'Medicamento para la presión', 20000.00, '2026-03-01', 'gasto', 4);
GO