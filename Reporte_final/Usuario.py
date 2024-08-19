from conexion import ConexionBd

class Usuarios:
    def __init__(self, nombre, correo, contraseña, rol):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.rol = rol

    def crear(self):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO Usuarios (nombre, correo, contraseña, rol) VALUES (%s, %s, %s, %s)", 
                           (self.nombre, self.correo, self.contraseña, self.rol))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def verificar_credenciales(correo, contraseña):
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM Usuarios WHERE correo = %s AND contraseña = %s", 
                           (correo, contraseña))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al verificar credenciales: {e}")
            return None
        finally:
            cursor.close()
            conexion.close()
