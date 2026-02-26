from inventario import Inventario
from producto import Producto


def mostrar_menu():
    print("\n" + "=" * 30)
    print(" SISTEMA DE GESTIÓN DE INVENTARIO ")
    print("=" * 30)
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    print("=" * 30)


def ejecutar():
    # Se crea la instancia del inventario (esto carga el archivo automáticamente)
    mi_inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            id_p = input("Ingrese el ID único: ")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad inicial: "))
                precio = float(input("Precio: "))
                nuevo_p = Producto(id_p, nombre, cantidad, precio)
                mi_inventario.añadir(nuevo_p)
            except ValueError:
                print("Error: Cantidad y Precio deben ser números.")

        elif opcion == "2":
            id_p = input("Ingrese el ID del producto a eliminar: ")
            mi_inventario.eliminar(id_p)

        elif opcion == "3":
            id_p = input("Ingrese el ID del producto a actualizar: ")
            print("Deje vacío si no desea cambiar el valor.")
            c_input = input("Nueva cantidad: ")
            p_input = input("Nuevo precio: ")

            cant = int(c_input) if c_input else None
            prec = float(p_input) if p_input else None
            mi_inventario.actualizar(id_p, cant, prec)

        elif opcion == "4":
            nombre = input("Ingrese el nombre (o parte del nombre) a buscar: ")
            mi_inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            print("\n--- LISTA DE PRODUCTOS ---")
            mi_inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema... ¡Adiós!")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    ejecutar()