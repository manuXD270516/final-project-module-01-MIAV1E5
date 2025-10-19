from gestor.imagenes import (
    registrar_imagen,
    modificar_imagen,
    eliminar_imagen,
    mostrar_imagenes,
)


def ejecutar_menu():
    """Ejecutar el menú principal del sistema CRUD."""
    while True:
        print("\n" + "=" * 35)
        print("           SISTEMA CRUD")
        print("=" * 35)
        print("1. Registrar nueva imagen")
        print("2. Modificar metadatos")
        print("3. Eliminar imagen")
        print("4. Mostrar imágenes registradas")
        print("5. Salir")
        print("-" * 35)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_imagen()
        elif opcion == "2":
            modificar_imagen()
        elif opcion == "3":
            eliminar_imagen()
        elif opcion == "4":
            mostrar_imagenes()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1-5.")


if __name__ == "__main__":
    ejecutar_menu()