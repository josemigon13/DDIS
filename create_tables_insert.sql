-- creación de tablas del área funconal de Almacén
CREATE TABLE Almacen(
    IdAlmacen VARCHAR2(20) PRIMARY KEY NOT NULL,
    Direccion VARCHAR2(50), 
    Superficie FLOAT,
    FechaInicioAlquiler_Alm DATE,
    FechaFinAlquiler_Alm DATE
);

CREATE TABLE LoteProductos(
    IdLote VARCHAR2(20) PRIMARY KEY NOT NULL,
    IdAlmacen VARCHAR2(20) NOT NULL REFERENCES Almacen(IdAlmacen),
    Descripcion_Lote VARCHAR2(20),
    Unidad VARCHAR2(20),
    Cantidad INTEGER,
    Coste_Lote FLOAT
);

-- inserción de tuplas en tablas del área funconal de Almacén
INSERT INTO Almacen (IdAlmacen, Direccion, Superficie, FechaInicioAlquiler_Alm, FechaFinAlquiler_Alm)
VALUES ('Alm1','Calle Periodistas','1000', TO_DATE('2021/12/14','yyyy-mm-dd'), TO_DATE('2022/12/14','yyyy-mm-dd'));

INSERT INTO Almacen (IdAlmacen, Direccion, Superficie, FechaInicioAlquiler_Alm, FechaFinAlquiler_Alm)
VALUES ('Alm2','Calle Fruteros','500', TO_DATE('2021/12/14','yyyy-mm-dd'), TO_DATE('2023/12/14','yyyy-mm-dd'));

INSERT INTO Almacen (IdAlmacen, Direccion, Superficie, FechaInicioAlquiler_Alm, FechaFinAlquiler_Alm)
VALUES ('Alm3','Calle Panaderos','5000', TO_DATE('2021/11/25','yyyy-mm-dd'), TO_DATE('2022/11/25','yyyy-mm-dd'));

INSERT INTO Almacen (IdAlmacen, Direccion, Superficie, FechaInicioAlquiler_Alm, FechaFinAlquiler_Alm)
VALUES ('Alm4','Calle Ingenieros','1000', TO_DATE('2021/11/25','yyyy-mm-dd'), TO_DATE('2023/11/25','yyyy-mm-dd'));

INSERT INTO Almacen (IdAlmacen, Direccion, Superficie, FechaInicioAlquiler_Alm, FechaFinAlquiler_Alm)
VALUES ('Alm5','Calle Médicos','2000', TO_DATE('2021/7/1','yyyy-mm-dd'), TO_DATE('2022/7/1','yyyy-mm-dd'));

INSERT INTO Almacen (IdAlmacen, Direccion, Superficie, FechaInicioAlquiler_Alm, FechaFinAlquiler_Alm)
VALUES ('Alm6','Calle Policías','1500', TO_DATE('2021/7/1','yyyy-mm-dd'), TO_DATE('2023/7/1','yyyy-mm-dd'));

INSERT INTO Almacen (IdAlmacen, Direccion, Superficie, FechaInicioAlquiler_Alm, FechaFinAlquiler_Alm)
VALUES ('Alm7','Calle Políticos','1255,67', TO_DATE('2021/10/5','yyyy-mm-dd'), TO_DATE('2022/10/5','yyyy-mm-dd'));

INSERT INTO Almacen (IdAlmacen, Direccion, Superficie, FechaInicioAlquiler_Alm, FechaFinAlquiler_Alm)
VALUES ('Alm8','Calle Mecánicos','1700', TO_DATE('2021/10/5','yyyy-mm-dd'), TO_DATE('2023/10/5','yyyy-mm-dd'));

INSERT INTO Almacen (IdAlmacen, Direccion, Superficie, FechaInicioAlquiler_Alm, FechaFinAlquiler_Alm)
VALUES ('Alm9','Calle Profesores','2000', TO_DATE('2021/9/9','yyyy-mm-dd'), TO_DATE('2022/9/9','yyyy-mm-dd'));

