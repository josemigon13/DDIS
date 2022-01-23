-- creación de tablas
CREATE TABLE Proveedor
(
	NumProveedor INT PRIMARY KEY,
	Nombre_Prov VARCHAR2( 40 ),
	DireccionWeb_Prov VARCHAR2( 20 ) UNIQUE,  estos 2 atributos podrían ser UNIQUE pero por simplicidad NO los indico como tal
	Tlf_Prov VARCHAR2( 20 ) UNIQUE
);

CREATE TABLE PedidoProveeSeEnvia
(
	NumPedido INT PRIMARY KEY,
	NumProveedor NOT NULL REFERENCES Proveedor( NumProveedor ),
	IdAlmacen NOT NULL REFERENCES Almacen( IdAlmacen ),
	Articulos VARCHAR2( 200 ),
	Fecha_Ped DATE,  -- CHECK Fecha_Ped>=SYSDATE,
	Precio_Ped FLOAT,
	
	CONSTRAINT precio_pedido_positivo CHECK Precio_Ped>0  -- en euros
);



-- inserción de tuplas en las tablas creadas
-- 10 tuplas de proveedores
INSERT INTO Proveedor (NumProveedor, Nombre_Prov, DireccionWeb_Prov, Tlf_Prov)
	VALUES (1, 'Proveo S.A.', 'www.proveo.com', '+34611111111');

INSERT INTO Proveedor (NumProveedor, Nombre_Prov, DireccionWeb_Prov, Tlf_Prov)
	VALUES (2, 'Provees S.A.', 'www.provees.com', '+39622222222');

INSERT INTO Proveedor (NumProveedor, Nombre_Prov, DireccionWeb_Prov, Tlf_Prov)
	VALUES (3, 'Provee S.A.', 'www.provee.com', '+39633333333');

INSERT INTO Proveedor (NumProveedor, Nombre_Prov, DireccionWeb_Prov, Tlf_Prov)
	VALUES (4, 'Proveemos S.A.', 'www.proveemos.com', '+39644444444');

INSERT INTO Proveedor (NumProveedor, Nombre_Prov, DireccionWeb_Prov, Tlf_Prov)
	VALUES (5, 'Proveéis S.A.', 'www.proveéis.com', '+39655555555');

INSERT INTO Proveedor (NumProveedor, Nombre_Prov, DireccionWeb_Prov, Tlf_Prov)
	VALUES (6, 'Proveen S.A.', 'www.proveen.com', '+34666666666');

INSERT INTO Proveedor (NumProveedor, Nombre_Prov, DireccionWeb_Prov, Tlf_Prov)
	VALUES (7, 'Proveía S.A.', 'www.proveía.com', '+39677777777');

INSERT INTO Proveedor (NumProveedor, Nombre_Prov, DireccionWeb_Prov, Tlf_Prov)
	VALUES (8, 'Proveías S.A.', 'www.proveías.com', '+39688888888');

INSERT INTO Proveedor (NumProveedor, Nombre_Prov, DireccionWeb_Prov, Tlf_Prov)
	VALUES (9, 'Proveíamos S.A.', 'www.proveíamos.com', '+39699999999');

INSERT INTO Proveedor (NumProveedor, Nombre_Prov, DireccionWeb_Prov, Tlf_Prov)
	VALUES (10, 'Proveíais S.A.', 'www.proveíais.com', '+39612345678');


-- 15 tuplas de pedidos
INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (1, 'Jamón serrano 50kg', 1, 'Alm1', TO_DATE( '1/1/2021', 'DD/MM/YYYY' ), 500);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (2, 'Aceitunas picual 40kg', 1, 'Alm2', TO_DATE( '2/2/2021', 'DD/MM/YYYY' ), 200);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (3, 'Mozzarella de buffala 20kg', 2, 'Alm3', TO_DATE( '3/3/2021', 'DD/MM/YYYY' ), 220);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (4, 'Burrata 150kg', 2, 'Alm4', TO_DATE( '4/4/2021', 'DD/MM/YYYY' ), 700);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (5, 'Pecorino romano 25kg', 3, 'Alm5', TO_DATE( '5/5/2021', 'DD/MM/YYYY' ), 150);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (6, 'Farina 100kg, frumento 80kg', 3, 'Alm6', TO_DATE( '6/6/2021', 'DD/MM/YYYY' ), 120);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (7, 'Grana padano 50kg', 4, 'Alm7', TO_DATE( '7/7/2021', 'DD/MM/YYYY' ), 300);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (8, 'Mascarpone 30kg', 4, 'Alm8', TO_DATE( '8/8/2021', 'DD/MM/YYYY' ), 350);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (9, 'Gorgonzola 70kg', 5, 'Alm9', TO_DATE( '9/9/2021', 'DD/MM/YYYY' ), 170);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (10, 'Provolone 40kg', 5, 'Alm10', TO_DATE( '10/10/2021', 'DD/MM/YYYY' ), 370);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (11, 'Queso cabrales 40kg', 1, 'Alm1', TO_DATE( '10/10/2021', 'DD/MM/YYYY' ), 240);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (12, 'Vino chianti 10l', 1, 'Alm1', TO_DATE( '12/12/2021', 'DD/MM/YYYY' ), 250);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (13, 'Vino marsala 15l', 1, 'Alm1', TO_DATE( '10/10/2021', 'DD/MM/YYYY' ), 200);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (14, 'Amaretto 10l', 1, 'Alm1', TO_DATE( '10/10/2021', 'DD/MM/YYYY' ), 150);

INSERT INTO PedidoProveeSeEnvia (NumPedido, NumProveedor, IdAlmacen, Articulos, Fecha_Ped, Precio_Ped)
	VALUES (15, 'Prosciuto 50kg', 1, 'Alm1', TO_DATE( '11/11/2021', 'DD/MM/YYYY' ), 400);


COMMIT; -- para hacer efectivas las inserciones
