CREATE TABLE InformeCuentas(
    IdInforme INT NOT NULL,
    Fecha_Informe DATE NOT NULL,
    PRIMARY KEY(IdInforme)
);

CREATE TABLE InformeCampaña(
    IdInforme INT NOT NULL,
    IdCampaña VARCHAR2(10) NOT NULL,
    FOREIGN KEY (IdInforme) REFERENCES InformeCuentas(IdInforme),
    FOREIGN KEY (IdCampaña) REFERENCES CampañaPublicitaria(IdCampaña)
);

CREATE TABLE InformeSalarialEmpleado(
   IdInforme INT NOT NULL,
    DNI VARCHAR2(10) NOT NULL,
    FOREIGN KEY (IdInforme) REFERENCES InformeCuentas(IdInforme),
    FOREIGN KEY (DNI) REFERENCES Contrato(DNI)
);

CREATE TABLE InformeProveedor(
    IdInforme INT NOT NULL,
    NumProveedor INT NOT NULL,
    FOREIGN KEY (IdInforme) REFERENCES InformeCuentas(IdInforme),
    FOREIGN KEY (NumProveedor) REFERENCES Proveedor(NumProveedor)
);

CREATE TABLE InformeTributario(
    IdInforme INT NOT NULL,
    ImporteTributario FLOAT NOT NULL,
    FOREIGN KEY (IdInforme) REFERENCES InformeCuentas(IdInforme)
);

CREATE TABLE InformePOS(
    IdInforme INT NOT NULL,
    BeneficiosPOS FLOAT NOT NULL,
    FOREIGN KEY (IdInforme) REFERENCES InformeCuentas(IdInforme)
);

COMMIT; -- para hacer efectivas las inserciones