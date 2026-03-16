CREATE LOGIN finanzas_user WITH PASSWORD = 'Finanzas2024*';
GO
USE FinanzasDB;
GO
CREATE USER finanzas_user FOR LOGIN finanzas_user;
GO
ALTER ROLE db_owner ADD MEMBER finanzas_user;
GO