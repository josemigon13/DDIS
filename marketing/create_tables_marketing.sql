-- Los atirbutos de las tablas - pendiente revisión sobre cuáles deberían ser NOT NULL en realidad

CREATE TABLE CampañaPublicitaria(
    IdCampaña VARCHAR2(10) PRIMARY KEY NOT NULL,
    Nombre_CampPub VARCHAR2(40) NOT NULL,
    Descripcion_CampPub VARCHAR2(100),
    Precio_CampPub FLOAT NOT NULL,
    ListaMediosEmision VARCHAR2(100) NOT NULL,
    FechaIni_CampPub DATE NOT NULL,
    FechaFin_CampPub DATE NOT NULL
);

CREATE TABLE OfertaProductos(
    IdOfertaProd VARCHAR2(10) PRIMARY KEY NOT NULL,
    Nombre_OferProd VARCHAR2(40) NOT NULL,
    ListaProductos VARCHAR2(100) NOT NULL,
    Precio_OferProd FLOAT NOT NULL,
    FechaIni_OferProd DATE NOT NULL,
    FechaFin_OferProd DATE NOT NULL
);

CREATE TABLE Promociona(
    IdCampaña VARCHAR2(10) NOT NULL REFERENCES CampañaPublicitaria(IdCampaña),
    IdOfertaProd VARCHAR2(10) NOT NULL REFERENCES OfertaProductos(IdOfertaProd),
    PRIMARY KEY (IdCampaña, IdOfertaProd)
);

INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-1', 'Campaña Margarita', 'Realce de la pizza margarita', '1000', 'La1, A3, L6, Cuatro, Tele5', 
        TO_DATE('2022/1/7','yyyy-mm-dd'), TO_DATE('2022/1/21','yyyy-mm-dd'));

INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-2', 'Campaña Calzone de la Casa', 'Ofrecer calzone al horno artesano importado de la zona florentina', '850,50', 'A3, Cuatro, Tele5', 
        TO_DATE('2022/1/14','yyyy-mm-dd'), TO_DATE('2022/1/28','yyyy-mm-dd'));


INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-3', 'Campaña Barbacoa', 'Realce de la pizza y calzone a la barbacoa', '499,99', 'La1, L6, Tele5', 
        TO_DATE('2022/1/10','yyyy-mm-dd'), TO_DATE('2022/1/28','yyyy-mm-dd'));

INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-4', 'Campaña Rabbioli', 'Especial de la casa de la pasta rabbioli importado de Roma', '200', 'La1, Tele5', 
        TO_DATE('2022/1/7','yyyy-mm-dd'), TO_DATE('2022/1/26','yyyy-mm-dd'));

INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-5', 'Campaña Parmesano', 'Ofrecer pizza y lasagna con el mejor queso parmesano', '1000', 'Canal Sur, A3, L6, Cuatro, Tele5', 
        TO_DATE('2022/1/10','yyyy-mm-dd'), TO_DATE('2022/1/21','yyyy-mm-dd'));

INSERT INTO CampañaPublicitaria (IdCampaña, Nombre_CampPub, Descripcion_CampPub, Precio_CampPub, ListaMediosEmision, FechaIni_CampPub, FechaFin_CampPub)
VALUES ('CP-6', 'Campaña al son italiano', 'Ofrecer platos de degustación con ingredientes exclusivos de Venecia y Florencia', '1000', 'La 1, RadioMarca, A3, L6, Cuatro, Tele5', 
        TO_DATE('2022/1/7','yyyy-mm-dd'), TO_DATE('2022/1/21','yyyy-mm-dd'));


INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos, Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-1', 'Oferta Menú-Margarita', 'Pizza Margarita, entremeses, bebida, postre', '8,80',
        TO_DATE('2022/1/1','yyyy-mm-dd'), TO_DATE('2022/1/30','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos, Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-2', 'Oferta Bebida Extra Grande', 'Bebida XL', '2,80',
        TO_DATE('2022/1/1','yyyy-mm-dd'), TO_DATE('2022/1/30','yyyy-mm-dd'));

INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos, Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-3', 'Oferta Bebida Mediana', 'Bebida Mediana', '1,50',
        TO_DATE('2022/1/1','yyyy-mm-dd'), TO_DATE('2022/1/30','yyyy-mm-dd'));

INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos, Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-4', 'Oferta Menú-Barbacoa', 'Calzone, pizza barbacoa, bebida, postre', '11,80',
        TO_DATE('2022/1/1','yyyy-mm-dd'), TO_DATE('2022/1/30','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos, Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-5', 'Oferta Menú Al Parmesano', 'Pizza con Extra Parmesano, rabbioli al Forno Parmesano, bebida, postre', '12,50',
        TO_DATE('2022/1/4','yyyy-mm-dd'), TO_DATE('2022/1/27','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos, Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-6', 'Oferta Menú-Calzone-Speziale', 'Calzone de la casa, entrante de carne al parmesano, bebida, postre', '8,80',
        TO_DATE('2022/1/1','yyyy-mm-dd'), TO_DATE('2022/1/30','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos, Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-7', 'Oferta 2x1 Pizza 8 Formaggi', '2 Pizzas 8 Formaggi, bebida', '7,90',
        TO_DATE('2022/1/4','yyyy-mm-dd'), TO_DATE('2022/2/4','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos, Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-8', 'Oferta Menú-Toscano', 'Pizza a la Toscana, bebida, postre', '8,80',
        TO_DATE('2022/1/1','yyyy-mm-dd'), TO_DATE('2022/2/10','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos, Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-9', 'Oferta Menú-Veneciano', 'Pizza a la Veneciana e funghi, bebida, fritteli venecianos', '10,80',
        TO_DATE('2022/1/3','yyyy-mm-dd'), TO_DATE('2022/2/15','yyyy-mm-dd'));
        
INSERT INTO OfertaProductos (IdOfertaProd, Nombre_OferProd, ListaProductos, Precio_OferProd, FechaIni_OferProd, FechaFin_OferProd)
VALUES ('OP-10', 'Oferta Menú-Degustación', 'Mini Pizza de la casa con rabbioli, pasta al pomodoro, bebida, postre casero', '8,80',
        TO_DATE('2022/1/7','yyyy-mm-dd'), TO_DATE('2022/1/28','yyyy-mm-dd'));

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-1', 'OP-1');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-1', 'OP-2');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-1', 'OP-3');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-2', 'OP-6');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-2', 'OP-2');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-3', 'OP-4');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-4', 'OP-5');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-4', 'OP-10');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-5', 'OP-2');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-5', 'OP-6');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-5', 'OP-5');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-6', 'OP-7');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-6', 'OP-8');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-6', 'OP-9');

INSERT INTO Promociona (IdCampaña, IdOfertaProd)
VALUES ('CP-6', 'OP-10');

COMMIT; -- para hacer efectivas las inserciones


SELECT * FROM USER_TABLES;
SELECT * FROM CampañaPublicitaria;
SELECT * FROM OfertaProductos;
SELECT * FROM Promociona;
SELECT IdOfertaProd FROM OfertaProductos
MINUS;
SELECT IdOfertaProd FROM Promociona WHERE IdCampaña = 'CP-11';

DELETE FROM OfertaProductos WHERE IdOfertaProd = 'a';
DELETE FROM CAMPAÑAPUBLICITARIA WHERE IDCAMPAÑA = 'CP-2';
DELETE FROM Promociona WHERE IDCAMPAÑA = 'CP-6' AND IDOFERTAPROD ='OP-1';
