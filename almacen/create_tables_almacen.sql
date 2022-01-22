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

--Cambiar en el doc la superficie a float--
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

COMMIT;