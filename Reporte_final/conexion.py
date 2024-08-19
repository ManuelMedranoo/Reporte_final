import mysql.connector

class ConexionBd:
    @staticmethod
    def obtener_conexion():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  
            database='CatalagoMotosvf'
        )
