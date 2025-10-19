from gestor.descarga import descargar_dataset, descargar_excel
from gestor.menu import ejecutar_menu


def main():
    """Función principal del sistema de gestión de imágenes médicas."""
    print("\n=== SISTEMA DE GESTIÓN DE IMÁGENES MÉDICAS ===")
    print()

    # Descargar recursos necesarios
    descargar_dataset()
    descargar_excel()

    # Ejecutar menú principal
    ejecutar_menu()


if __name__ == "__main__":
    main()