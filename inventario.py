import os
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga datos al iniciar (Requisito 2) y maneja errores (Requisito 3)."""
        try:
            if not os.path.exists(self.archivo):
                with open(self.archivo, 'w') as f: pass
                return
            with open(self.archivo, 'r') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) == 4:
                        id_p, nom, cant, prec = partes
                        self.productos[id_p] = Producto(id_p, nom, int(cant), float(prec))
            print(">>> ÉXITO: Inventario cargado correctamente.")
        except (FileNotFoundError, PermissionError) as e:
            print(f">>> ERROR al leer archivo: {e}")

    def guardar_en_archivo(self):
        """Guarda los cambios en el archivo .txt (Requisito 1)."""
        try:
            with open(self.archivo, 'w') as f:
                for p in self.productos.values():
                    f.write(str(p) + "\n")
            return True
        except PermissionError:
            print(">>> ERROR: No tienes permisos para escribir en el archivo.")
            return False

    def añadir_producto(self, producto):
        self.productos[producto.id_producto] = producto
        if self.guardar_en_archivo():
            print(f">>> ÉXITO: {producto.nombre} guardado en el archivo.")

    def mostrar_todo(self):
        if not self.productos:
            print("El inventario está vacío.")
        for p in self.productos.values():
            print(f"ID: {p.id_producto} | Nombre: {p.nombre} | Stock: {p.cantidad} | Precio: ${p.precio}")