INSERT INTO Almacen (IdAlmacen, Direccion, Superficie, FechaInicioAlquiler_Alm, FechaFinAlquiler_Alm)
VALUES ('Alm10','Calle Te Falta Calle','1000', TO_DATE('2021/9/9','yyyy-mm-dd'), TO_DATE('2023/9/9','yyyy-mm-dd'));

INSERT INTO LoteProductos (IdLote, IdAlmacen, Descripcion_Lote, Unidad, Cantidad, Coste_Lote)
VALUES ('Lote1','Alm1','Tomates','Sacos de 1kg','10','15,00');

INSERT INTO LoteProductos (IdLote, IdAlmacen, Descripcion_Lote, Unidad, Cantidad, Coste_Lote)
VALUES ('Lote2','Alm1','Queso Parmesano','Pedazo de 1kg','5','41,00');

INSERT INTO LoteProductos (IdLote, IdAlmacen, Descripcion_Lote, Unidad, Cantidad, Coste_Lote)
VALUES ('Lote3','Alm1','Harina tipo 00','Sacos de 5kg','10','30,00');

INSERT INTO LoteProductos (IdLote, IdAlmacen, Descripcion_Lote, Unidad, Cantidad, Coste_Lote)
VALUES ('Lote4','Alm2','Agua mineral natural','Botellas de 1.5L','100','67,00');

INSERT INTO LoteProductos (IdLote, IdAlmacen, Descripcion_Lote, Unidad, Cantidad, Coste_Lote)
VALUES ('Lote5','Alm2','Agua mineral natural','Botellas de 1.5L','100','67,00');

INSERT INTO LoteProductos (IdLote, IdAlmacen, Descripcion_Lote, Unidad, Cantidad, Coste_Lote)
VALUES ('Lote6','Alm3','Queso Mozzarella','Paquetes de 250g','20','100,00');

INSERT INTO LoteProductos (IdLote, IdAlmacen, Descripcion_Lote, Unidad, Cantidad, Coste_Lote)
VALUES ('Lote7','Alm4','Spaghetti nº15','Paquetes de 500g','20','42,80');

INSERT INTO LoteProductos (IdLote, IdAlmacen, Descripcion_Lote, Unidad, Cantidad, Coste_Lote)
VALUES ('Lote8','Alm5','Macarrones','Paquetes de 400g','12','31,90');

INSERT INTO LoteProductos (IdLote, IdAlmacen, Descripcion_Lote, Unidad, Cantidad, Coste_Lote)
VALUES ('Lote9','Alm6','Harina tipo 00','Sacos de 5kg','10','30,00');

INSERT INTO LoteProductos (IdLote, IdAlmacen, Descripcion_Lote, Unidad, Cantidad, Coste_Lote)
VALUES ('Lote10','Alm7','Tomates','Sacos de 1kg','10','15,00');

-- creación de tablas del área funconal de Logística
CREATE TABLE Proveedor
(
	NumProveedor INT PRIMARY KEY,
	Nombre_Prov VARCHAR2( 40 ),
	DireccionWeb_Prov VARCHAR2( 20 ),
	Tlf_Prov VARCHAR2( 20 )
);

CREATE TABLE Pedido
(
	NumPedido INT PRIMARY KEY,
	Articulos VARCHAR2( 200 ),
	Fecha_Ped DATE,
	Precio_Ped FLOAT,
	CONSTRAINT Precio_Ped_positivo CHECK (Precio_Ped>0)
);




-- inserción de tuplas en tablas del área funconal de Logística
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




INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (1, 'Jamón serrano 50kg', TO_DATE( '1/1/2021', 'DD/MM/YYYY' ), 500);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (2, 'Aceitunas picual 40kg', TO_DATE( '2/2/2021', 'DD/MM/YYYY' ), 200);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (3, 'Mozzarella de buffala 20kg', TO_DATE( '3/3/2021', 'DD/MM/YYYY' ), 220);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (4, 'Burrata 150kg', TO_DATE( '4/4/2021', 'DD/MM/YYYY' ), 700);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (5, 'Pecorino romano 25kg', TO_DATE( '5/5/2021', 'DD/MM/YYYY' ), 150);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (6, 'Farina 100kg, frumento 80kg', TO_DATE( '6/6/2021', 'DD/MM/YYYY' ), 120);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (7, 'Grana padano 50kg', TO_DATE( '7/7/2021', 'DD/MM/YYYY' ), 300);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (8, 'Mascarpone 30kg', TO_DATE( '8/8/2021', 'DD/MM/YYYY' ), 350);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (9, 'Gorgonzola 70kg', TO_DATE( '9/9/2021', 'DD/MM/YYYY' ), 170);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (10, 'Provolone 40kg', TO_DATE( '10/10/2021', 'DD/MM/YYYY' ), 370);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (11, 'Queso cabrales 40kg', TO_DATE( '10/10/2021', 'DD/MM/YYYY' ), 240);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (12, 'Vino chianti 10l', TO_DATE( '12/12/2021', 'DD/MM/YYYY' ), 250);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (13, 'Vino marsala 15l', TO_DATE( '10/10/2021', 'DD/MM/YYYY' ), 200);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (14, 'Amaretto 10l', TO_DATE( '10/10/2021', 'DD/MM/YYYY' ), 150);

INSERT INTO Pedido (NumPedido, Articulos, Fecha_Ped, Precio_Ped)
VALUES (15, 'Prosciuto 50kg', TO_DATE( '11/11/2021', 'DD/MM/YYYY' ), 400);


-- creación de tablas del área funconal de Marketing
CREATE TABLE CampañaPublicitaria(
    IdCampaña VARCHAR2(10) PRIMARY KEY NOT NULL,
    Nombre_CampPub VARCHAR2(40),
    Descripcion_CampPub VARCHAR2(100),
    Precio_CampPub FLOAT,
    ListaMediosEmision VARCHAR2(100),
    FechaIni_CampPub DATE,
    FechaFin_CampPub DATE,
    CONSTRAINT Fecha_CampPub_Ini_Ant_Fin 
    CHECK (FechaIni_CampPub <= FechaFin_CampPub)
);

CREATE TABLE OfertaProductos(
    IdOfertaProd VARCHAR2(10) PRIMARY KEY NOT NULL,
    Nombre_OferProd VARCHAR2(40),
    ListaProductos VARCHAR2(100),
    Precio_OferProd FLOAT,
    FechaIni_OferProd DATE,
    FechaFin_OferProd DATE,
    CONSTRAINT Fecha_OferProd_Ini_Ant_Fin
    CHECK (FechaIni_OferProd <= FechaFin_OferProd)
);

CREATE TABLE Promociona(
    IdCampaña VARCHAR2(10) NOT NULL REFERENCES CampañaPublicitaria(IdCampaña),
    IdOfertaProd VARCHAR2(10) NOT NULL REFERENCES OfertaProductos(IdOfertaProd),
    PRIMARY KEY (IdCampaña, IdOfertaProd)
);

-- inserción de tuplas en tablas del área funconal de Marketing
INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, 
        Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-1', 'Campaña Margarita', 'Realce de la pizza margarita', 
        '1000', 'La1, A3, L6, Cuatro, Tele5', 
        TO_DATE('2022/1/7','yyyy-mm-dd'), TO_DATE('2022/1/21','yyyy-mm-dd'));
        
INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, 
        Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-2', 'Campaña Calzone de la Casa', 
        'Ofrecer calzone al horno artesano importado de la zona florentina', 
        '850,50', 'A3, Cuatro, Tele5', 
        TO_DATE('2022/1/14','yyyy-mm-dd'), TO_DATE('2022/1/28','yyyy-mm-dd'));
        
INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, 
        Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-3', 'Campaña Barbacoa', 'Realce de la pizza y calzone a la barbacoa', 
        '499,99', 'La1, L6, Tele5', 
        TO_DATE('2022/1/10','yyyy-mm-dd'), TO_DATE('2022/1/28','yyyy-mm-dd'));
        
INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, 
        Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-4', 'Campaña Rabbioli', 
        'Especial de la casa de la pasta rabbioli importado de Roma', '200', 'La1, Tele5', 
        TO_DATE('2022/1/7','yyyy-mm-dd'), TO_DATE('2022/1/26','yyyy-mm-dd'));
        
INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, 
        Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-5', 'Campaña Parmesano', 'Ofrecer pizza y lasagna con el mejor queso parmesano',
        '1000', 'Canal Sur, A3, L6, Cuatro, Tele5', 
        TO_DATE('2022/1/10','yyyy-mm-dd'), TO_DATE('2022/1/21','yyyy-mm-dd'));
        
INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, 
        Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-6', 'Campaña al son italiano', 
        'Ofrecer platos de degustación con ingredientes exclusivos de Venecia y Florencia', 
        '1000', 'La 1, RadioMarca, A3, L6, Cuatro, Tele5', 
        TO_DATE('2022/1/7','yyyy-mm-dd'), TO_DATE('2022/1/21','yyyy-mm-dd'));
        
INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, 
        Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-7', 'Campaña a la romana', 
        'Ofrecer platos de degustación con ingredientes exclusivos de la capital italiana',
        '999,99', 'Mediaset, Atresmedia',
        TO_DATE('2022/1/1','yyyy-mm-dd'), TO_DATE('2022/1/20','yyyy-mm-dd'));
        
INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, 
        Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-8', 'Campaña a la mozzarella', 
        'Ofrecer platos con el mejor queso mozzarella del país', '899', 'La1, L6', 
        TO_DATE('2022/1/11','yyyy-mm-dd'), TO_DATE('2022/1/29','yyyy-mm-dd'));
        
INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, 
        Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-9', 'Campaña Risotto alla milanese',
        'Especial de la casa del mejor arroz a la milanesa importado de Roma',
        '459', 'Canal Sur, RadioMarca',
        TO_DATE('2022/1/14','yyyy-mm-dd'), TO_DATE('2022/1/30','yyyy-mm-dd'));
        
INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, 
        Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-10', 'Campaña Carpaccio y Pasta veneciana',
        'Especial de la casa del mejor carpaccio importado del norte de Italia',
        '1299,59', 'Mediaset, Atresmedia', 	
        TO_DATE('2022/1/5','yyyy-mm-dd'), TO_DATE('2022/1/25','yyyy-mm-dd'));


INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos,
                Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-1', 'Oferta Menú-Margarita', 'Pizza Margarita, entremeses, bebida, postre', 
        '8,80', TO_DATE('2022/1/1','yyyy-mm-dd'), TO_DATE('2022/1/30','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos,
                Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-2', 'Oferta Bebida Extra Grande', 'Bebida XL', '2,80',
        TO_DATE('2022/1/1','yyyy-mm-dd'), TO_DATE('2022/1/30','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos,
                Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-3', 'Oferta Bebida Mediana', 'Bebida Mediana', '1,50',
        TO_DATE('2022/1/1','yyyy-mm-dd'), TO_DATE('2022/1/30','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos,
                Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-4', 'Oferta Menú-Barbacoa', 'Calzone, pizza barbacoa, bebida, postre', '11,80',
        TO_DATE('2022/1/1','yyyy-mm-dd'), TO_DATE('2022/1/30','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos,
                Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-5', 'Oferta Menú Al Parmesano', 
        'Pizza con Extra Parmesano, rabbioli al Forno Parmesano, bebida, postre', '12,50',
        TO_DATE('2022/1/4','yyyy-mm-dd'), TO_DATE('2022/1/27','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos,
                Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-6', 'Oferta Menú-Calzone-Speziale', 
        'Calzone de la casa, entrante de carne al parmesano, bebida, postre', '8,80',
        TO_DATE('2022/1/1','yyyy-mm-dd'), TO_DATE('2022/1/30','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos,
                Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-7', 'Oferta 2x1 Pizza 8 Formaggi', '2 Pizzas 8 Formaggi, bebida', '7,90',
        TO_DATE('2022/1/4','yyyy-mm-dd'), TO_DATE('2022/2/4','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos,
                Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-8', 'Oferta Menú-Toscano', 'Pizza a la Toscana, bebida, postre', '8,80',
        TO_DATE('2022/1/1','yyyy-mm-dd'), TO_DATE('2022/2/10','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos,
                Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-9', 'Oferta Menú-Veneciano', 
        'Pizza a la Veneciana e funghi, bebida, fritteli venecianos', '10,80',
        TO_DATE('2022/1/3','yyyy-mm-dd'), TO_DATE('2022/2/15','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos,
                Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-10', 'Oferta Menú-Degustación', 
        'Mini Pizza de la casa con rabbioli, pasta al pomodoro, bebida, postre casero', 
        '8,80', TO_DATE('2022/1/7','yyyy-mm-dd'), TO_DATE('2022/1/28','yyyy-mm-dd'));

INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-1', 'OP-1');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-1', 'OP-2');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-1', 'OP-3');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-2', 'OP-6');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-2', 'OP-2');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-3', 'OP-4');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-4', 'OP-5');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-4', 'OP-10');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-5', 'OP-2');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-5', 'OP-6');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-5', 'OP-5');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-6', 'OP-7');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-6', 'OP-8');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-6', 'OP-9');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-6', 'OP-10');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-7', 'OP-10');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-8', 'OP-3');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-9', 'OP-3');
INSERT INTO Promociona (IdCampaña, IdOfertaProd) VALUES ('CP-10', 'OP-9');

-- creación de tablas del área funconal de Recursos Humanos
CREATE TABLE OfertaEmpleo (
    IDOfertaEmpleo VARCHAR(9) PRIMARY KEY,
    ListadoEmpleos VARCHAR(100),
    FechaIni_OferEmp DATE,
    FechaFin_OferEmp DATE
);

CREATE TABLE Contrato (
    DNI VARCHAR(9) PRIMARY KEY,
    IDOfertaEmpleo VARCHAR(9),
    Nombre_Empleado VARCHAR(30),
    Tlf_Empleado INT,
    NumSegSocial INT,
    Salario DECIMAL,
    FOREIGN KEY (IDOfertaEmpleo) REFERENCES OfertaEmpleo(IDOfertaEmpleo)
);

-- inserción de tuplas en tablas del área funconal de Recursos Humanos
INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) 
VALUES(1,'chef', '01/01/21', '01/01/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) 
VALUES(2,'pinche', '11/01/21', '11/01/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) 
VALUES(3,'administrador', '15/01/21', '15/01/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) 
VALUES(4,'encargado', '21/01/21', '21/01/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) 
VALUES(5,'control de calidad', '02/03/21', '02/03/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) 
VALUES(6,'camarero', '01/04/21', '01/04/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) 
VALUES(7,'barman', '21/05/21', '21/05/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) 
VALUES(8,'proveedor de productos', '14/06/21', '14/06/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) 
VALUES(9,'nutricionista', '06/07/21', '06/07/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) 
VALUES(10,'camarero', '18/08/21', '18/08/22');


INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) 
VALUES('12345678X', 1, 'Carlos Fernández Castro', 784096793, 1726381901, 2200);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) 
VALUES('12345678Y', 2, 'Tomás Galiana García', 721083092, 1726381901, 1200);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) 
VALUES('12345678A', 3, 'Alicia Fernández Fernández', 618293018, 1726381901, 2300);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) 
VALUES('12345678W', 4, 'Carlos González Pérez', 692758223, 1726381901, 2000);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) 
VALUES('12345678Z', 5, 'Lucía Pérez Maraver', 639472783, 1726381901, 1200);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) 
VALUES('70391935M', 6, 'Carlos García Galiana', 639283749, 1726381901, 1300);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) 
VALUES('65391174B', 7, 'Tomás Fernández Sáez', 601928354, 1726381901, 2200);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) 
VALUES('27191630T', 8, 'Gerardo González García', 620988655, 1726381901, 2300);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) 
VALUES('68391601U', 9, 'Francisco Galiana Martínez', 617264906, 1726381901, 1900);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) 
VALUES('77135672J', 10, 'Laura Fernández García', 695647890, 1726381901, 1500);

