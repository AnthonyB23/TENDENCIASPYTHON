# TENDENCIASPYTHON
Este proyecto grupal utiliza scripts para gestionar entornos virtuales con Python.

## Descripción

El objetivo del proyecto es facilitar la administración y activación de entornos virtuales en proyectos Python. Incluye scripts automatizados para sistemas Windows, Linux y MacOS.

## Estructura del Proyecto

- `activate.bat`: Script para activar el entorno virtual en Windows.
- `Activate.ps1`: Script en PowerShell para activar el entorno virtual.
- `deactivate.bat`: Script para desactivar el entorno virtual en Windows.
- `activate.fish`: Script para activar el entorno virtual usando el shell Fish (Linux/MacOS).
- `README.md`: Documentación básica del proyecto.

## Archivo requirements.txt

Este archivo es muy importante y debemos crearlo ya que no se crea automaticamente enlista las dependencias necesaeias para le entorno .

- `Flask==3.0.3`
- `Flask-Cors==4.0.1`

## Estructura de datos Json
  
  Instrucciones para ejecutar 

  1.- Crea el entorno virtual :

   `Fpython -m venv venv-`
   
   2.-Activa el entorno:

   `venv\Scripts\activate`

   3.-Instala las dependencias:

`pip install -r requirements.txt`

   4.-Ejecuta el servidor:

   `python app.py`

   5.-Prueba en el navegador:
   - http://http://127.0.0.1:3000

- http://127.0.0.1:3000/api/saludo

- http://127.0.0.1:3000/api/estudiantes

- http://127.0.0.1:3000//api/estudiantes/<id>

- http://127.0.0.1:3000/api/estudiantes/carrera/<carrera>



## Instalación

1. Clonar el repositorio.
- `git clone`

2. Ubica los scripts en la carpeta principal del proyecto.
- `cd ruta/de/tu/proyecto`


3. Ejecuta el script .
- `python app.py`


## Uso

Ejecuta el script 

`activate.bat`

 `Activate.ps1` (PowerShell) para activar el entorno virtual y prepararlo para desarrollo.