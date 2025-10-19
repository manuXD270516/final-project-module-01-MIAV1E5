# 🏥 Sistema de Gestión de Imágenes Médicas

Sistema CRUD (Create, Read, Update, Delete) para la gestión de imágenes oftalmológicas de pacientes con glaucoma. Este proyecto permite registrar, modificar, eliminar y visualizar imágenes médicas junto con sus metadatos asociados.

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Requisitos Técnicos](#-requisitos-técnicos)
- [Instalación Paso a Paso](#-instalación-paso-a-paso)
- [Guía de Ejecución Completa](#-guía-de-ejecución-completa)
- [Comandos Esenciales](#-comandos-esenciales)
- [Caso de Uso](#-caso-de-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Funcionalidades CRUD](#-funcionalidades-crud)
- [Pruebas del Sistema](#-pruebas-del-sistema)
- [Tecnologías Utilizadas](#️-tecnologías-utilizadas)
- [Solución de Problemas](#-solución-de-problemas)
- [Dataset de Origen](#-dataset-de-origen)
- [Video Demostración](#-video-demostración)
- [Equipo de Desarrollo](#-equipo-de-desarrollo)
- [Licencia](#-licencia)

---

## 📖 Descripción

Este sistema está diseñado para gestionar un dataset médico de imágenes de fondo de ojo (Color Fundus Photography - CFP) utilizadas en el diagnóstico de glaucoma. El sistema descarga automáticamente el dataset desde Springer Nature y permite realizar operaciones CRUD sobre los registros de imágenes y sus metadatos.

### Características Principales:
- ✅ Descarga automática de dataset médico (150-300 MB)
- ✅ Gestión CRUD completa de registros de imágenes
- ✅ Visualización de imágenes con matplotlib
- ✅ Integración con datos de Excel (300+ pacientes)
- ✅ Interfaz de usuario intuitiva por consola
- ✅ Sistema de caché (no re-descarga recursos)
- ✅ Script de verificación automática

---

## 💻 Requisitos Técnicos

### Software Requerido:

| Software | Versión Mínima | Propósito |
|----------|----------------|-----------|
| Python   | 3.8+          | Lenguaje de programación |
| pip      | 20.0+         | Gestor de paquetes |
| Git      | 2.0+          | Control de versiones (opcional) |

### Espacio en Disco:
- **Mínimo**: 500 MB
- **Recomendado**: 1 GB (para dataset completo)

### Sistema Operativo:
- ✅ Windows 10/11
- ✅ Linux (Ubuntu 20.04+)
- ✅ macOS (10.15+)

### Verificar Python:
```bash
python --version
# o en algunos sistemas:
python3 --version
```
**Resultado esperado**: `Python 3.8.x` o superior

---

## 🚀 Instalación Paso a Paso

### Paso 1: Clonar o Descargar el Proyecto

```bash
# Si usa Git
git clone <url-del-repositorio>
cd Proyecto

# Si descargó el ZIP
# Extraer y navegar a la carpeta del proyecto
```

### Paso 2: Crear un Entorno Virtual (RECOMENDADO)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

**Resultado esperado**: Ver `(venv)` al inicio de la línea de comandos

### Paso 3: Actualizar pip (Recomendado)

```bash
python -m pip install --upgrade pip
```

### Paso 4: Instalar Dependencias

```bash
pip install -r requirements.txt
```

Este comando instalará todas las dependencias necesarias:
- `requests==2.31.0` - Descarga de archivos HTTP
- `patool==2.1.0` - Descompresión de archivos RAR
- `pandas==2.1.4` - Procesamiento de datos Excel
- `matplotlib==3.8.2` - Visualización de imágenes
- `openpyxl==3.1.2` - Soporte para archivos Excel (.xlsx)

**Tiempo estimado**: 1-3 minutos

### Paso 5: Verificar la Instalación (RECOMENDADO)

```bash
python verificar_instalacion.py
```

Este script verifica automáticamente:
- ✅ Versión de Python correcta (3.8+)
- ✅ Todas las dependencias instaladas
- ✅ Estructura del proyecto completa
- ✅ Estado de recursos descargados

**Verificación manual alternativa**:
```bash
python -c "import requests, patoolib, pandas, matplotlib, openpyxl; print('✓ Todas las dependencias instaladas correctamente')"
```

### Paso 6: Ejecutar la Aplicación

```bash
python main.py
```

---

## ▶️ Guía de Ejecución Completa

### Primera Ejecución

En la **primera ejecución**, el sistema realizará automáticamente:

#### 1. Descarga del Dataset (~150-300 MB)
   - Se descargará de Springer Nature Figshare
   - Se extraerá en la carpeta `dataset/`
   - **Puede tardar 5-10 minutos** según la conexión a internet

#### 2. Descarga de Archivo Excel (~5 MB)
   - Contiene metadatos de 300+ pacientes
   - Se guardará como `datos.xlsx`

#### 3. Inicio del Menú Principal
   - Sistema listo para usar

**Salida esperada**:
```
=== SISTEMA DE GESTIÓN DE IMÁGENES MÉDICAS ===

Descargando dataset...
Descomprimiendo dataset...
Dataset listo en la carpeta 'dataset'.
Descargando archivo Excel...
Archivo Excel descargado: datos.xlsx

===================================
           SISTEMA CRUD
===================================
1. Registrar nueva imagen
2. Modificar metadatos
3. Eliminar imagen
4. Mostrar imágenes registradas
5. Salir
-----------------------------------
Seleccione una opción:
```

### Ejecuciones Posteriores

El sistema detecta si los archivos ya existen y **no volverá a descargarlos**, iniciando directamente el menú principal (inicio instantáneo).

---

## 📝 Comandos Esenciales

### ⚠️ IMPORTANTE: Diferencia entre Comandos

#### Para INSTALAR dependencias (al clonar el proyecto):
```bash
pip install -r requirements.txt
```
**Cuándo usar**: Cuando clonas el proyecto o cuando alguien más agregó dependencias

#### Para CREAR/ACTUALIZAR requirements.txt (solo desarrolladores):
```bash
pip freeze > requirements.txt
```
**Cuándo usar**: Solo cuando TÚ instalas nuevas librerías al proyecto

### Comandos de Verificación

```bash
# Ver versión de Python
python --version

# Ver versión de pip
pip --version

# Ver paquetes instalados
pip list

# Verificar instalación completa
python verificar_instalacion.py
```

### Comandos de Entorno Virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
venv\Scripts\activate

# Activar entorno virtual (Linux/macOS)
source venv/bin/activate

# Desactivar entorno virtual
deactivate
```

### Comandos de Ejecución

```bash
# Ejecutar aplicación principal
python main.py

# Ejecutar módulos individuales (testing)
python -m gestor.descarga
python -m gestor.menu
```

---

## 🎯 Caso de Uso

### Contexto Clínico

**Dominio**: Oftalmología - Diagnóstico de Glaucoma  
**Usuarios**: Personal médico, investigadores, estudiantes de medicina  
**Dataset**: Color Fundus Photography (CFP) - Imágenes de fondo de ojo  
**Pacientes**: 300+ registros con metadatos completos

### Menú del Sistema

```
===================================
           SISTEMA CRUD
===================================
1. Registrar nueva imagen       → CREATE
2. Modificar metadatos          → UPDATE
3. Eliminar imagen              → DELETE
4. Mostrar imágenes registradas → READ
5. Salir                        → EXIT
-----------------------------------
```

### Escenarios de Uso Típicos

#### 1. Investigador Médico

```
Dr. García necesita analizar imágenes de pacientes con glaucoma:

1. Ejecuta el sistema: python main.py
2. Selecciona "Mostrar imágenes registradas" (Opción 4)
3. Revisa la lista de 300+ pacientes con sus datos:
   - ID del paciente
   - Edad
   - Diagnóstico (OAGG, OANG, etc.)
   - Archivo de imagen asociado
4. Selecciona una imagen (ej: opción 1)
5. El sistema muestra la imagen con metadatos en pantalla
6. Cierra la ventana de imagen
7. Ingresa 0 para volver al menú
```

#### 2. Técnico de Laboratorio

```
María necesita agregar una nueva imagen al sistema:

1. Ejecuta el sistema
2. Selecciona "Registrar nueva imagen" (Opción 1)
3. Ingresa el nombre del archivo: "150_OD_1.jpg"
4. Ingresa ID del paciente: "150"
5. Ingresa edad: "45"
6. Ingresa diagnóstico: "OAGG"
7. La imagen queda registrada en el sistema
8. Puede visualizarla en la opción 4
```

#### 3. Actualización de Datos

```
Un error en el diagnóstico debe corregirse:

1. Selecciona "Modificar metadatos" (Opción 2)
2. Ingresa el nombre de la imagen a modificar
3. Actualiza solo el campo de diagnóstico
4. Presiona Enter en los demás campos para mantenerlos
5. Los cambios quedan guardados
```

#### 4. Eliminación de Registro

```
Eliminar un registro incorrecto:

1. Selecciona "Eliminar imagen" (Opción 3)
2. Ingresa el nombre de la imagen a eliminar
3. El registro se elimina de la memoria
4. Nota: El archivo físico NO se elimina
```

### Flujo de Operaciones

```
┌─────────────────────────────────────┐
│    INICIO DEL SISTEMA               │
│    python main.py                   │
└─────────────┬───────────────────────┘
              │
              ▼
┌─────────────────────────────────────┐
│  Descarga automática de recursos    │
│  (Solo primera ejecución)           │
│  - Dataset de imágenes (~300 MB)    │
│  - Archivo Excel (~5 MB)            │
└─────────────┬───────────────────────┘
              │
              ▼
┌─────────────────────────────────────┐
│        MENÚ PRINCIPAL               │
├─────────────────────────────────────┤
│  1. Registrar nueva imagen          │◄─┐
│  2. Modificar metadatos             │  │
│  3. Eliminar imagen                 │  │
│  4. Mostrar imágenes registradas    │  │
│  5. Salir                           │  │
└─────────────┬───────────────────────┘  │
              │                          │
              │ (Opciones 1-4: Loop)     │
              └──────────────────────────┘
              │
              │ (Opción 5: Salir)
              ▼
┌─────────────────────────────────────┐
│    FIN DEL SISTEMA                  │
└─────────────────────────────────────┘
```

---

## 📁 Estructura del Proyecto

```
Proyecto/
│
├── main.py                      # ⭐ Punto de entrada principal
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Esta documentación
├── verificar_instalacion.py    # Script de verificación automática
├── .gitignore                   # Exclusiones para Git
│
├── gestor/                      # 📦 Paquete principal del sistema
│   ├── __init__.py             # Inicializador del paquete
│   ├── descarga.py             # Módulo de descarga de recursos
│   ├── imagenes.py             # Módulo de gestión CRUD de imágenes
│   └── menu.py                 # Módulo de interfaz de usuario
│
├── dataset/                     # 📂 Dataset de imágenes (auto-descargado)
│   └── ROI images/             # Carpeta con imágenes médicas
│       ├── 1_OD_1.jpg
│       ├── 2_OD_1.jpg
│       ├── 3_OD_1.jpg
│       └── ... (300+ imágenes)
│
├── datos.xlsx                   # 📊 Archivo Excel con metadatos (auto-descargado)
│
└── diagrama de clases/          # 📐 Documentación visual
    └── diagrama de clase modulo.png
```

### Descripción de Módulos

#### `main.py`
- Punto de entrada del sistema
- Orquesta la descarga de recursos
- Inicia el menú principal

#### `gestor/descarga.py`
- Descarga dataset de Springer Nature
- Descarga archivo Excel con metadatos
- Extrae archivos RAR automáticamente
- Instala dependencias dinámicamente (patool)

#### `gestor/imagenes.py`
- **CREATE**: `registrar_imagen()` - Registra nuevas imágenes
- **READ**: `mostrar_imagenes()` - Lista y visualiza imágenes
- **UPDATE**: `modificar_imagen()` - Actualiza metadatos
- **DELETE**: `eliminar_imagen()` - Elimina registros

#### `gestor/menu.py`
- Interfaz de usuario por consola
- Loop principal del sistema
- Validación de opciones

---

## ⚙️ Funcionalidades CRUD

### 1. 🆕 Registrar Nueva Imagen (CREATE)

Permite agregar una nueva imagen al sistema con sus metadatos.

**Datos requeridos**:
- Nombre del archivo (ej: `150_OD_1.jpg`)
- ID del paciente (ej: `150`)
- Edad del paciente (ej: `45`)
- Diagnóstico médico (ej: `OAGG`)

**Validaciones**:
- ✅ Verifica que la imagen exista en `dataset/ROI images/`
- ✅ Almacena en diccionario en memoria

**Ejemplo de uso**:
```
Seleccione una opción: 1
Nombre del archivo (ej. 1_OD_1.jpg): 150_OD_1.jpg
ID del paciente (ej. 144): 150
Edad del paciente (ej. 21): 45
Diagnóstico (ej. OAGG): OAGG
Imagen '150_OD_1.jpg' registrada correctamente.
```

---

### 2. 📝 Modificar Metadatos (UPDATE)

Permite actualizar información de imágenes ya registradas.

**Campos modificables**:
- ID del paciente
- Edad
- Diagnóstico

**Características**:
- ✅ Preserva valores no modificados (presionar Enter)
- ✅ Muestra valores actuales durante la edición
- ✅ Validación de existencia del registro

**Ejemplo de uso**:
```
Seleccione una opción: 2
Ingrese el nombre del archivo a modificar: 150_OD_1.jpg
Deje en blanco si no desea cambiar el valor.
Nuevo ID paciente [150]: 
Nueva edad [45]: 46
Nuevo diagnóstico [OAGG]: 
Imagen '150_OD_1.jpg' modificada correctamente.
```

---

### 3. 🗑️ Eliminar Imagen (DELETE)

Elimina un registro del sistema.

**Características**:
- Búsqueda por nombre de archivo
- Elimina solo el registro en memoria
- **NO elimina el archivo físico**
- Confirmación visual

**Ejemplo de uso**:
```
Seleccione una opción: 3
Ingrese el nombre de la imagen a eliminar: 150_OD_1.jpg
Imagen '150_OD_1.jpg' eliminada.
```

---

### 4. 👁️ Mostrar Imágenes Registradas (READ)

Funcionalidad más completa del sistema.

**Características**:
- Lista todos los registros del Excel (primeras 300 filas)
- Incluye registros agregados manualmente
- Muestra información completa de cada paciente
- Permite seleccionar imágenes para visualización
- Visualización con matplotlib (ventana emergente)
- Título de imagen incluye: Paciente, Edad, Diagnóstico

**Ejemplo de uso**:
```
Seleccione una opción: 4

Lista de registros disponibles:

1. Paciente: 144 | Edad: 21 | Diagnóstico: OAGG | Imagen: 1_OD_1.jpg
2. Paciente: 145 | Edad: 34 | Diagnóstico: OANG | Imagen: 2_OD_1.jpg
3. Paciente: 146 | Edad: 45 | Diagnóstico: OAGG | Imagen: 3_OD_1.jpg
...

Ingrese el número de imagen que desea visualizar, o '0' para salir: 1
[Se abre ventana con la imagen]
[Cerrar ventana para continuar]

Ingrese el número de imagen que desea visualizar, o '0' para salir: 0
Volviendo al menú principal...
```

---

### 5. 📥 Descarga Automática de Recursos

Se ejecuta automáticamente en la primera ejecución.

**Recursos descargados**:
1. **Dataset de imágenes**:
   - URL: Springer Nature Figshare
   - Tamaño: ~150-300 MB
   - Formato: RAR (se extrae automáticamente)
   - Destino: `dataset/ROI images/`

2. **Archivo Excel**:
   - URL: Springer Nature Figshare
   - Tamaño: ~5 MB
   - Formato: XLSX
   - Destino: `datos.xlsx`

**Características**:
- ✅ Sistema de caché (no re-descarga si existe)
- ✅ Extracción automática de archivos comprimidos
- ✅ Limpieza de archivos temporales
- ✅ Instalación automática de dependencias (patool)

---

## 🧪 Pruebas del Sistema

### Prueba Rápida (5 minutos)

#### 1. Verificar Instalación
```bash
python verificar_instalacion.py
```
**✓ Éxito**: Todos los checks en verde

---

#### 2. Ejecutar Aplicación
```bash
python main.py
```
**✓ Éxito**: Menú se muestra correctamente

---

#### 3. Visualizar Imágenes Existentes
```
1. Seleccionar opción: 4
2. Revisar lista de imágenes
3. Ingresar: 1
4. Verificar que se muestra imagen
5. Cerrar ventana
6. Ingresar: 0
```
**✓ Éxito**: Imagen se visualiza con metadatos

---

#### 4. Registrar Nueva Imagen
```
1. Seleccionar opción: 1
2. Nombre: 1_OD_1.jpg
3. ID: 999
4. Edad: 35
5. Diagnóstico: OAGG
```
**✓ Éxito**: Mensaje de confirmación

---

#### 5. Modificar Registro
```
1. Seleccionar opción: 2
2. Nombre: 1_OD_1.jpg
3. Cambiar edad: 36
4. Presionar Enter en otros campos
```
**✓ Éxito**: Mensaje de modificación

---

#### 6. Verificar Cambios
```
1. Seleccionar opción: 4
2. Buscar registro con ID 999
3. Verificar edad = 36
```
**✓ Éxito**: Cambios reflejados

---

#### 7. Eliminar Registro
```
1. Seleccionar opción: 3
2. Nombre: 1_OD_1.jpg
```
**✓ Éxito**: Mensaje de eliminación

---

#### 8. Salir del Sistema
```
1. Seleccionar opción: 5
```
**✓ Éxito**: Sistema cierra correctamente

---

### Checklist de Prueba Completa

- [ ] Python 3.8+ instalado
- [ ] Entorno virtual creado y activado
- [ ] Dependencias instaladas sin errores
- [ ] Script de verificación ejecutado (todo OK)
- [ ] Primera ejecución completada (descarga de recursos)
- [ ] ✅ Prueba 1: Visualizar imágenes existentes
- [ ] ✅ Prueba 2: Registrar nueva imagen
- [ ] ✅ Prueba 3: Modificar metadatos
- [ ] ✅ Prueba 4: Verificar cambios en visualización
- [ ] ✅ Prueba 5: Eliminar registro
- [ ] ✅ Prueba 6: Salir del sistema

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Uso | Instalación |
|------------|---------|-----|-------------|
| Python | 3.8+ | Lenguaje principal | [python.org](https://python.org) |
| requests | 2.31.0 | Descarga de archivos HTTP | `pip install requests` |
| patool | 2.1.0 | Descompresión de RAR | `pip install patool` |
| pandas | 2.1.4 | Procesamiento de Excel | `pip install pandas` |
| matplotlib | 3.8.2 | Visualización de imágenes | `pip install matplotlib` |
| openpyxl | 3.1.2 | Soporte para .xlsx | `pip install openpyxl` |

### Arquitectura del Sistema

```
┌─────────────────────────────────────────┐
│           CAPA DE INTERFAZ              │
│         (gestor/menu.py)                │
│    - Menú de consola                    │
│    - Validación de entrada              │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│         CAPA DE LÓGICA DE NEGOCIO       │
│         (gestor/imagenes.py)            │
│    - Operaciones CRUD                   │
│    - Gestión de metadatos               │
│    - Visualización                      │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│          CAPA DE DATOS                  │
│    - Diccionario en memoria             │
│    - Lectura de Excel (pandas)          │
│    - Archivos de imagen                 │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│       CAPA DE INFRAESTRUCTURA           │
│      (gestor/descarga.py)               │
│    - Descarga de recursos               │
│    - Extracción de archivos             │
│    - Gestión de dependencias            │
└─────────────────────────────────────────┘
```

---

## 🔧 Solución de Problemas

### Problema 1: "pip no reconocido"

**Solución**:
```bash
python -m pip install -r requirements.txt
```

---

### Problema 2: "python no reconocido"

**Diagnóstico**: Python no está en el PATH del sistema

**Solución**:
- Windows: Reinstalar Python y marcar "Add to PATH"
- Linux/macOS: Intentar con `python3`:
```bash
python3 --version
python3 -m pip install -r requirements.txt
python3 main.py
```

---

### Problema 3: Error al descargar dataset

**Causas posibles**:
- Sin conexión a internet
- Firewall bloqueando la descarga
- Problema con el servidor de Figshare

**Soluciones**:
1. Verificar conexión a internet
2. Desactivar temporalmente firewall/antivirus
3. Intentar ejecutar nuevamente
4. Descarga manual:
   - Dataset: https://springernature.figshare.com/ndownloader/files/41358150
   - Excel: https://springernature.figshare.com/ndownloader/files/41670009

---

### Problema 4: "No module named 'openpyxl'"

**Solución**:
```bash
pip install openpyxl
```

---

### Problema 5: "No module named 'patoolib'"

**Solución**:
```bash
pip install patool
```

---

### Problema 6: Imágenes no se muestran

**Diagnóstico**: Problema con matplotlib o backend gráfico

**Soluciones**:

**Windows**:
```bash
pip install matplotlib --upgrade
```

**Linux**:
```bash
sudo apt-get install python3-tk
pip install matplotlib --upgrade
```

**macOS**:
```bash
brew install python-tk
pip install matplotlib --upgrade
```

---

### Problema 7: Error al leer Excel

**Solución**:
```bash
pip install pandas openpyxl --upgrade
```

---

### Problema 8: Entorno virtual no se activa

**Windows**:
```bash
# Si hay error de permisos
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

**Linux/macOS**:
```bash
# Verificar permisos
chmod +x venv/bin/activate
source venv/bin/activate
```

---

### Problema 9: Dependencias no se instalan

**Solución paso a paso**:
```bash
# 1. Actualizar pip
python -m pip install --upgrade pip

# 2. Actualizar setuptools
pip install --upgrade setuptools wheel

# 3. Instalar dependencias una por una
pip install requests
pip install patool
pip install pandas
pip install matplotlib
pip install openpyxl

# 4. Verificar
pip list
```

---

### Problema 10: "La imagen no existe en el directorio"

**Causas**:
- Dataset no se descargó correctamente
- Nombre de archivo incorrecto

**Soluciones**:
1. Verificar que existe la carpeta `dataset/ROI images/`
2. Listar archivos disponibles:
```bash
# Windows
dir "dataset\ROI images"

# Linux/macOS
ls "dataset/ROI images"
```
3. Usar un nombre de archivo existente

---

## 📊 Dataset de Origen

**Fuente**: Springer Nature - Figshare  
**Tipo**: Imágenes médicas de fondo de ojo (Color Fundus Photography - CFP)  
**Pacientes**: 300+ registros con metadatos completos  
**Formato**: 
- Imágenes: JPEG
- Metadatos: XLSX (Excel)

**Categorías de Glaucoma incluidas**:
- **OAGG**: Open-Angle Glaucoma with Generalized defects
- **OANG**: Open-Angle Normal-tension Glaucoma
- Y otras categorías diagnósticas

**Enlaces de descarga**:
- Dataset: https://springernature.figshare.com/ndownloader/files/41358150
- Excel: https://springernature.figshare.com/ndownloader/files/41670009

**Estructura del dataset**:
```
dataset/
└── ROI images/
    ├── 1_OD_1.jpg
    ├── 2_OD_1.jpg
    ├── 3_OD_1.jpg
    └── ... (300+ imágenes)
```

**Estructura del Excel** (`datos.xlsx`):
- **Hoja**: Baseline
- **Columnas**:
  - Subject Number (ID del paciente)
  - Age (Edad)
  - Category of Glaucoma (Diagnóstico)
  - Corresponding CFP (Nombre de archivo de imagen)
  - [Otras columnas de metadatos médicos]

---

## 🎥 Video Demostración

### Video Tutorial del Sistema

Para ver una demostración completa del funcionamiento del sistema, incluyendo:
- ✅ Proceso de instalación
- ✅ Descarga automática de recursos
- ✅ Uso de todas las funcionalidades CRUD
- ✅ Visualización de imágenes médicas
- ✅ Casos de uso prácticos

**Accede al video en Google Drive**:

📹 **https://1drv.ms/f/c/fc5cbdc14bdcf26d/EmDYF9JXk0hBnxF2NIfPvoEBLmqwAYf7otstLpAllocbaA?e=85WDEO**

> **Nota para el equipo**: Por favor, subir el video demo a Google Drive, configurarlo como "Cualquier persona con el enlace puede ver" y agregar el enlace arriba.

### Contenido Sugerido para el Video

1. **Introducción** (0:00 - 0:30)
   - Presentación del equipo
   - Descripción del proyecto

2. **Instalación** (0:30 - 2:00)
   - Creación de entorno virtual
   - Instalación de dependencias
   - Ejecución del script de verificación

3. **Primera Ejecución** (2:00 - 4:00)
   - Descarga de dataset
   - Descarga de Excel
   - Inicio del menú principal

4. **Demostración CRUD** (4:00 - 8:00)
   - Visualizar imágenes existentes (READ)
   - Registrar nueva imagen (CREATE)
   - Modificar metadatos (UPDATE)
   - Eliminar registro (DELETE)

5. **Cierre** (8:00 - 16:30)
   - Resumen de funcionalidades codigo
   - Explicacion de diagrama de clases

---


## Buenas Practicas Utilizadas PEP8
- PEP8 es la guía de estilo para escribir código en Python de forma clara y uniforme. Define reglas sobre la indentación, nombres de variables y organización del código. Por ejemplo, recomienda usar cuatro espacios para indentar y nombres en minúsculas con guiones bajos, como mi_variable. En mi proyecto apliqué PEP8 al nombrar funciones y variables correctamente y al mantener una estructura limpia, lo que facilitó la lectura y comprensión del código.


## 👥 Equipo de Desarrollo

Este proyecto fue desarrollado como parte del **Módulo 01 - Proyecto Final**.

### Integrantes del Equipo:

| Nombre | Rol |
|--------|-----|
| **Erick Ariel Coca Mariaca** | Desarrollador |
| **Cristhian Labrandero Perez** | Desarrollador |
| **Josue Choque Llanos** | Desarrollador |
| **Manuel Joaquin Saavedra Severiche** | Desarrollador |

### Contribuciones

Este proyecto demuestra la aplicación de:
- ✅ Programación Orientada a Objetos (POO)
- ✅ Gestión de archivos y datos
- ✅ Integración de bibliotecas externas
- ✅ Desarrollo de sistemas CRUD
- ✅ Manejo de datasets médicos
- ✅ Documentación profesional
- ✅ Buenas prácticas de programación PEP8
  

### Agradecimientos

Agradecemos a:
- **Springer Nature** por proporcionar el dataset médico
- **Nuestros instructores** por la guía durante el desarrollo
- **La comunidad de Python** por las excelentes bibliotecas utilizadas

---

## 📄 Licencia

Este proyecto es de **uso académico**. 

### Términos de Uso:

- ✅ Permitido el uso para fines educativos
- ✅ Permitido el estudio y modificación del código
- ✅ Permitido compartir con fines académicos

### Nota sobre el Dataset:

El dataset médico proviene de **Springer Nature** y está sujeto a sus términos de uso. No se permite el uso comercial del dataset sin autorización.

---

## 📞 Soporte y Contacto

### Para Dudas o Problemas:

1. **Revisar esta documentación**: Especialmente la sección de [Solución de Problemas](#-solución-de-problemas)
2. **Ejecutar script de verificación**: `python verificar_instalacion.py`
3. **Contactar al equipo**: [Agregar correo o medio de contacto del equipo]

### Reportar Issues:

Si encuentras un bug o tienes una sugerencia de mejora:
1. Describir el problema detalladamente
2. Incluir los pasos para reproducirlo
3. Adjuntar capturas de pantalla si es posible
4. Indicar tu sistema operativo y versión de Python

---

## 📚 Recursos Adicionales

### Documentación de Bibliotecas Utilizadas:

- [Python Official Documentation](https://docs.python.org/3/)
- [Requests Documentation](https://docs.python-requests.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Patool Documentation](https://wummel.github.io/patool/)

### Tutoriales Relacionados:

- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Working with Excel in Python](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
- [Image Processing with Matplotlib](https://matplotlib.org/stable/tutorials/introductory/images.html)

---

## 🔄 Control de Versiones

### Historial de Versiones:

- **v1.0** (Octubre 2025) - Versión inicial
  - Implementación completa del CRUD
  - Descarga automática de dataset
  - Visualización de imágenes
  - Documentación completa

### Próximas Mejoras (Futuro):

- 🔜 Persistencia de datos en base de datos
- 🔜 Interfaz gráfica (GUI) con Tkinter/PyQt
- 🔜 Exportación de reportes en PDF
- 🔜 Búsqueda avanzada de pacientes
- 🔜 Estadísticas y gráficos del dataset
- 🔜 Sistema de usuarios y autenticación

---

## 📝 Notas Importantes

### Limitaciones Conocidas:

1. **Persistencia**: Los registros agregados manualmente se almacenan solo en memoria y se pierden al cerrar el programa.
2. **Dataset**: Se procesan solo las primeras 300 filas del Excel.
3. **Conexión**: Requiere conexión a internet en la primera ejecución.
4. **Concurrencia**: No soporta múltiples usuarios simultáneos.
5. **Validación**: Validaciones básicas en la entrada de datos.

### Recomendaciones de Uso:

- ✅ Usar siempre entorno virtual
- ✅ Mantener backup del archivo Excel
- ✅ No modificar manualmente el diccionario de imágenes
- ✅ Cerrar el programa correctamente (opción 5)
- ✅ No interrumpir la descarga de recursos

---

## 🎓 Contexto Académico

**Institución**: [Agregar nombre de la institución]  
**Curso**: Módulo 01 - [Agregar nombre del curso]  
**Fecha**: Octubre 2025  
**Tipo**: Proyecto Final de Módulo

### Objetivos de Aprendizaje Cumplidos:

- ✅ Implementar un sistema CRUD funcional
- ✅ Gestionar archivos y estructuras de datos
- ✅ Integrar bibliotecas externas
- ✅ Desarrollar interfaz de usuario
- ✅ Procesar datos de Excel
- ✅ Visualizar información gráficamente
- ✅ Documentar código profesionalmente
- ✅ Trabajar en equipo
- ✅ Aplicar buenas prácticas de programación

---

## 🌟 Características Destacadas

### Lo que hace especial a este proyecto:

1. **Descarga Automática**: No requiere configuración manual de datos
2. **Caché Inteligente**: No re-descarga recursos existentes
3. **Script de Verificación**: Diagnóstico automático de problemas
4. **Visualización Integrada**: Ver imágenes directamente desde el sistema
5. **Documentación Completa**: Guías detalladas para cada funcionalidad
6. **Arquitectura Modular**: Código organizado y mantenible
7. **Datos Reales**: Dataset médico real de Springer Nature
8. **Interfaz Intuitiva**: Fácil de usar para usuarios no técnicos

---

## 🚀 Inicio Rápido (Resumen)

```bash
# 1. Verificar Python
python --version

# 2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Verificar instalación
python verificar_instalacion.py

# 5. Ejecutar aplicación
python main.py
```

---

**Última actualización**: Octubre 2025  
**Versión del Proyecto**: 1.0  
**Estado**: ✅ Completo y Funcional

---

<div align="center">

### 🏥 Sistema de Gestión de Imágenes Médicas

**Desarrollado con ❤️ por el equipo de desarrollo**

**Python** | **Pandas** | **Matplotlib** | **Medical Imaging**

---

© 2025 - Proyecto Académico - Módulo 01

</div>
