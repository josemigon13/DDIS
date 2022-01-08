CREATE OR REPLACE TRIGGER campañaMinimoUnaOferta
BEFORE DELETE ON OfertaProductos
FOR EACH ROW
DECLARE
	CURSOR campañas IS SELECT IdCampaña FROM CampañaPublicitaria;
	IdCampañaActual CampañaPublicitaria.IdCampaña%TYPE;
	num_promociones_oferta INTEGER;
    IdInformeAsociadoCamp InformeCampaña.IdInforme%TYPE;
    num_informes_campaña INTEGER;
BEGIN
	OPEN campañas;
	FETCH campañas INTO IdCampañaActual;
    WHILE (campañas%FOUND) LOOP
        SELECT COUNT(*) INTO num_promociones_oferta FROM Promociona WHERE IdCampaña = IdCampañaActual;
        IF (num_promociones_oferta = 0) THEN
            BEGIN
                DBMS_OUTPUT.PUT_LINE(  'Como se elimina la única oferta de productos que la campaña identificada por ' ||
                                        to_char(IdCampañaActual) || ' promociona, se elimina tal campaña, para evitar
                                        tener una campaña sin relación con ninguna oferta.');
    
                SELECT COUNT(*) INTO num_informes_campaña FROM InformeCampaña WHERE IdCampaña = IdCampañaActual;
                IF (num_informes_campaña != 0) THEN
                    BEGIN
                        SELECT IdInforme INTO IdInformeAsociadoCamp FROM InformeCampaña WHERE IdCampaña = IdCampañaActual;
                        DELETE FROM InformeCampaña WHERE IdInforme = IdInformeAsociadoCamp;
                        DELETE FROM InformeCuentas WHERE IdInforme = IdInformeAsociadoCamp;
                    END;
                END IF;
                DELETE FROM CampañaPublicitaria WHERE IdCampaña = IdCampañaActual;
            END;
        END IF;
        FETCH campañas INTO IdCampañaActual;
	END LOOP;
	CLOSE campañas;
EXCEPTION
	WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(  'EXCEPCIÓN: al ejecutar sentencias de SQL en la eliminación
                                de la Oferta de Productos en el DISPARADOR campañaMinimoUnaOferta.');
		IF (campañas%ISOPEN) THEN
			CLOSE campañas;
		END IF;
END;
/

CREATE OR REPLACE TRIGGER fechasPromociona
BEFORE INSERT ON Promociona
FOR EACH ROW
DECLARE
    FechaIni_OferProd DATE;
    FechaFin_OferProd DATE;
    FechaIni_CampPub DATE;
    FechaFin_CampPub DATE;
    e_fechasIncorrectas_promociona EXCEPTION;
    PRAGMA EXCEPTION_INIT (e_fechasIncorrectas_promociona, -20001);
BEGIN
    SELECT FechaIni_CampPub, FechaFin_CampPub INTO FechaIni_CampPub, FechaFin_CampPub 
    FROM CampañaPublicitaria WHERE IdCampaña = :new.IdCampaña;
    SELECT FechaIni_OferProd, FechaFin_OferProd INTO FechaIni_OferProd, FechaFin_OferProd 
    FROM OfertaProductos WHERE IdOfertaProd = :new.IdOfertaProd;
    IF (FechaIni_OferProd > FechaIni_CampPub OR FechaFin_OferProd < FechaFin_CampPub) THEN
        RAISE e_fechasIncorrectas_promociona;
    ELSE
        DBMS_OUTPUT.PUT_LINE('Fechas Correctas en la promoción de la oferta, válida para la duración de la campaña');
    END IF;
EXCEPTION
    WHEN e_fechasIncorrectas_promociona THEN
        DBMS_OUTPUT.PUT_LINE('EXCEPCIÓN: Fechas Incorrectas: el intervalo de fechas de la campaña (' 
        || TO_CHAR(FechaIni_CampPub, 'YYYY/MM/DD') || ' a ' ||  TO_CHAR(FechaFin_CampPub, 'YYYY/MM/DD') 
        || ') debería estar contenido (pero no lo está) en el intervalo de validez de la oferta ('
        || TO_CHAR(FechaIni_OferProd, 'YYYY/MM/DD') || ' a ' || TO_CHAR(FechaFin_OferProd, 'YYYY/MM/DD')
        || ') para no estar promocionando una oferta no canjeable en el período de la campaña.');
        RAISE;
END;
/