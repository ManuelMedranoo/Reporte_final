from conexion import ConexionBd

class Ventas:
    def __init__(self, clienteid, empleadoid, fechaVenta, costoDVenta, id_venta=None):
        self.id_venta = id_venta
        self.clienteid = clienteid
        self.empleadoid = empleadoid
        self.fechaVenta = fechaVenta
        self.costoDVenta = costoDVenta

    def crear(self):
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor()
            query = "INSERT INTO ventas (clienteid, empleadoid, fechaVenta, costoDVenta) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.clienteid, self.empleadoid, self.fechaVenta, self.costoDVenta))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error al crear venta: {e}")
            return False

    def actualizar(self):
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor()
            query = "UPDATE ventas SET clienteid=%s, empleadoid=%s, fechaVenta=%s, costoDVenta=%s WHERE id_venta=%s"
            cursor.execute(query, (self.clienteid, self.empleadoid, self.fechaVenta, self.costoDVenta, self.id_venta))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error al actualizar venta: {e}")
            return False

    @staticmethod
    def eliminar(id_venta):
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor()
            query = "DELETE FROM ventas WHERE id_venta=%s"
            cursor.execute(query, (id_venta,))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error al eliminar venta: {e}")
            return False

    @staticmethod
    def obtener_todas():
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM ventas"
            cursor.execute(query)
            ventas = cursor.fetchall()
            cursor.close()
            connection.close()
            return ventas
        except Exception as e:
            print(f"Error al obtener ventas: {e}")
            return []