-- creación de tablas del área funconal de Contabilidad
CREATE TABLE InformeCuentas(
    IdInforme INT NOT NULL,
    Fecha_Informe DATE NOT NULL,
    PRIMARY KEY(IdInforme)
);

CREATE TABLE InformeCampaña(
    IdInforme INT NOT NULL,
    IdCampaña VARCHAR2(10) NOT NULL,
    FOREIGN KEY (IdInforme) REFERENCES InformeCuentas(IdInforme),
    FOREIGN KEY (IdCampaña) REFERENCES CampañaPublicitaria(IdCampaña),
    PRIMARY KEY(IdInforme)
);

CREATE TABLE InformeSalarialEmpleado(
    IdInforme INT NOT NULL,
    DNI VARCHAR2(10) NOT NULL,
    FOREIGN KEY (IdInforme) REFERENCES InformeCuentas(IdInforme),
    FOREIGN KEY (DNI) REFERENCES Contrato(DNI),
    PRIMARY KEY(IdInforme)
);

CREATE TABLE InformeProveedor(
    IdInforme INT NOT NULL,
    NumProveedor INT NOT NULL,
    FOREIGN KEY (IdInforme) REFERENCES InformeCuentas(IdInforme),
    FOREIGN KEY (NumProveedor) REFERENCES Proveedor(NumProveedor),
    PRIMARY KEY(IdInforme)
);

CREATE TABLE InformeTributario(
    IdInforme INT NOT NULL,
    ImporteTributario FLOAT NOT NULL,
    FOREIGN KEY (IdInforme) REFERENCES InformeCuentas(IdInforme),
    PRIMARY KEY(IdInforme)
);

CREATE TABLE InformePOS(
    IdInforme INT NOT NULL,
    BeneficiosPOS FLOAT NOT NULL,
    CodigoPOS INT NOT NULL,
    FOREIGN KEY (IdInforme) REFERENCES InformeCuentas(IdInforme),
    PRIMARY KEY(IdInforme)
);


-- inserción de tuplas en tablas del área funconal de Contabilidad

-- Inserción de tuplas para un informe salarial de empleado

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(1,'01/01/22');
INSERT INTO InformeSalarialEmpleado(IdInforme, DNI) VALUES(1,'12345678X');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(2,'01/02/22');
INSERT INTO InformeSalarialEmpleado(IdInforme, DNI) VALUES(2,'12345678X');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(3,'01/01/22');
INSERT INTO InformeSalarialEmpleado(IdInforme, DNI) VALUES(3,'12345678Y');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(4,'01/02/22');
INSERT INTO InformeSalarialEmpleado(IdInforme, DNI) VALUES(4,'12345678Y');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(5,'01/01/22');
INSERT INTO InformeSalarialEmpleado(IdInforme, DNI) VALUES(5,'12345678A');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(6,'01/02/22');
INSERT INTO InformeSalarialEmpleado(IdInforme, DNI) VALUES(6,'12345678A');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(7,'01/01/22');
INSERT INTO InformeSalarialEmpleado(IdInforme, DNI) VALUES(7,'12345678W');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(8,'01/02/22');
INSERT INTO InformeSalarialEmpleado(IdInforme, DNI) VALUES(8,'12345678W');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(9,'01/01/22');
INSERT INTO InformeSalarialEmpleado(IdInforme, DNI) VALUES(9,'12345678Z');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(10,'01/02/22');
INSERT INTO InformeSalarialEmpleado(IdInforme, DNI) VALUES(10,'12345678Z');

