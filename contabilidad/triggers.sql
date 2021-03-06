-- Disparador para que no se permita que un informe disponga de un identificador entero menor que uno
-- No se añadirá como funcionalidad a la aplicación puesto que controla un aspecto ya dirimido en
-- la misma

CREATE OR REPLACE TRIGGER IdInforme
    BEFORE
    INSERT ON InformeCuentas
    FOR EACH ROW
DECLARE
    errIdInforme EXCEPTION;
BEGIN
    IF :new.IdInforme<1 THEN
        RAISE errIdInforme;
    END IF;
EXCEPTION
    WHEN errIdInforme THEN 
        DBMS_OUTPUT.PUT_LINE('ERROR: Identificador de informe no válido');
        raise_application_error(-20600, :new.IdInforme || ' es menor que uno');
END;

-- Procedimientos para mostrar las descripciones de los informes insertados --

CREATE OR REPLACE PROCEDURE inf_salarial(IdInforme INTEGER) AS
	CURSOR cInforme IS SELECT * FROM InformeCuentas;
    CURSOR cInformeEmpleado IS SELECT * FROM InformeSalarialEmpleado;
	Inf_cuentas cInforme%ROWTYPE;
    Inf_empleado cInformeEmpleado%ROWTYPE;
BEGIN
	OPEN cInforme;
	LOOP
    FETCH cInforme INTO Inf_cuentas;
    EXIT WHEN Inf_cuentas.IdInforme = IdInforme;
    END LOOP;
    OPEN cInformeEmpleado;
    LOOP
    FETCH cInformeEmpleado INTO Inf_empleado;
    EXIT WHEN Inf_empleado.IdInforme = IdInforme;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Nuevo informe salarial insertado: { IdInforme:' || IdInforme ||
    ',  DNI:' || Inf_empleado.DNI || ', Fecha_Informe:' || Inf_cuentas.Fecha_Informe || ' }');
    CLOSE cInformeEmpleado;
    CLOSE cInforme;
END;

CREATE OR REPLACE PROCEDURE inf_proveedor(IdInforme INTEGER) AS
	CURSOR cInforme IS SELECT * FROM InformeCuentas;
    CURSOR cInformeProveedor IS SELECT * FROM InformeProveedor;
	Inf_cuentas cInforme%ROWTYPE;
    Inf_pro cInformeProveedor%ROWTYPE;
BEGIN
	OPEN cInforme;
	LOOP
    FETCH cInforme INTO Inf_cuentas;
    EXIT WHEN Inf_cuentas.IdInforme = IdInforme;
    END LOOP;
    OPEN cInformeProveedor;
    LOOP
    FETCH cInformeProveedor INTO Inf_pro;
    EXIT WHEN Inf_pro.IdInforme = IdInforme;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Nuevo informe de proveedor insertado: { IdInforme:' || IdInforme ||
    ', NumProveedor:' || Inf_pro.NumProveedor || ', Fecha_Informe:' || Inf_cuentas.Fecha_Informe || ' }');
    CLOSE cInformeProveedor;
    CLOSE cInforme;
END;

CREATE OR REPLACE PROCEDURE inf_campaña(IdInforme INTEGER) AS
	CURSOR cInforme IS SELECT * FROM InformeCuentas;
    CURSOR cInformeCampaña IS SELECT * FROM InformeCampaña;
	Inf_cuentas cInforme%ROWTYPE;
    Inf_Campaña cInformeCampaña%ROWTYPE;
BEGIN
	OPEN cInforme;
	LOOP
    FETCH cInforme INTO Inf_cuentas;
    EXIT WHEN Inf_cuentas.IdInforme = IdInforme;
    END LOOP;
    OPEN cInformeCampaña;
    LOOP
    FETCH cInformeCampaña INTO Inf_Campaña;
    EXIT WHEN Inf_Campaña.IdInforme = IdInforme;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Nuevo informe de campaña insertado: { IdInforme:' || IdInforme ||
    ', IdCampaña:' || Inf_Campaña.IdCampaña || ', Fecha_Informe:' || Inf_cuentas.Fecha_Informe || ' }');
    CLOSE cInformeCampaña;
    CLOSE cInforme;
END;

CREATE OR REPLACE PROCEDURE inf_pos(IdInforme INTEGER) AS
	CURSOR cInforme IS SELECT * FROM InformeCuentas;
    CURSOR cInformePOS IS SELECT * FROM InformePOS;
	Inf_cuentas cInforme%ROWTYPE;
    Inf_POS cInformePOS%ROWTYPE;
BEGIN
	OPEN cInforme;
	LOOP
    FETCH cInforme INTO Inf_cuentas;
    EXIT WHEN Inf_cuentas.IdInforme = IdInforme;
    END LOOP;
    OPEN cInformePOS;
    LOOP
    FETCH cInformePOS INTO Inf_POS;
    EXIT WHEN Inf_POS.IdInforme = IdInforme;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Nuevo informe POS insertado: { IdInforme:' || IdInforme ||
    ', CodigoPOS:' || Inf_POS.CodigoPOS || ', BeneficiosPOS:' || Inf_POS.BeneficiosPOS || 
    ', Fecha_Informe:' || Inf_cuentas.Fecha_Informe || ' }');
    CLOSE cInformePOS;
    CLOSE cInforme;
END;

CREATE OR REPLACE PROCEDURE inf_TRIB(IdInforme INTEGER) AS
	CURSOR cInforme IS SELECT * FROM InformeCuentas;
    CURSOR cInformeTRIB IS SELECT * FROM InformeTributario;
	Inf_cuentas cInforme%ROWTYPE;
    Inf_TRIB cInformeTRIB%ROWTYPE;
BEGIN
	OPEN cInforme;
	LOOP
    FETCH cInforme INTO Inf_cuentas;
    EXIT WHEN Inf_cuentas.IdInforme = IdInforme;
    END LOOP;
    OPEN cInformeTRIB;
    LOOP
    FETCH cInformeTRIB INTO Inf_TRIB;
    EXIT WHEN Inf_TRIB.IdInforme = IdInforme;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Nuevo informe tributario insertado: { IdInforme:' || IdInforme || 
    ',  ImporteTributario:' || Inf_TRIB.ImporteTributario || ', Fecha_Informe:' || Inf_cuentas.Fecha_Informe || ' }');
    CLOSE cInformeTRIB;
    CLOSE cInforme;
END;