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
    NumSegSocial INT
    Salario DECIMAL,
    FOREIGN KEY (IDOfertaEmpleo) REFERENCES OfertaEmpleo(IDOfertaEmpleo)
);


INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) VALUES(10,'chef', '01/01/21', '01/01/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) VALUES(11,'pinche', '11/01/21', '11/01/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) VALUES(12,'administrador', '15/01/21', '15/01/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) VALUES(13,'encargado', '21/01/21', '21/01/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) VALUES(15,'control de calidad', '02/03/21', '02/03/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) VALUES(16,'camarero', '01/04/21', '01/04/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) VALUES(17,'barman', '21/05/21', '21/05/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) VALUES(18,'proveedor de productos', '14/06/21', '14/06/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) VALUES(19,'nutricionista', '06/07/21', '06/07/22');

INSERT INTO OfertaEmpleo(IdOfertaEmpleo, ListadoEmpleos, FechaIni_OferEmp, FechaFin_OferEmp ) VALUES(20,'camarero', '18/08/21', '18/08/22');

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) VALUES('77391639C', 10, 'Carlos Fernández Castro', 784096793, 1726381901, 2200);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) VALUES('67361439F', 11, 'Tomás Galiana García', 721083092, 1726381901, 1200);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) VALUES('56396123H', 12, 'Alicia Fernández Fernández', 618293018, 1726381901, 2300);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) VALUES('32391617L', 13, 'Carlos González Pérez', 692758223, 1726381901, 2000);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) VALUES('79323639K', 15, 'Lucía Pérez Maraver', 639472783, 1726381901, 1200);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) VALUES('70391935M', 15, 'Carlos García Galiana', 639283749, 1726381901, 1300);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) VALUES('65391174B', 16, 'Tomás Fernández Sáez', 601928354, 1726381901, 2200);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) VALUES('27191630T', 17, 'Gerardo González García', 620988655, 1726381901, 2300);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) VALUES('68391601U', 18, 'Francisco Galiana Martínez', 617264906, 1726381901, 1900);

INSERT INTO Contrato(DNI, IdOfertaEmpleo, Nombre_Empleado, Tlf_Empleado, NumSegSocial, Salario) VALUES('77135672J', 19, 'Laura Fernández García', 695647890, 1726381901, 1500);