-- Inserción de tuplas para un informe de proveedor

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(11,'01/01/22');
INSERT INTO InformeProveedor(IdInforme, NumProveedor) VALUES(11,1);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(12,'01/01/22');
INSERT INTO InformeProveedor(IdInforme, NumProveedor) VALUES(12,2);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(13,'01/01/22');
INSERT INTO InformeProveedor(IdInforme, NumProveedor) VALUES(13,3);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(14,'01/01/22');
INSERT INTO InformeProveedor(IdInforme, NumProveedor) VALUES(14,4);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(15,'01/01/22');
INSERT INTO InformeProveedor(IdInforme, NumProveedor) VALUES(15,5);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(16,'01/01/22');
INSERT INTO InformeProveedor(IdInforme, NumProveedor) VALUES(16,6);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(17,'01/01/22');
INSERT INTO InformeProveedor(IdInforme, NumProveedor) VALUES(17,7);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(18,'01/01/22');
INSERT INTO InformeProveedor(IdInforme, NumProveedor) VALUES(18,8);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(19,'01/01/22');
INSERT INTO InformeProveedor(IdInforme, NumProveedor) VALUES(19,9);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(20,'01/01/22');
INSERT INTO InformeProveedor(IdInforme, NumProveedor) VALUES(20,10);

-- Inserción de tuplas para un informe de campaña publicitaria

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(21,'01/01/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(21, 'CP-1');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(22,'01/01/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(22, 'CP-2');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(23,'01/02/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(23, 'CP-3');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(24,'01/03/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(24, 'CP-4');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(25,'01/03/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(25, 'CP-5');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(26,'01/04/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(26, 'CP-6');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(27,'01/01/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(27, 'CP-7');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(28,'01/04/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(28, 'CP-8');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(29,'01/06/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(29, 'CP-9');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(30,'01/02/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(30, 'CP-10');

-- Inserción de tuplas para un informe tributario

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(31,'01/01/22');
INSERT INTO InformeTributario(IdInforme, ImporteTributario) VALUES(31, 79000.00);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(32,'01/02/22');
INSERT INTO InformeTributario(IdInforme, ImporteTributario) VALUES(32, 93000.00);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(33,'01/03/22');
INSERT INTO InformeTributario(IdInforme, ImporteTributario) VALUES(33, 125000.00);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(34,'01/04/22');
INSERT INTO InformeTributario(IdInforme, ImporteTributario) VALUES(34, 115000.00);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(35,'01/05/22');
INSERT INTO InformeTributario(IdInforme, ImporteTributario) VALUES(35, 25000.00);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(36,'01/06/22');
INSERT INTO InformeTributario(IdInforme, ImporteTributario) VALUES(36, 85000.00);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(37,'01/07/22');
INSERT INTO InformeTributario(IdInforme, ImporteTributario) VALUES(37, 170000.00);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(38,'01/08/22');
INSERT INTO InformeTributario(IdInforme, ImporteTributario) VALUES(38, 132000.00);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(39,'01/09/22');
INSERT INTO InformeTributario(IdInforme, ImporteTributario) VALUES(39, 95000.00);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(40,'01/10/22');
INSERT INTO InformeTributario(IdInforme, ImporteTributario) VALUES(40, 208000.00);

-- Inserción de tuplas para un informe de punto de venta

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(41,'01/01/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(41, 1599.00, 1);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(42,'01/02/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(42, 1899.00, 1);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(43,'01/03/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(43, 1999.00, 1);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(44,'01/01/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(44, 2739.00, 2);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(45,'01/02/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(45, 2839.00, 2);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(46,'01/01/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(46, 2239.00, 3);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(47,'01/01/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(47, 2739.00, 4);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(48,'01/01/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(48, 3199.00, 5);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(49,'01/01/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(49, 2739.00, 6);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(50,'01/02/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(50, 4619.00, 6);

COMMIT; -- para hacer efectivas las inserciones
