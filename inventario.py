import json
import os
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}  # Colección solicitada (Diccionario)
        self.cargar_desde_archivo() # Carga automática al iniciar

    def añadir(self, p):
        if p.get_id() not in self.productos:
            self.productos[p.get_id()] = p
            self.guardar_en_archivo()
            print("Añadido con éxito.")
        else:
            print("Error: El ID ya existe.")

    def eliminar(self, id_p):
        if id_p in self.productos:
            del self.productos[id_p]
            self.guardar_en_archivo()
            print("Eliminado.")
        else:
            print("No se encontró el producto.")

    # NUEVO: Método para actualizar cantidad o precio
    def actualizar(self, id_p, cantidad=None, precio=None):
        if id_p in self.productos:
            if cantidad is not None:
                self.productos[id_p].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_p].set_precio(precio)
            self.guardar_en_archivo()
            print("Producto actualizado.")
        else:
            print("Error: Producto no encontrado.")

    # NUEVO: Búsqueda por nombre
    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron coincidencias.")

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos.values():
                print(p)

    def guardar_en_archivo(self):
        # Serialización a JSON
        with open(self.archivo, 'w') as f:
            datos = {k: vars(v) for k, v in self.productos.items()}
            json.dump(datos, f, indent=4)

    # NUEVO: Cargar datos desde el archivo al iniciar
    def cargar_desde_archivo(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as f:
                    datos = json.load(f)
                    for d in datos.values():
                        # Creamos objetos Producto a partir del diccionario cargado
                        p = Producto(d['id_producto'], d['nombre'], d['cantidad'], d['precio'])
                        self.productos[p.get_id()] = p
            except (json.JSONDecodeError, FileNotFoundError):
                print("Iniciando inventario nuevo (archivo vacío o no encontrado).")