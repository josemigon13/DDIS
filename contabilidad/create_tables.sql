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