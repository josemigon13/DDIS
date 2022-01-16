-- Disparador para que no se permita que una fecha de inicio de alquiler sea posterior a la de fin --

CREATE OR REPLACE TRIGGER insert_alm
    BEFORE
    INSERT ON Almacen
    FOR EACH ROW
DECLARE
    errorFecha EXCEPTION;
BEGIN
    IF :new.FechaFinAlquiler_Alm < :new.FechaInicioAlquiler_Alm THEN
        RAISE errorFecha;
    END IF;
EXCEPTION
    WHEN errorFecha THEN 
        DBMS_OUTPUT.PUT_LINE('Error en las fechas');
        raise_application_error(-20600, :new.FechaInicioAlquiler_Alm || ' no puede ser posterior a ' || :new.FechaFinAlquiler_Alm);
END;

-- Disparador para que no se permita que una cantidad sea menor o igual que cero o un coste negativo --

CREATE OR REPLACE TRIGGER insert_lote
    BEFORE
    INSERT ON LoteProductosAlmacena
    FOR EACH ROW
DECLARE
    errorCoste EXCEPTION;
    errorCantidad EXCEPTION;
BEGIN
    IF :new.Cantidad <= 0 THEN
        RAISE errorCantidad;
    END IF;

    IF :new.Coste_Lote < 0 THEN
        RAISE errorCoste;
    END IF;
EXCEPTION
    WHEN errorCantidad THEN 
        DBMS_OUTPUT.PUT_LINE('Error en la cantidad');
        raise_application_error(-20600, :new.Cantidad || ' no puede ser menor que 1');
        
    WHEN errorCoste THEN 
        DBMS_OUTPUT.PUT_LINE('Error en el coste');
        raise_application_error(-20600, :new.Coste_Lote || ' no puede ser negativo');
END;

--Método para mostrar la descripción del lote borrado--

CREATE OR REPLACE PROCEDURE lote_borrado(idLote VARCHAR2) AS
	CURSOR lLote IS SELECT * FROM LoteProductosAlmacena;
	registroLote lLote%ROWTYPE;
BEGIN
	OPEN lLote;
	LOOP
    FETCH lLote INTO registroLote;
    EXIT WHEN registroLote.IdLote = idLote;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Se ha borrado el lote de ' || registroLote.Descripcion_Lote);
    CLOSE lLote;
END;

--Método para mostrar la dirección del almacén borrado--

CREATE OR REPLACE PROCEDURE almacen_borrado(idAlmacen VARCHAR2) AS
	CURSOR aAlmacen IS SELECT * FROM Almacen;
	registroAlmacen aAlmacen%ROWTYPE;
BEGIN
	OPEN aAlmacen;
	LOOP
    FETCH aAlmacen INTO registroAlmacen;
    EXIT WHEN registroAlmacen.IdAlmacen = idAlmacen;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Se ha borrado el almacen de la ' || registroAlmacen.Direccion);
    CLOSE aAlmacen;
END;