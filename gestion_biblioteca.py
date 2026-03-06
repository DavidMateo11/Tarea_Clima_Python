# --- CLASES PRINCIPALES ---

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Se usa una tupla para título y autor (inmutables)
        self.datos_inmutables = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.datos_inmutables[0]} por {self.datos_inmutables[1]} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para gestionar los libros prestados
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        # Diccionario para libros disponibles {isbn: objeto_libro}
        self.libros_disponibles = {}
        # Conjunto para asegurar IDs de usuario únicos
        self.usuarios_ids = set()
        # Diccionario para buscar objetos de usuario por su ID
        self.usuarios_datos = {}

    def añadir_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro añadido: {libro.datos_inmutables[0]}")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            eliminado = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {eliminado.datos_inmutables[0]}")
        else:
            print("El libro no existe.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_ids:
            self.usuarios_ids.add(usuario.id_usuario)
            self.usuarios_datos[usuario.id_usuario] = usuario
            print(f"Usuario {usuario.nombre} registrado.")
        else:
            print("Error: El ID ya está en uso.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_ids and isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            self.usuarios_datos[id_usuario].libros_prestados.append(libro)
            print(f"Préstamo: '{libro.datos_inmutables[0]}' a {self.usuarios_datos[id_usuario].nombre}")
        else:
            print("No se pudo realizar el préstamo.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_datos:
            usuario = self.usuarios_datos[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    print(f"Devolución exitosa: {libro.datos_inmutables[0]}")
                    return
        print("No se encontró el registro del préstamo.")

    def buscar_libro(self, criterio, valor):
        print(f"\nResultados de búsqueda ({criterio}):")
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.datos_inmutables[0].lower():
                print(f" - {libro}")
            elif criterio == "autor" and valor.lower() in libro.datos_inmutables[1].lower():
                print(f" - {libro}")
            elif criterio == "categoria" and valor.lower() == libro.categoria.lower():
                print(f" - {libro}")


# --- PRUEBAS DEL SISTEMA ---
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # 1. Crear libros
    l1 = Libro("Python Avanzado", "M. Lopez", "Tecnología", "97801")
    l2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Cuento", "97802")
    biblioteca.añadir_libro(l1)
    biblioteca.añadir_libro(l2)

    # 2. Registrar usuario
    user = Usuario("Estudiante", "USR100")
    biblioteca.registrar_usuario(user)

    # 3. Operaciones
    biblioteca.prestar_libro("USR100", "97801")
    biblioteca.buscar_libro("categoria", "Cuento")
    biblioteca.devolver_libro("USR100", "97801")