SELECT * FROM USER_TABLES; -- para mostrar todas las tablas del usuario

DROP TABLE InformeCampaña;
DROP TABLE InformePOS;
DROP TABLE InformeProveedor;
DROP TABLE InformeSalarialEmpleado;
DROP TABLE InformeTributario;
DROP TABLE InformeCuentas;

DROP TABLE Pedido;
DROP TABLE Proveedor;

DROP TABLE Contrato;
DROP TABLE OfertaEmpleo;

DROP TABLE Promociona;
DROP TABLE CampañaPublicitaria;
DROP TABLE OfertaProductos;

DROP TABLE LoteProductos;
DROP TABLE Almacen;


-- COMMIT; -- creo que no es necesario tras hacer DROP TABLE

SELECT * FROM INFORMECUENTAS;
SELECT * FROM CAMPAÑAPUBLICITARIA;
SELECT * FROM PROMOCIONA;
SELECT * FROM OFERTAPRODUCTOS;

SELECT * FROM CONTRATO;
SELECT * FROM OFERTAEMPLEO;
SELECT * FROM PEDIDO;
SELECT * FROM PROVEEDOR;
ALTER SESSION SET PLSCOPE_SETTINGS = 'IDENTIFIERS:NONE'; 
-- lo tuve que añadir para poder compilar un trigger que no me dejaba por error en algún momento