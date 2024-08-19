from conexion import ConexionBd

class DetallesVentas:
    def __init__(self, ventaid, motoid, cantidad, preciototal, id_detalle=None):
        self.id_detalle = id_detalle
        self.ventaid = ventaid
        self.motoid = motoid
        self.cantidad = cantidad
        self.preciototal = preciototal

    def crear(self):
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor()
            query = "INSERT INTO detalles_ventas (ventaid, motoid, cantidad, preciototal) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.ventaid, self.motoid, self.cantidad, self.preciototal))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error al crear detalle de venta: {e}")
            return False

    def actualizar(self):
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor()
            query = "UPDATE detalles_ventas SET ventaid=%s, motoid=%s, cantidad=%s, preciototal=%s WHERE id_detalle=%s"
            cursor.execute(query, (self.ventaid, self.motoid, self.cantidad, self.preciototal, self.id_detalle))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error al actualizar detalle de venta: {e}")
            return False

    @staticmethod
    def eliminar(id_detalle):
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor()
            query = "DELETE FROM detalles_ventas WHERE id_detalle=%s"
            cursor.execute(query, (id_detalle,))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error al eliminar detalle de venta: {e}")
            return False

    @staticmethod
    def obtener_todos():
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM detalles_ventas"
            cursor.execute(query)
            detalles = cursor.fetchall()
            cursor.close()
            connection.close()
            return detalles
        except Exception as e:
            print(f"Error al obtener detalles de ventas: {e}")
            return []
