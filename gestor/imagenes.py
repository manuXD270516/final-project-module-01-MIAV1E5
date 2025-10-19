import os

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd

# Diccionario para almacenar metadatos de imágenes
imagenes = {}


def registrar_imagen():
    """Registrar una nueva imagen en el sistema."""
    nombre = input("Nombre del archivo (ej. 1_OD_1.jpg): ")
    ruta = os.path.join("dataset/ROI images", nombre)

    if not os.path.exists(ruta):
        print("La imagen no existe en el directorio.")
        return

    paciente = input("ID del paciente (ej. 144): ")
    edad = int(input("Edad del paciente (ej. 21): "))
    diagnostico = input("Diagnóstico (ej. OAGG): ")

    imagenes[nombre] = {
        "path": ruta,
        "paciente": paciente,
        "edad": edad,
        "diagnostico": diagnostico,
    }

    print(f"Imagen '{nombre}' registrada correctamente.")


def modificar_imagen():
    """Modificar los metadatos de una imagen registrada."""
    nombre = input("Ingrese el nombre del archivo a modificar: ")

    if nombre not in imagenes:
        print("No se encontró esa imagen registrada.")
        return

    print("Deje en blanco si no desea cambiar el valor.")

    paciente_actual = imagenes[nombre]['paciente']
    edad_actual = imagenes[nombre]['edad']
    diagnostico_actual = imagenes[nombre]['diagnostico']

    nuevo_paciente = input(f"Nuevo ID paciente [{paciente_actual}]: ") or paciente_actual
    nueva_edad = input(f"Nueva edad [{edad_actual}]: ")
    nuevo_diagnostico = input(f"Nuevo diagnóstico [{diagnostico_actual}]: ") or diagnostico_actual

    imagenes[nombre]['paciente'] = nuevo_paciente
    if nueva_edad:
        imagenes[nombre]['edad'] = int(nueva_edad)
    imagenes[nombre]['diagnostico'] = nuevo_diagnostico

    print(f"Imagen '{nombre}' modificada correctamente.")


def eliminar_imagen():
    """Eliminar una imagen del registro."""
    nombre = input("Ingrese el nombre de la imagen a eliminar: ")

    if nombre in imagenes:
        del imagenes[nombre]
        print(f"Imagen '{nombre}' eliminada.")
    else:
        print("No se encontró esa imagen.")


def _leer_datos_excel(excel_path, img_folder):
    """Leer datos del archivo Excel y procesarlos."""
    registros = []

    if not os.path.exists(excel_path):
        return registros

    try:
        dataframe = pd.read_excel(excel_path, sheet_name="Baseline")
        dataframe.columns = dataframe.columns.str.strip()

        for _, row in dataframe.head(300).iterrows():
            if all(pd.isna(row[col]) for col in [
                "Subject Number", "Age", "Category of Glaucoma", "Corresponding CFP"
            ]):
                continue

            paciente = (
                int(row["Subject Number"])
                if not pd.isna(row["Subject Number"])
                else None
            )
            edad = int(row["Age"]) if not pd.isna(row["Age"]) else None
            diagnostico = (
                str(row["Category of Glaucoma"])
                if not pd.isna(row["Category of Glaucoma"])
                else None
            )
            img_name = (
                str(row["Corresponding CFP"]).strip()
                if not pd.isna(row["Corresponding CFP"])
                else None
            )
            img_path = (
                os.path.join(img_folder, img_name)
                if img_name
                else None
            )

            if any([paciente, edad, diagnostico, img_name]):
                registros.append({
                    "paciente": paciente,
                    "edad": edad,
                    "diagnostico": diagnostico,
                    "img_name": img_name,
                    "path": img_path,
                })

    except Exception as error:
        print(f"Error al leer el Excel: {error}")

    return registros


def _agregar_imagenes_registradas(registros):
    """Agregar imágenes registradas en memoria a la lista de registros."""
    for nombre, datos in imagenes.items():
        registros.append({
            "paciente": datos.get("paciente"),
            "edad": datos.get("edad"),
            "diagnostico": datos.get("diagnostico"),
            "img_name": nombre,
            "path": datos.get("path"),
        })


def _mostrar_lista_registros(registros):
    """Mostrar la lista de registros disponibles."""
    print("\nLista de registros disponibles:\n")
    for indice, registro in enumerate(registros, 1):
        print(
            f"{indice}. Paciente: {registro['paciente']} | "
            f"Edad: {registro['edad']} | "
            f"Diagnóstico: {registro['diagnostico']} | "
            f"Imagen: {registro['img_name']}"
        )


def _visualizar_imagen_seleccionada(registros):
    """Manejar la visualización de imágenes seleccionadas."""
    while True:
        opcion = input(
            "\nIngrese el número de imagen que desea visualizar, "
            "o '0' para salir: "
        )

        if opcion == '0':
            print("Volviendo al menú principal...")
            break

        try:
            indice = int(opcion) - 1
            if indice < 0 or indice >= len(registros):
                print("Opción no válida. Intente nuevamente.")
                continue

            registro = registros[indice]
            img_path = registro['path']

            if not img_path or not os.path.exists(img_path):
                print("No se tiene imagen disponible para este registro.")
                continue

            _mostrar_imagen(registro, img_path)

        except ValueError:
            print("Debe ingresar un número válido.")


def _mostrar_imagen(registro, img_path):
    """Mostrar una imagen con matplotlib."""
    img = mpimg.imread(img_path)
    plt.imshow(img)
    plt.axis("off")

    titulo = (
        f"Paciente {registro['paciente']} - "
        f"Edad {registro['edad']} - "
        f"Dx: {registro['diagnostico']}"
    )
    plt.title(titulo, fontsize=10)
    plt.show()


def mostrar_imagenes():
    """Mostrar y visualizar imágenes disponibles."""
    excel_path = "datos.xlsx"
    img_folder = "dataset/ROI images"

    registros = _leer_datos_excel(excel_path, img_folder)
    _agregar_imagenes_registradas(registros)

    if not registros:
        print("No hay registros válidos para mostrar.")
        return

    _mostrar_lista_registros(registros)
    _visualizar_imagen_seleccionada(registros)