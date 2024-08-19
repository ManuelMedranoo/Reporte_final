import tkinter as tk
from tkinter import messagebox, ttk
from Usuario import Usuarios
from DetallesVentas import DetallesVentas
from Motos import Motos
from Ventas import Ventas
from Proveedores import Proveedores
from conexion import ConexionBd

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Concesionaria de Motos Durango")
        self.geometry("1920x1080")
        self.mostrar_menu_inicio()

    def mostrar_menu_inicio(self):
        tk.Label(self, text="..::Concesionaria de Motos Durango::..", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="Registrarse", command=self.mostrar_registro).pack(pady=10)
        tk.Button(self, text="Iniciar sesión", command=self.mostrar_login).pack(pady=10)
        tk.Button(self, text="Salir del sistema", command=self.quit).pack(pady=10)

    def mostrar_login(self):
        ventana_login = tk.Toplevel(self)
        ventana_login.title("Inicio de sesión")
        ventana_login.geometry("1920x1080")
        tk.Label(ventana_login, text="Correo:").pack(pady=5)
        self.correo_entry = tk.Entry(ventana_login)
        self.correo_entry.pack(pady=5)
        tk.Label(ventana_login, text="Contraseña:").pack(pady=5)
        self.contrasena_entry = tk.Entry(ventana_login, show='*')
        self.contrasena_entry.pack(pady=5)
        tk.Button(ventana_login, text="Iniciar sesión", command=self.login).pack(pady=10)
        tk.Button(ventana_login, text="Regresar", command=ventana_login.destroy).pack(pady=10)

    def login(self):
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()
        usuario = Usuarios.verificar_credenciales(correo, contrasena)
        if usuario:
            if usuario['rol'] == 'empleado':
                self.mostrar_menu_empleado()
            elif usuario['rol'] == 'cliente':
                self.mostrar_menu_cliente()
        else:
            messagebox.showerror("Error", "Credenciales inválidas.")

    def mostrar_registro(self):
        ventana_registro = tk.Toplevel(self)
        ventana_registro.title("Registro de Usuario")
        ventana_registro.geometry("1920x1080")
        tk.Label(ventana_registro, text="Nombre:").pack(pady=5)
        self.nombre_entry = tk.Entry(ventana_registro)
        self.nombre_entry.pack(pady=5)
        tk.Label(ventana_registro, text="Correo:").pack(pady=5)
        self.correo_entry = tk.Entry(ventana_registro)
        self.correo_entry.pack(pady=5)
        tk.Label(ventana_registro, text="Contraseña:").pack(pady=5)
        self.contrasena_entry = tk.Entry(ventana_registro, show='*')
        self.contrasena_entry.pack(pady=5)
        tk.Label(ventana_registro, text="Rol (empleado/cliente):").pack(pady=5)
        self.rol_entry = tk.Entry(ventana_registro)
        self.rol_entry.pack(pady=5)
        tk.Button(ventana_registro, text="Registrar", command=self.registrar_usuario).pack(pady=10)
        tk.Button(ventana_registro, text="Regresar", command=ventana_registro.destroy).pack(pady=10)

    def registrar_usuario(self):
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()
        rol = self.rol_entry.get()
        nuevo_usuario = Usuarios(nombre, correo, contrasena, rol)
        if nuevo_usuario.crear():
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            self.mostrar_menu_inicio()
        else:
            messagebox.showerror("Error", "No se pudo registrar el usuario.")
    
    def mostrar_menu_empleado(self):
        ventana_empleado = tk.Toplevel(self)
        ventana_empleado.title("Menú Empleado")
        ventana_empleado.geometry("1920x1080")
        tk.Label(ventana_empleado, text="Menú Empleado", font=("Arial", 14)).pack(pady=20)
        tk.Button(ventana_empleado, text="Gestión de Motos", command=self.mostrar_menu_motos).pack(pady=10)
        tk.Button(ventana_empleado, text="Gestión de Ventas", command=self.mostrar_menu_ventas).pack(pady=10)
        tk.Button(ventana_empleado, text="Gestión de Detalles de Ventas", command=self.mostrar_menu_detalles_ventas).pack(pady=10)
        tk.Button(ventana_empleado, text="Gestión de Proveedores", command=self.mostrar_menu_proveedores).pack(pady=10)
        tk.Button(ventana_empleado, text="Cerrar sesión", command=ventana_empleado.destroy).pack(pady=10)

    def mostrar_menu_cliente(self):
        ventana_cliente = tk.Toplevel(self)
        ventana_cliente.title("Menú Cliente")
        ventana_cliente.geometry("1920x1080")
        tk.Label(ventana_cliente, text="Menú Cliente", font=("Arial", 14)).pack(pady=20)
        tk.Button(ventana_cliente, text="Ver Motos", command=self.ver_motos).pack(pady=10)
        tk.Button(ventana_cliente, text="Cerrar sesión", command=ventana_cliente.destroy).pack(pady=10)

    def mostrar_menu_motos(self):
        ventana_motos = tk.Toplevel(self)
        ventana_motos.title("Gestión de Motos")
        ventana_motos.geometry("1920x1080")
        tk.Label(ventana_motos, text="Gestión de Motos", font=("Arial", 14)).pack(pady=20)
        tk.Button(ventana_motos, text="Ver Motos", command=self.ver_motos).pack(pady=10)
        tk.Button(ventana_motos, text="Añadir Moto", command=self.anadir_moto).pack(pady=10)
        tk.Button(ventana_motos, text="Actualizar Moto", command=self.actualizar_moto).pack(pady=10)
        tk.Button(ventana_motos, text="Eliminar Moto", command=self.eliminar_moto).pack(pady=10)
        tk.Button(ventana_motos, text="Regresar", command=ventana_motos.destroy).pack(pady=10)

    def mostrar_menu_ventas(self):
        ventana_ventas = tk.Toplevel(self)
        ventana_ventas.title("Gestión de Ventas")
        ventana_ventas.geometry("1920x1080")
        tk.Label(ventana_ventas, text="Gestión de Ventas", font=("Arial", 14)).pack(pady=20)
        tk.Button(ventana_ventas, text="Ver Ventas", command=self.ver_ventas).pack(pady=10)
        tk.Button(ventana_ventas, text="Añadir Venta", command=self.anadir_venta).pack(pady=10)
        tk.Button(ventana_ventas, text="Actualizar Venta", command=self.actualizar_venta).pack(pady=10)
        tk.Button(ventana_ventas, text="Eliminar Venta", command=self.eliminar_venta).pack(pady=10)
        tk.Button(ventana_ventas, text="Regresar", command=ventana_ventas.destroy).pack(pady=10)

    def mostrar_menu_detalles_ventas(self):
        ventana_detalles = tk.Toplevel(self)
        ventana_detalles.title("Gestión de Detalles de Ventas")
        ventana_detalles.geometry("1920x1080")
        tk.Label(ventana_detalles, text="Gestión de Detalles de Ventas", font=("Arial", 14)).pack(pady=20)
        tk.Button(ventana_detalles, text="Ver Detalles de Ventas", command=self.ver_detalles_ventas).pack(pady=10)
        tk.Button(ventana_detalles, text="Añadir Detalle de Venta", command=self.anadir_detalle_venta).pack(pady=10)
        tk.Button(ventana_detalles, text="Actualizar Detalle de Venta", command=self.actualizar_detalle_venta).pack(pady=10)
        tk.Button(ventana_detalles, text="Eliminar Detalle de Venta", command=self.eliminar_detalle_venta).pack(pady=10)
        tk.Button(ventana_detalles, text="Regresar", command=ventana_detalles.destroy).pack(pady=10)

    def mostrar_menu_proveedores(self):
        ventana_proveedores = tk.Toplevel(self)
        ventana_proveedores.title("Gestión de Proveedores")
        ventana_proveedores.geometry("1920x1080")
        tk.Label(ventana_proveedores, text="Gestión de Proveedores", font=("Arial", 14)).pack(pady=20)
        tk.Button(ventana_proveedores, text="Ver Proveedores", command=self.ver_proveedores).pack(pady=10)
        tk.Button(ventana_proveedores, text="Añadir Proveedor", command=self.anadir_proveedor).pack(pady=10)
        tk.Button(ventana_proveedores, text="Actualizar Proveedor", command=self.actualizar_proveedor).pack(pady=10)
        tk.Button(ventana_proveedores, text="Eliminar Proveedor", command=self.eliminar_proveedor).pack(pady=10)
        tk.Button(ventana_proveedores, text="Regresar", command=ventana_proveedores.destroy).pack(pady=10)

    def ver_motos(self):
        ventana_ver_motos = tk.Toplevel(self)
        ventana_ver_motos.title("Ver Motos")
        ventana_ver_motos.geometry("1920x1080")
        tk.Label(ventana_ver_motos, text="Motos disponibles", font=("Arial", 14)).pack(pady=20)
    
    def ver_motos(self):
        ventana_ver_motos = tk.Toplevel(self)
        ventana_ver_motos.title("Ver Motos")
        ventana_ver_motos.geometry("1920x1080")
        tk.Label(ventana_ver_motos, text="Motos disponibles", font=("Arial", 14)).pack(pady=20)
        columnas = ["ID", "Marca", "Modelo", "Año", "Precio"]
        tree = ttk.Treeview(ventana_ver_motos, columns=columnas, show='headings')
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        tree.pack(fill=tk.BOTH, expand=True)
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM producto_moto")
        motos = cursor.fetchall()
        for moto in motos:
            tree.insert("", tk.END, values=moto)
        cursor.close()
        conexion.close()
        
    def anadir_moto(self):
        ventana_anadir_moto = tk.Toplevel(self)
        ventana_anadir_moto.title("Añadir Moto")
        ventana_anadir_moto.geometry("1920x1080")
        tk.Label(ventana_anadir_moto, text="Marca:").pack(pady=5)
        marca_entry = tk.Entry(ventana_anadir_moto)
        marca_entry.pack(pady=5)
        tk.Label(ventana_anadir_moto, text="Modelo:").pack(pady=5)
        modelo_entry = tk.Entry(ventana_anadir_moto)
        modelo_entry.pack(pady=5)
        tk.Label(ventana_anadir_moto, text="Año:").pack(pady=5)
        ano_entry = tk.Entry(ventana_anadir_moto)
        ano_entry.pack(pady=5)
        tk.Label(ventana_anadir_moto, text="Precio:").pack(pady=5)
        precio_entry = tk.Entry(ventana_anadir_moto)
        precio_entry.pack(pady=5)
        
        def guardar_moto():
            marca = marca_entry.get()
            modelo = modelo_entry.get()
            ano = ano_entry.get()
            precio = precio_entry.get()
            conexion = ConexionBd.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO producto_moto (marca, modelo, año, precio) VALUES (%s, %s, %s, %s)",
                        (marca, modelo, ano, precio))
            conexion.commit()
            cursor.close()
            conexion.close()
            ventana_anadir_moto.destroy()
            messagebox.showinfo("Éxito", "Moto añadida correctamente.")

        tk.Button(ventana_anadir_moto, text="Añadir Moto", command=guardar_moto).pack(pady=10)
        tk.Button(ventana_anadir_moto, text="Regresar", command=ventana_anadir_moto.destroy).pack(pady=10)

    def actualizar_moto(self):
        ventana_actualizar_moto = tk.Toplevel(self)
        ventana_actualizar_moto.title("Actualizar Moto")
        ventana_actualizar_moto.geometry("1920x1080")
        tk.Label(ventana_actualizar_moto, text="ID de la Moto a Actualizar:").pack(pady=5)
        id_entry = tk.Entry(ventana_actualizar_moto)
        id_entry.pack(pady=5)
        tk.Label(ventana_actualizar_moto, text="Marca:").pack(pady=5)
        marca_entry = tk.Entry(ventana_actualizar_moto)
        marca_entry.pack(pady=5)
        tk.Label(ventana_actualizar_moto, text="Modelo:").pack(pady=5)
        modelo_entry = tk.Entry(ventana_actualizar_moto)
        modelo_entry.pack(pady=5)
        tk.Label(ventana_actualizar_moto, text="Año:").pack(pady=5)
        ano_entry = tk.Entry(ventana_actualizar_moto)
        ano_entry.pack(pady=5)
        tk.Label(ventana_actualizar_moto, text="Precio:").pack(pady=5)
        precio_entry = tk.Entry(ventana_actualizar_moto)
        precio_entry.pack(pady=5)
        
        def guardar_actualizacion():
            id_moto = id_entry.get()
            marca = marca_entry.get()
            modelo = modelo_entry.get()
            ano = ano_entry.get()
            precio = precio_entry.get()
            conexion = ConexionBd.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("UPDATE producto_moto SET marca = %s, modelo = %s, año = %s, precio = %s WHERE id_moto = %s",
                        (marca, modelo, ano, precio, id_moto))
            conexion.commit()
            cursor.close()
            conexion.close()
            ventana_actualizar_moto.destroy()
            messagebox.showinfo("Éxito", "Moto actualizada correctamente.")

        tk.Button(ventana_actualizar_moto, text="Actualizar Moto", command=guardar_actualizacion).pack(pady=10)
        tk.Button(ventana_actualizar_moto, text="Regresar", command=ventana_actualizar_moto.destroy).pack(pady=10)

    def eliminar_moto(self):
        ventana_eliminar_moto = tk.Toplevel(self)
        ventana_eliminar_moto.title("Eliminar Moto")
        ventana_eliminar_moto.geometry("1920x1080")
        tk.Label(ventana_eliminar_moto, text="ID de la Moto a Eliminar:").pack(pady=5)
        id_entry = tk.Entry(ventana_eliminar_moto)
        id_entry.pack(pady=5)
        
        def eliminar():
            id_moto = id_entry.get()
            conexion = ConexionBd.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM producto_moto WHERE id_moto = %s", (id_moto,))
            conexion.commit()
            cursor.close()
            conexion.close()
            ventana_eliminar_moto.destroy()
            messagebox.showinfo("Éxito", "Moto eliminada correctamente.")

        tk.Button(ventana_eliminar_moto, text="Eliminar Moto", command=eliminar).pack(pady=10)
        tk.Button(ventana_eliminar_moto, text="Regresar", command=ventana_eliminar_moto.destroy).pack(pady=10)

     
    def ver_ventas(self):
        ventana_ver_ventas = tk.Toplevel(self)
        ventana_ver_ventas.title("Ver Ventas")
        ventana_ver_ventas.geometry("1920x1080")
        tk.Label(ventana_ver_ventas, text="Ventas realizadas", font=("Arial", 14)).pack(pady=20)
    def ver_ventas(self):
        ventana_ver_ventas = tk.Toplevel(self)
        ventana_ver_ventas.title("Ver Ventas")
        ventana_ver_ventas.geometry("1920x1080")
        tk.Label(ventana_ver_ventas, text="Ventas realizadas", font=("Arial", 14)).pack(pady=20)
        columnas = ["ID", "Cliente ID", "Empleado ID", "Fecha", "Costo Total"]
        tree = ttk.Treeview(ventana_ver_ventas, columns=columnas, show='headings')
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        tree.pack(fill=tk.BOTH, expand=True)
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM ventas")
        ventas = cursor.fetchall()
        for venta in ventas:
            tree.insert("", tk.END, values=venta)
        cursor.close()
        conexion.close()

    def anadir_venta(self):
        ventana_anadir_venta = tk.Toplevel(self)
        ventana_anadir_venta.title("Añadir Venta")
        ventana_anadir_venta.geometry("1920x1080")
        tk.Label(ventana_anadir_venta, text="Cliente ID:").pack(pady=5)
        cliente_entry = tk.Entry(ventana_anadir_venta)
        cliente_entry.pack(pady=5)
        tk.Label(ventana_anadir_venta, text="Empleado ID:").pack(pady=5)
        empleado_entry = tk.Entry(ventana_anadir_venta)
        empleado_entry.pack(pady=5)
        tk.Label(ventana_anadir_venta, text="Fecha:").pack(pady=5)
        fecha_entry = tk.Entry(ventana_anadir_venta)
        fecha_entry.pack(pady=5)
        tk.Label(ventana_anadir_venta, text="Costo Total:").pack(pady=5)
        costo_entry = tk.Entry(ventana_anadir_venta)
        costo_entry.pack(pady=5)
        
        def guardar_venta():
            cliente_id = cliente_entry.get()
            empleado_id = empleado_entry.get()
            fecha = fecha_entry.get()
            costo_total = costo_entry.get()
            conexion = ConexionBd.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO ventas (clienteid, empleadoid, fechaVenta, costoDVenta) VALUES (%s, %s, %s, %s)",
                        (cliente_id, empleado_id, fecha, costo_total))
            conexion.commit()
            cursor.close()
            conexion.close()
            ventana_anadir_venta.destroy()
            messagebox.showinfo("Éxito", "Venta añadida correctamente.")

        tk.Button(ventana_anadir_venta, text="Añadir Venta", command=guardar_venta).pack(pady=10)
        tk.Button(ventana_anadir_venta, text="Regresar", command=ventana_anadir_venta.destroy).pack(pady=10)

    def actualizar_venta(self):
        ventana_actualizar_venta = tk.Toplevel(self)
        ventana_actualizar_venta.title("Actualizar Venta")
        ventana_actualizar_venta.geometry("1920x1080")
        tk.Label(ventana_actualizar_venta, text="ID de la Venta a Actualizar:").pack(pady=5)
        id_entry = tk.Entry(ventana_actualizar_venta)
        id_entry.pack(pady=5)
        tk.Label(ventana_actualizar_venta, text="Cliente ID:").pack(pady=5)
        cliente_entry = tk.Entry(ventana_actualizar_venta)
        cliente_entry.pack(pady=5)
        tk.Label(ventana_actualizar_venta, text="Empleado ID:").pack(pady=5)
        empleado_entry = tk.Entry(ventana_actualizar_venta)
        empleado_entry.pack(pady=5)
        tk.Label(ventana_actualizar_venta, text="Fecha:").pack(pady=5)
        fecha_entry = tk.Entry(ventana_actualizar_venta)
        fecha_entry.pack(pady=5)
        tk.Label(ventana_actualizar_venta, text="Costo Total:").pack(pady=5)
        costo_entry = tk.Entry(ventana_actualizar_venta)
        costo_entry.pack(pady=5)
        
        def guardar_actualizacion():
            id_venta = id_entry.get()
            cliente_id = cliente_entry.get()
            empleado_id = empleado_entry.get()
            fecha = fecha_entry.get()
            costo_total = costo_entry.get()
            conexion = ConexionBd.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("UPDATE ventas SET clienteid = %s, empleadoid = %s, fechaVenta = %s, costoDVenta = %s WHERE id=%s",
                        (cliente_id, empleado_id, fecha, costo_total, id_venta))
            conexion.commit()
            cursor.close()
            conexion.close()
            ventana_actualizar_venta.destroy()
            messagebox.showinfo("Éxito", "Venta actualizada correctamente.")

        tk.Button(ventana_actualizar_venta, text="Actualizar Venta", command=guardar_actualizacion).pack(pady=10)
        tk.Button(ventana_actualizar_venta, text="Regresar", command=ventana_actualizar_venta.destroy).pack(pady=10)

    def eliminar_venta(self):
        ventana_eliminar_venta = tk.Toplevel(self)
        ventana_eliminar_venta.title("Eliminar Venta")
        ventana_eliminar_venta.geometry("1920x1080")
        tk.Label(ventana_eliminar_venta, text="ID de la Venta a Eliminar:").pack(pady=5)
        id_entry = tk.Entry(ventana_eliminar_venta)
        id_entry.pack(pady=5)
        
        def eliminar():
            id_venta = id_entry.get()
            conexion = ConexionBd.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM ventas WHERE id_venta = %s", (id_venta,))
            conexion.commit()
            cursor.close()
            conexion.close()
            ventana_eliminar_venta.destroy()
            messagebox.showinfo("Éxito", "Venta eliminada correctamente.")

        tk.Button(ventana_eliminar_venta, text="Eliminar Venta", command=eliminar).pack(pady=10)
        tk.Button(ventana_eliminar_venta, text="Regresar", command=ventana_eliminar_venta.destroy).pack(pady=10)

    def ver_detalles_ventas(self):
        ventana_ver_detalles = tk.Toplevel(self)
        ventana_ver_detalles.title("Ver Detalles de Ventas")
        ventana_ver_detalles.geometry("1920x1080")
        tk.Label(ventana_ver_detalles, text="Detalles de ventas", font=("Arial", 14)).pack(pady=20)
    def ver_detalles_ventas(self):
        ventana_ver_detalles = tk.Toplevel(self)
        ventana_ver_detalles.title("Ver Detalles de Ventas")
        ventana_ver_detalles.geometry("1920x1080")
        tk.Label(ventana_ver_detalles, text="Detalles de ventas", font=("Arial", 14)).pack(pady=20)
        columnas = ["ID Venta", "ID Moto", "Cantidad", "Precio Total"]
        tree = ttk.Treeview(ventana_ver_detalles, columns=columnas, show='headings')
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        tree.pack(fill=tk.BOTH, expand=True)
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM detalles_ventas")
        detalles = cursor.fetchall()
        for detalle in detalles:
            tree.insert("", tk.END, values=detalle)
        cursor.close()
        conexion.close()

    def anadir_detalle_venta(self):
        ventana_anadir_detalle = tk.Toplevel(self)
        ventana_anadir_detalle.title("Añadir Detalle de Venta")
        ventana_anadir_detalle.geometry("1920x1080")
        tk.Label(ventana_anadir_detalle, text="ID Venta:").pack(pady=5)
        id_venta_entry = tk.Entry(ventana_anadir_detalle)
        id_venta_entry.pack(pady=5)
        tk.Label(ventana_anadir_detalle, text="ID Moto:").pack(pady=5)
        id_moto_entry = tk.Entry(ventana_anadir_detalle)
        id_moto_entry.pack(pady=5)
        tk.Label(ventana_anadir_detalle, text="Cantidad:").pack(pady=5)
        cantidad_entry = tk.Entry(ventana_anadir_detalle)
        cantidad_entry.pack(pady=5)
        tk.Label(ventana_anadir_detalle, text="Precio Total:").pack(pady=5)
        precio_total_entry = tk.Entry(ventana_anadir_detalle)
        precio_total_entry.pack(pady=5)
        
        def guardar_detalle():
            id_venta = id_venta_entry.get()
            id_moto = id_moto_entry.get()
            cantidad = cantidad_entry.get()
            precio_total = precio_total_entry.get()
            conexion = ConexionBd.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO detalles_ventas (ventaid, motoid, cantidad, preciototal) VALUES (%s, %s, %s, %s)",
                        (id_venta, id_moto, cantidad, precio_total))
            conexion.commit()
            cursor.close()
            conexion.close()
            ventana_anadir_detalle.destroy()
            messagebox.showinfo("Éxito", "Detalle de venta añadido correctamente.")

        tk.Button(ventana_anadir_detalle, text="Añadir Detalle", command=guardar_detalle).pack(pady=10)
        tk.Button(ventana_anadir_detalle, text="Regresar", command=ventana_anadir_detalle.destroy).pack(pady=10)

    def actualizar_detalle_venta(self):
        ventana_actualizar_detalle = tk.Toplevel(self)
        ventana_actualizar_detalle.title("Actualizar Detalle de Venta")
        ventana_actualizar_detalle.geometry("1920x1080")
        tk.Label(ventana_actualizar_detalle, text="ID del Detalle a Actualizar:").pack(pady=5)
        id_detalle_entry = tk.Entry(ventana_actualizar_detalle)
        id_detalle_entry.pack(pady=5)
        tk.Label(ventana_actualizar_detalle, text="ID Venta:").pack(pady=5)
        id_venta_entry = tk.Entry(ventana_actualizar_detalle)
        id_venta_entry.pack(pady=5)
        tk.Label(ventana_actualizar_detalle, text="ID Moto:").pack(pady=5)
        id_moto_entry = tk.Entry(ventana_actualizar_detalle)
        id_moto_entry.pack(pady=5)
        tk.Label(ventana_actualizar_detalle, text="Cantidad:").pack(pady=5)
        cantidad_entry = tk.Entry(ventana_actualizar_detalle)
        cantidad_entry.pack(pady=5)
        tk.Label(ventana_actualizar_detalle, text="Precio Total:").pack(pady=5)
        precio_total_entry = tk.Entry(ventana_actualizar_detalle)
        precio_total_entry.pack(pady=5)
        
        def guardar_actualizacion():
            id_detalle = id_detalle_entry.get()
            id_venta = id_venta_entry.get()
            id_moto = id_moto_entry.get()
            cantidad = cantidad_entry.get()
            precio_total = precio_total_entry.get()
            conexion = ConexionBd.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("UPDATE detalles_ventas SET ventaid = %s, motoid = %s, cantidad = %s, preciototal = %s WHERE id_venta = %s",
                        (id_venta, id_moto, cantidad, precio_total, id_detalle))
            conexion.commit()
            cursor.close()
            conexion.close()
            ventana_actualizar_detalle.destroy()
            messagebox.showinfo("Éxito", "Detalle de venta actualizado correctamente.")

        tk.Button(ventana_actualizar_detalle, text="Actualizar Detalle", command=guardar_actualizacion).pack(pady=10)
        tk.Button(ventana_actualizar_detalle, text="Regresar", command=ventana_actualizar_detalle.destroy).pack(pady=10)

    def eliminar_detalle_venta(self):
        ventana_eliminar_detalle = tk.Toplevel(self)
        ventana_eliminar_detalle.title("Eliminar Detalle de Venta")
        ventana_eliminar_detalle.geometry("1920x1080")
        tk.Label(ventana_eliminar_detalle, text="ID del Detalle a Eliminar:").pack(pady=5)
        id_detalle_entry = tk.Entry(ventana_eliminar_detalle)
        id_detalle_entry.pack(pady=5)
        
        def eliminar():
            id_detalle = id_detalle_entry.get()
            conexion = ConexionBd.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM detalles_ventas WHERE id_detalle = %s", (id_detalle,))
            conexion.commit()
            cursor.close()
            conexion.close()
            ventana_eliminar_detalle.destroy()
            messagebox.showinfo("Éxito", "Detalle de venta eliminado correctamente.")

        tk.Button(ventana_eliminar_detalle, text="Eliminar Detalle", command=eliminar).pack(pady=10)
        tk.Button(ventana_eliminar_detalle, text="Regresar", command=ventana_eliminar_detalle.destroy).pack(pady=10)


    def ver_proveedores(self):
        ventana_ver_proveedores = tk.Toplevel(self)
        ventana_ver_proveedores.title("Ver Proveedores")
        ventana_ver_proveedores.geometry("1920x1080")
        tk.Label(ventana_ver_proveedores, text="Proveedores disponibles", font=("Arial", 14)).pack(pady=20)
    def ver_proveedores(self):
        ventana_ver_proveedores = tk.Toplevel(self)
        ventana_ver_proveedores.title("Ver Proveedores")
        ventana_ver_proveedores.geometry("1920x1080")
        tk.Label(ventana_ver_proveedores, text="Proveedores disponibles", font=("Arial", 14)).pack(pady=20)
        columnas = ["ID", "Nombre Compañía", "Nombre", "Correo", "Teléfono", "Ciudad"]
        tree = ttk.Treeview(ventana_ver_proveedores, columns=columnas, show='headings')
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        tree.pack(fill=tk.BOTH, expand=True)
        conexion = ConexionBd.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM proveedores")
        proveedores = cursor.fetchall()
        for proveedor in proveedores:
            tree.insert("", tk.END, values=proveedor)
        cursor.close()
        conexion.close()

    def anadir_proveedor(self):
        ventana_anadir_proveedor = tk.Toplevel(self)
        ventana_anadir_proveedor.title("Añadir Proveedor")
        ventana_anadir_proveedor.geometry("1920x1080")
        tk.Label(ventana_anadir_proveedor, text="Nombre Compañía:").pack(pady=5)
        nombre_compania_entry = tk.Entry(ventana_anadir_proveedor)
        nombre_compania_entry.pack(pady=5)
        tk.Label(ventana_anadir_proveedor, text="Nombre:").pack(pady=5)
        nombre_entry = tk.Entry(ventana_anadir_proveedor)
        nombre_entry.pack(pady=5)
        tk.Label(ventana_anadir_proveedor, text="Correo:").pack(pady=5)
        correo_entry = tk.Entry(ventana_anadir_proveedor)
        correo_entry.pack(pady=5)
        tk.Label(ventana_anadir_proveedor, text="Teléfono:").pack(pady=5)
        telefono_entry = tk.Entry(ventana_anadir_proveedor)
        telefono_entry.pack(pady=5)
        tk.Label(ventana_anadir_proveedor, text="Ciudad:").pack(pady=5)
        ciudad_entry = tk.Entry(ventana_anadir_proveedor)
        ciudad_entry.pack(pady=5)
        
        def guardar_proveedor():
            nombre_compania = nombre_compania_entry.get()
            nombre = nombre_entry.get()
            correo = correo_entry.get()
            telefono = telefono_entry.get()
            ciudad = ciudad_entry.get()
            conexion = ConexionBd.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO proveedores (nombre_compania, nombre, correo, telefono, ciudad) VALUES (%s, %s, %s, %s, %s)",
                        (nombre_compania, nombre, correo, telefono, ciudad))
            conexion.commit()
            cursor.close()
            conexion.close()
            ventana_anadir_proveedor.destroy()
            messagebox.showinfo("Éxito", "Proveedor añadido correctamente.")

        tk.Button(ventana_anadir_proveedor, text="Añadir Proveedor", command=guardar_proveedor).pack(pady=10)
        tk.Button(ventana_anadir_proveedor, text="Regresar", command=ventana_anadir_proveedor.destroy).pack(pady=10)

    def actualizar_proveedor(self):
        ventana_actualizar_proveedor = tk.Toplevel(self)
        ventana_actualizar_proveedor.title("Actualizar Proveedor")
        ventana_actualizar_proveedor.geometry("1920x1080")
        tk.Label(ventana_actualizar_proveedor, text="ID del Proveedor a Actualizar:").pack(pady=5)
        id_entry = tk.Entry(ventana_actualizar_proveedor)
        id_entry.pack(pady=5)
        tk.Label(ventana_actualizar_proveedor, text="Nombre Compañía:").pack(pady=5)
        nombre_compania_entry = tk.Entry(ventana_actualizar_proveedor)
        nombre_compania_entry.pack(pady=5)
        tk.Label(ventana_actualizar_proveedor, text="Nombre:").pack(pady=5)
        nombre_entry = tk.Entry(ventana_actualizar_proveedor)
        nombre_entry.pack(pady=5)
        tk.Label(ventana_actualizar_proveedor, text="Correo:").pack(pady=5)
        correo_entry = tk.Entry(ventana_actualizar_proveedor)
        correo_entry.pack(pady=5)
        tk.Label(ventana_actualizar_proveedor, text="Teléfono:").pack(pady=5)
        telefono_entry = tk.Entry(ventana_actualizar_proveedor)
        telefono_entry.pack(pady=5)
        tk.Label(ventana_actualizar_proveedor, text="Ciudad:").pack(pady=5)
        ciudad_entry = tk.Entry(ventana_actualizar_proveedor)
        ciudad_entry.pack(pady=5)
        
        def guardar_actualizacion():
            id_proveedor = id_entry.get()
            nombre_compania = nombre_compania_entry.get()
            nombre = nombre_entry.get()
            correo = correo_entry.get()
            telefono = telefono_entry.get()
            ciudad = ciudad_entry.get()
            conexion = ConexionBd.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("UPDATE proveedores SET nombre_compania = %s, nombre = %s, correo = %s, telefono = %s, ciudad = %s WHERE id_proveedor = %s",
                        (nombre_compania, nombre, correo, telefono, ciudad, id_proveedor))
            conexion.commit()
            cursor.close()
            conexion.close()
            ventana_actualizar_proveedor.destroy()
            messagebox.showinfo("Éxito", "Proveedor actualizado correctamente.")

        tk.Button(ventana_actualizar_proveedor, text="Actualizar Proveedor", command=guardar_actualizacion).pack(pady=10)
        tk.Button(ventana_actualizar_proveedor, text="Regresar", command=ventana_actualizar_proveedor.destroy).pack(pady=10)

    def eliminar_proveedor(self):
        ventana_eliminar_proveedor = tk.Toplevel(self)
        ventana_eliminar_proveedor.title("Eliminar Proveedor")
        ventana_eliminar_proveedor.geometry("1920x1080")
        tk.Label(ventana_eliminar_proveedor, text="ID del Proveedor a Eliminar:").pack(pady=5)
        id_entry = tk.Entry(ventana_eliminar_proveedor)
        id_entry.pack(pady=5)
        
        def eliminar():
            id_proveedor = id_entry.get()
            conexion = ConexionBd.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM proveedores WHERE id_proveedor = %s", (id_proveedor,))
            conexion.commit()
            cursor.close()
            conexion.close()
            ventana_eliminar_proveedor.destroy()
            messagebox.showinfo("Éxito", "Proveedor eliminado correctamente.")

        tk.Button(ventana_eliminar_proveedor, text="Eliminar Proveedor", command=eliminar).pack(pady=10)
        tk.Button(ventana_eliminar_proveedor, text="Regresar", command=ventana_eliminar_proveedor.destroy).pack(pady=10)

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
