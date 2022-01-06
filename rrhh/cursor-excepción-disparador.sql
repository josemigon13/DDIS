CREATE OR REPLACE TRIGGER salarioMinimo
    BEFORE
    INSERT ON contrato
    FOR EACH ROW
DECLARE
    errSalario EXCEPTION;
BEGIN
    IF :new.Salario<965 THEN
        RAISE errSalario;
    END IF;
EXCEPTION
    WHEN errSalario THEN 
        DBMS_OUTPUT.PUT_LINE(' El salario debe ser superior a 965 euros, ya que es el salario minimo');
        raise_application_error(-20600, :new.IdInforme || ' Salario no válido');
END;


CREATE OR REPLACE PROCEDURE DNI_contrato(DNI VARCHAR2) AS
	CURSOR mostrar_Contrato IS SELECT * FROM Contrato;
	info_contrato mostrar_Contrato%ROWTYPE;
BEGIN
		OPEN mostrar_Contrato;
		LOOP
    FETCH mostrar_Contrato INTO info_contrato;
    EXIT WHEN info_contrato.DNI = DNI;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Nuevo contrato insertado: { DNI:' || DNI ||
    ',  Nombre del empleado:' || info_contrato.Nombre_Empleado || ', Id de la oferta de empleo:' || info_contrato.IDOfertaEmpleo || ' }');
    CLOSE mostrar_Contrato;
END

CREATE OR REPLACE PROCEDURE IDOfertaEmpleo_OfertaEmpleo(IDOfertaEmpleo VARCHAR2) AS
	CURSOR mostrar_OfertaEmpleo IS SELECT * FROM OfertaEmpleo;
	info_ofertaEmpleo mostrar_OfertaEmpleo%ROWTYPE;
BEGIN
		OPEN mostrar_OfertaEmpleo;
		LOOP
    FETCH mostrar_OfertaEmpleo INTO info_ofertaEmpleo;
    EXIT WHEN info_ofertaEmpleo.IDOfertaEmpleo = IDOfertaEmpleo;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Nueva oferta de empleo insertada: { IDOfertEmpleo:' || IDOfertaEmpleo ||
    ',  Listado de empleos ofertados:' || info_ofertaEmpleo.ListadoEmpleos || ' }');
    CLOSE mostrar_OfertaEmpleo;
END;
