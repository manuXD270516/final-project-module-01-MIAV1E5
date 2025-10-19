import os
import subprocess

import requests


def instalar_dependencias():
    """Instalar patool si no está disponible."""
    try:
        import patoolib
    except ImportError:
        print("Instalando dependencia 'patool'...")
        subprocess.check_call(['pip', 'install', 'patool'])
        import patoolib
    return patoolib


# Instalar dependencias al importar
patoolib = instalar_dependencias()


def descargar_dataset():
    """Descargar y extraer el dataset comprimido."""
    url = "https://springernature.figshare.com/ndownloader/files/41358150"
    archivo = "dataset.rar"
    carpeta = "dataset"

    if os.path.exists(carpeta):
        print("Dataset ya descargado y extraído.")
        return

    print("Descargando dataset...")
    response = requests.get(url)
    with open(archivo, 'wb') as file:
        file.write(response.content)

    print("Descomprimiendo dataset...")
    patoolib.extract_archive(archivo, outdir=carpeta)

    # Limpiar archivo comprimido después de extraer
    if os.path.exists(archivo):
        os.remove(archivo)

    print("Dataset listo en la carpeta 'dataset'.")


def descargar_excel():
    """Descargar archivo Excel con los datos."""
    url = "https://springernature.figshare.com/ndownloader/files/41670009"
    archivo = "datos.xlsx"

    if os.path.exists(archivo):
        print("Archivo Excel ya descargado.")
        return

    print("Descargando archivo Excel...")
    response = requests.get(url)
    with open(archivo, 'wb') as file:
        file.write(response.content)

    print(f"Archivo Excel descargado: {archivo}")


if __name__ == "__main__":
    descargar_dataset()
    descargar_excel()