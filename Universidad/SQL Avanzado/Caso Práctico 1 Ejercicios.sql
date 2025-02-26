-- Caso Práctico 1
/* Enunciado
 1. Un ejemplo propio que contenga un Inner Join, un Outer Join y un Exception Join, todos juntos en una misma consulta.
 2. Un ejemplo propio donde demuestre la diferencia entre el ON y el WHERE usando un LEFT OUTER JOIN.
 3. Un ejemplo propio usando el UNION de por lo menos tres consultas.
 4. Un ejemplo propio creando una consulta en donde haga uso de subqueries, deben tener al menos 2 niveles.
 5. Un ejemplo propio donde use por lo menos 4 funciones de agregación, y pueda demostrar si hay diferencias usando el ALL/Distinct y donde haya NULOS dentro de los registros.
 6. Un ejemplo propio donde utilice HAVING.
 7. Un ejemplo propio donde utilice cálculos en columnas que estén dentro de un subquery.
 8. Un ejemplo propio donde utilice top, group by, order by inner join, left join, where, distinct, subquery, union all.
 */

 -- 1. Un ejemplo propio que contenga un Inner Join, un Outer Join y un Exception Join, todos juntos en una misma consulta.

SELECT * FROM [Purchasing].[ProductVendor]
where ProductID = 954;
SELECT * FROM [Production].[Product]
where ProductID = 954;
SELECT * FROM [Sales].[SalesOrderDetail] SOD
where ProductID = 4
or SalesOrderID = 60240;

SELECT 
	PP.ProductID,
	PV.BusinessEntityID,
	SOD.SalesOrderID
FROM [Production].[Product] PP
-- Este Inner Join permite saber que Productos tienen dependencia de un vendor para realizar compras.
INNER JOIN [Purchasing].[ProductVendor] PV ON PV.ProductID = PP.ProductID
-- Con el Full Outer Join permite obtener 3 tipos deinformación sobre los Product IDs 
	-- 1) Productos que Adquiero del Vendor y que no tienen un Sales_Order_ID Asociado.
	-- 2) Productos que Adquiero del Vendor y que tienen un Sales_Order_ID Asociado.
	-- 3) Productos que tengo en la Tabla de Sales_Order que no Adquiero por parte del Vendor.
FULL OUTER JOIN [Sales].[SalesOrderDetail] SOD ON SOD.ProductID = PP.ProductID
-- Exception cuando el producto es null - Productos que tengo en la Tabla de Sales_Order que no Adquiero por parte del Vendor. El Producto depende de mi Fabricación.
WHERE PP.ProductID IS NULL 



-- 2. Un ejemplo propio donde demuestre la diferencia entre el ON y el WHERE usando un LEFT OUTER JOIN.
-- La diferencia entre el ON y el Where radica en que usando "ON" Especificamos que las tablas se unen por medio del identificador y la dirección que nosotros deseamos, 
-- en este caso particular, El LEFT JOIN Indicamos que deseamos todos los productos de la tabla [Production].[WorkOrder] que tienen en común el identificador ProductID del la tabla
-- Producto. Y el Where me permite filtrar el conjunto de datos obtenido mediante el criterio que quiera definir, en este caso deseo saber que el safetyStockLevel sea mayor a 250

SELECT * FROM [Production].[WorkOrder] PW
LEFT OUTER JOIN [Production].[Product] PP ON PP.ProductID = PW.ProductID
WHERE SafetyStockLevel > 250



 -- 3. Un ejemplo propio usando el UNION de por lo menos tres consultas.
 SELECT 
	ProductID,
	Name,
	ProductNumber,
	SafetyStockLevel,
	'UPPER STOCK'	AS CONDITION_STOCK
 FROM [Production].[Product]
 WHERE SafetyStockLevel >= 500
 UNION
 SELECT 
	ProductID,
	Name,
	ProductNumber,
	SafetyStockLevel,
	'UNDER STOCK'	AS CONDITION_STOCK
 FROM [Production].[Product]
 WHERE SafetyStockLevel < 100
 UNION
 SELECT 
	ProductID,
	Name,
	ProductNumber,
	SafetyStockLevel,
	'SAFETY STOCK'	AS CONDITION_STOCK
 FROM [Production].[Product]
 WHERE SafetyStockLevel  >= 100 AND SafetyStockLevel <= 500

 -- 4. Un ejemplo propio creando una consulta en donde haga uso de subqueries, deben tener al menos 2 niveles.
 -- Seleccionalos productos en la tabla producto que están en la tabla de Sales Order Detail con el order qty mayor a 5.
 SELECT * FROM [Production].[Product] PP
 WHERE PP.ProductID IN (SELECT SOD.ProductID FROM [Sales].[SalesOrderDetail] SOD
						WHERE SOD.OrderQty > 5)

