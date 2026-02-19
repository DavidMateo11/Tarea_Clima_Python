from inventario import Inventario
from producto import Producto

def menu():
    mi_inv = Inventario()
    while True:
        print("\n--- SISTEMA DE GESTIÓN (REQUISITO 4) ---")
        print("1. Añadir Producto\n2. Mostrar Inventario\n3. Salir")
        op = input("Seleccione una opción: ")

        if op == '1':
            try:
                id_p = input("ID: ")
                nom = input("Nombre: ")
                can = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                mi_inv.añadir_producto(Producto(id_p, nom, can, pre))
            except ValueError:
                print(">>> ERROR: Cantidad y Precio deben ser números.")
        elif op == '2':
            mi_inv.mostrar_todo()
        elif op == '3':
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    menu()