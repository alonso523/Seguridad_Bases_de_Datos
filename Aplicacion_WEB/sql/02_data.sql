USE FinanzasDB;
GO

CREATE TABLE categorias (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    descripcion NVARCHAR(255)
);
GO

CREATE TABLE transacciones (
    id INT IDENTITY(1,1) PRIMARY KEY,
    descripcion NVARCHAR(255) NOT NULL,
    monto DECIMAL(18,2) NOT NULL,
    fecha DATE NOT NULL,
    tipo NVARCHAR(50) NOT NULL,
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);
GO

INSERT INTO categorias (nombre, descripcion) VALUES
('Alimentación', 'Compras de comida y restaurantes'),
('Transporte', 'Gasolina, Uber, autobús'),
('Servicios', 'Luz, agua, internet'),
('Salud', 'Medicinas, consultas'),
('Ingresos', 'Salario y otros ingresos');
GO

INSERT INTO transacciones (descripcion, monto, fecha, tipo, categoria_id) VALUES
('Compra supermercado', 35000.00, '2026-02-23', 'GASTO', 1),
('Gasolina', 15000.00, '2026-02-26', 'Gasto', 2),
('Pago de Internet', 25000.00, '2026-03-01', 'gasto', 3),
('Medicamento para la presión', 20000.00, '2026-03-01', 'gasto', 4);
GO