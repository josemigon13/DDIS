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

-- Inserción de tuplas para un informe salarial de empleado

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(1,'01/01/22');
INSERT INTO InformeSalarialEmpleado(IdInforme, DNI) VALUES(1,'12345678X');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(2,'01/02/22');
INSERT INTO InformeSalarialEmpleado(IdInforme, DNI) VALUES(2,'12345678X');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(3,'01/01/22');
INSERT INTO InformeSalarialEmpleado(IdInforme, DNI) VALUES(3,'12345678Y');

-- Inserción de tuplas para un informe de proveedor

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(4,'01/01/22');
INSERT INTO InformeProveedor(IdInforme, NumProveedor) VALUES(4,1);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(5,'01/02/22');
INSERT INTO InformeProveedor(IdInforme, NumProveedor) VALUES(5,1);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(6,'01/01/22');
INSERT INTO InformeProveedor(IdInforme, NumProveedor) VALUES(6,2);

-- Inserción de tuplas para un informe de campaña publicitaria

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(7,'01/01/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(7, 'CP-1');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(8,'01/01/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(8, 'CP-2');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(9,'01/02/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(9, 'CP-3');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(10,'01/03/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(10, 'CP-4');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(11,'01/03/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(11, 'CP-5');

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(12,'01/04/22');
INSERT INTO InformeCampaña(IdInforme, IdCampaña) VALUES(12, 'CP-6');

-- Inserción de tuplas para un informe tributario

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(13,'01/01/22');
INSERT INTO InformeTributario(IdInforme, ImporteTributario) VALUES(13, 79000.00);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(14,'01/02/22');
INSERT INTO InformeTributario(IdInforme, ImporteTributario) VALUES(14, 93000.00);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(15,'01/03/22');
INSERT INTO InformeTributario(IdInforme, ImporteTributario) VALUES(15, 125000.00);

-- Inserción de tuplas para un informe de punto de venta

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(16,'01/03/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(16, 1599.00, 1);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(17,'01/01/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(17, 2199.00, 1);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(18,'01/02/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(18, 1999.00, 2);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(19,'01/03/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(19, 2739.00, 3);

INSERT INTO InformeCuentas(IdInforme, Fecha_Informe) VALUES(20,'01/05/22');
INSERT INTO InformePOS(IdInforme, BeneficiosPOS, CodigoPOS) VALUES(20, 2739.00, 4);

COMMIT; -- para hacer efectivas las inserciones