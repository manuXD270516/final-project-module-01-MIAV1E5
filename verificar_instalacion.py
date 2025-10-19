"""
Script de verificación de instalación del Sistema de Gestión de Imágenes Médicas.
Ejecutar antes de main.py para verificar que todo está configurado correctamente.
"""

import sys
import os


def verificar_version_python():
    """Verifica que la versión de Python sea 3.8 o superior."""
    print("🔍 Verificando versión de Python...")
    version = sys.version_info
    
    if version.major == 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro}")
        print("   ⚠️  Se requiere Python 3.8 o superior")
        return False


def verificar_dependencia(nombre_modulo, nombre_paquete=None):
    """Verifica si un módulo está instalado."""
    if nombre_paquete is None:
        nombre_paquete = nombre_modulo
    
    try:
        __import__(nombre_modulo)
        print(f"   ✅ {nombre_paquete} - Instalado")
        return True
    except ImportError:
        print(f"   ❌ {nombre_paquete} - NO instalado")
        return False


def verificar_dependencias():
    """Verifica todas las dependencias necesarias."""
    print("\n🔍 Verificando dependencias...")
    
    dependencias = [
        ("requests", "requests"),
        ("patoolib", "patool"),
        ("pandas", "pandas"),
        ("matplotlib", "matplotlib"),
        ("openpyxl", "openpyxl"),
    ]
    
    resultados = []
    for modulo, paquete in dependencias:
        resultados.append(verificar_dependencia(modulo, paquete))
    
    return all(resultados)


def verificar_estructura_proyecto():
    """Verifica que existen los archivos necesarios del proyecto."""
    print("\n🔍 Verificando estructura del proyecto...")
    
    archivos_necesarios = [
        "main.py",
        "requirements.txt",
        "gestor/__init__.py",
        "gestor/descarga.py",
        "gestor/imagenes.py",
        "gestor/menu.py",
    ]
    
    todos_existen = True
    for archivo in archivos_necesarios:
        if os.path.exists(archivo):
            print(f"   ✅ {archivo}")
        else:
            print(f"   ❌ {archivo} - NO encontrado")
            todos_existen = False
    
    return todos_existen


def verificar_recursos_descargados():
    """Verifica si los recursos ya fueron descargados."""
    print("\n🔍 Verificando recursos descargados...")
    
    dataset_existe = os.path.exists("dataset")
    excel_existe = os.path.exists("datos.xlsx")
    
    if dataset_existe:
        print("   ✅ Dataset - Ya descargado")
    else:
        print("   ⚠️  Dataset - Se descargará en la primera ejecución (~150-300 MB)")
    
    if excel_existe:
        print("   ✅ Archivo Excel - Ya descargado")
    else:
        print("   ⚠️  Archivo Excel - Se descargará en la primera ejecución (~5 MB)")
    
    return dataset_existe and excel_existe


def mostrar_resumen(python_ok, dependencias_ok, estructura_ok, recursos_ok):
    """Muestra un resumen del estado de la instalación."""
    print("\n" + "=" * 60)
    print("                    RESUMEN DE VERIFICACIÓN")
    print("=" * 60)
    
    checks = [
        ("Versión de Python", python_ok),
        ("Dependencias instaladas", dependencias_ok),
        ("Estructura del proyecto", estructura_ok),
        ("Recursos descargados", recursos_ok),
    ]
    
    for nombre, estado in checks:
        simbolo = "✅" if estado else "❌"
        print(f"{simbolo} {nombre}")
    
    print("=" * 60)
    
    if python_ok and dependencias_ok and estructura_ok:
        print("\n🎉 ¡Todo listo para ejecutar la aplicación!")
        print("\nEjecutar:")
        print("   python main.py")
        
        if not recursos_ok:
            print("\n⏱️  Primera ejecución: Los recursos se descargarán automáticamente")
            print("   (Puede tardar 5-10 minutos según tu conexión)")
    else:
        print("\n⚠️  Hay problemas que deben resolverse:")
        
        if not python_ok:
            print("   • Actualizar Python a versión 3.8 o superior")
        
        if not dependencias_ok:
            print("   • Instalar dependencias: pip install -r requirements.txt")
        
        if not estructura_ok:
            print("   • Verificar que todos los archivos del proyecto estén presentes")


def main():
    """Función principal de verificación."""
    print("\n" + "=" * 60)
    print("  VERIFICACIÓN DE INSTALACIÓN - Sistema de Gestión Médica")
    print("=" * 60)
    
    # Realizar todas las verificaciones
    python_ok = verificar_version_python()
    dependencias_ok = verificar_dependencias()
    estructura_ok = verificar_estructura_proyecto()
    recursos_ok = verificar_recursos_descargados()
    
    # Mostrar resumen
    mostrar_resumen(python_ok, dependencias_ok, estructura_ok, recursos_ok)
    
    print("\n" + "=" * 60)
    print()


if __name__ == "__main__":
    main()

