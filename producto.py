class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Formato para guardar en el archivo .txt
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"