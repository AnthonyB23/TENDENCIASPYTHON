# TENDENCIASPYTHON
Este proyecto consiste en la creación de un servicio web con Python utilizando el framework Flask.

## Descripción

A través del servicio se implementaron distintos endpoints para mostrar información de estudiantes, demostrando cómo funciona la comunicación entre el servidor y el cliente mediante peticiones HTTP.

## Estructura del Proyecto

- `activate`: Script para activar el entorno virtual.
- `app.py`: Archivo principal que inicia el servidor web y define los endpoints.
- `README.md`: Documentación básica del proyecto.

## Archivo requirements.txt

Este archivo es muy importante y debemos crearlo ya que no se crea automaticamente enlista las dependencias necesaeias para le entorno .

- `Flask==3.0.3`
- `Flask-Cors==4.0.1`

## Estructura de datos Json
  
  Instrucciones para ejecutar 

   1.- Crea el entorno virtual :

   `python -m venv venv-`
   
   2.-Activa el entorno:

   `venv\Scripts\activate`

   3.-Instala las dependencias:

   `pip install -r requirements.txt`

   4.-Ejecuta el servidor:

   `python app.py`

   5.-Prueba en el navegador:
   - http://127.0.0.1:3000

   - http://127.0.0.1:3000/api/saludo

   - http://127.0.0.1:3000/api/estudiantes

   - http://127.0.0.1:3000//api/estudiantes/<id>

   - http://127.0.0.1:3000/api/estudiantes/carrera/<carrera>

## Enlaces de las Dependencias

Flask y Flask-CORS
- https://flask-cors.readthedocs.io/en/latest/