--5. Un ejemplo propio donde use por lo menos 4 funciones de agregación, y pueda demostrar si hay diferencias usando el ALL/Distinct y donde haya NULOS dentro de los registros.
SELECT distinct
	Type,
	MIN(MinQty)			min_minQTY,
	MAX(MinQty)			max_minQTY,
	AVG([DiscountPct])	avg_DP,
	SUM([DiscountPct])  sum_DP,
	(SELECT DISTINCT COUNT(MaxQty) FROM [Sales].[SpecialOffer])		DISTINCT_COUNT_Max_qty_NULL,
	(SELECT ALL COUNT(MaxQty) FROM [Sales].[SpecialOffer])			ALL_COUNT_Max_qty_NULL
FROM [Sales].[SpecialOffer]
GROUP BY Type
/*
SELECT * FROM [Sales].[SpecialOffer]
SELECT DISTINCT MaxQty FROM [Sales].[SpecialOffer]
SELECT DISTINCT COUNT(MaxQty) FROM [Sales].[SpecialOffer]
SELECT ALL COUNT(MaxQty) FROM [Sales].[SpecialOffer] COUNT_NULL
SELECT ALL MaxQty FROM [Sales].[SpecialOffer] COUNT_NULL*/

-- 6. Un ejemplo propio donde utilice HAVING.
SELECT  
      ProductID,
	  SUM(orderQty)  AS ORDER_QTY
FROM [Sales].[SalesOrderDetail] SOD
GROUP BY ProductID
HAVING SUM(orderQty) < 100

-- 7. Un ejemplo propio donde utilice cálculos en columnas que estén dentro de un subquery.
SELECT
	PP.ProductID,
	TSOD.TOTAL_ORDER_QTY,
	TSOD.TOTAL_ORDER_QTY * PP.ListPrice AS Total_Price
FROM [Production].[Product] PP 
LEFT JOIN (SELECT ProductID, SUM(OrderQty) AS TOTAL_ORDER_QTY  FROM [Sales].[SalesOrderDetail] SOD GROUP BY ProductID) TSOD ON TSOD.ProductID = PP.ProductID

--8. Un ejemplo propio donde utilice top, group by, order by inner join, left join, where, distinct, subquery, union all.
SELECT DISTINCT UNION_T.ProductID,
				UNION_T.TOTAL_ORDER_QTY,
				PP.NAME FROM (
SELECT TOP 10 TABLE1.ProductID, TABLE1.TOTAL_ORDER_QTY
FROM (SELECT TOP 10 ProductID, SUM(OrderQty) AS TOTAL_ORDER_QTY  FROM [Sales].[SalesOrderDetail] SOD GROUP BY ProductID ORDER BY TOTAL_ORDER_QTY DESC) TABLE1
UNION
SELECT TOP 10 TABLE2.ProductID, TABLE2.TOTAL_ORDER_QTY
FROM (SELECT TOP 10 ProductID, SUM(OrderQty) AS TOTAL_ORDER_QTY  FROM [Sales].[SalesOrderDetail] SOD GROUP BY ProductID ORDER BY TOTAL_ORDER_QTY ASC) TABLE2
UNION ALL
SELECT TABLE3.ProductID, TABLE3.TOTAL_ORDER_QTY
FROM (SELECT ProductID, SUM(OrderQty) AS TOTAL_ORDER_QTY  FROM [Sales].[SalesOrderDetail] SOD GROUP BY ProductID
		HAVING SUM(OrderQty) < 8) TABLE3
) UNION_T
LEFT JOIN [Production].[Product] PP ON PP.ProductID = UNION_T.ProductID
INNER JOIN [Production].[WorkOrder] PW ON PW.ProductID = UNION_T.ProductID
WHERE UNION_T.TOTAL_ORDER_QTY > 20



SELECT *  FROM [Sales].[SalesOrderDetail] SOD