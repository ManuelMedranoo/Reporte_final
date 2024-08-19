from conexion import ConexionBd

class Proveedores:
    def __init__(self, nombre_compania, nombre, correo, telefono, ciudad, id_proveedor=None):
        self.id_proveedor = id_proveedor
        self.nombre_compania = nombre_compania
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.ciudad = ciudad

    def crear(self):
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor()
            query = "INSERT INTO proveedores (nombre_compania, nombre, correo, telefono, ciudad) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (self.nombre_compania, self.nombre, self.correo, self.telefono, self.ciudad))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error al crear proveedor: {e}")
            return False

    def actualizar(self):
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor()
            query = "UPDATE proveedores SET nombre_compania=%s, nombre=%s, correo=%s, telefono=%s, ciudad=%s WHERE id_proveedor=%s"
            cursor.execute(query, (self.nombre_compania, self.nombre, self.correo, self.telefono, self.ciudad, self.id_proveedor))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error al actualizar proveedor: {e}")
            return False

    @staticmethod
    def eliminar(id_proveedor):
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor()
            query = "DELETE FROM proveedores WHERE id_proveedor=%s"
            cursor.execute(query, (id_proveedor,))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Error al eliminar proveedor: {e}")
            return False

    @staticmethod
    def obtener_todos():
        try:
            connection = ConexionBd.obtener_conexion()
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM proveedores"
            cursor.execute(query)
            proveedores = cursor.fetchall()
            cursor.close()
            connection.close()
            return proveedores
        except Exception as e:
            print(f"Error al obtener proveedores: {e}")
            return []
