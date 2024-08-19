from conexion import ConexionBd

class Motos:
    def __init__(self, marca, modelo, año, precio, proveedorid, id_moto=None):
        self.id_moto = id_moto
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.proveedorid = proveedorid

    def crear(self):
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor()
            query = "INSERT INTO motos (marca, modelo, año, precio, proveedorid) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (self.marca, self.modelo, self.año, self.precio, self.proveedorid))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error al crear moto: {e}")
            return False

    def actualizar(self):
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor()
            query = "UPDATE motos SET marca=%s, modelo=%s, año=%s, precio=%s, proveedorid=%s WHERE id_moto=%s"
            cursor.execute(query, (self.marca, self.modelo, self.año, self.precio, self.proveedorid, self.id_moto))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error al actualizar moto: {e}")
            return False

    @staticmethod
    def eliminar(id_moto):
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor()
            query = "DELETE FROM motos WHERE id_moto=%s"
            cursor.execute(query, (id_moto,))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error al eliminar moto: {e}")
            return False

    @staticmethod
    def obtener_todas():
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM motos"
            cursor.execute(query)
            motos = cursor.fetchall()
            cursor.close()
            connection.close()
            return motos
        except Exception as e:
            print(f"Error al obtener motos: {e}")
            return []
