-- Método para mostrar los artículos del pedido borrado
CREATE OR REPLACE PROCEDURE pedido_borrado(numPedido INT) AS
	CURSOR cPedido IS SELECT * FROM Pedido;
	registroPedido cPedido%ROWTYPE;
BEGIN
	OPEN cPedido;
	LOOP
    FETCH cPedido INTO registroPedido;
    EXIT WHEN registroPedido.NumPedido = numPedido;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Se ha borrado el pedido ' || registroPedido.NumPedido 
                            || ' con los artículos ' || registroPedido.Articulos);
    CLOSE cPedido;
END;