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
