# Laboratorio_4<br>
Estas son las instrucciones para la instalación y la ejecución del servidor:

## Instrucciones<br>
1. Ejecutar el comando pip install -r requirements.txt
2. Ejecutar el comando uvicorn main:app --reload

## Rutas del API<br>
### Servidor local
- Ruta para predicción: 127.0.0.1:8000/predict
- Ruta para fit: 127.0.0.1:8000/fit
- Puede también usar la interfaz de FastAPI para realizar las peticiones: 127.0.0.1:8000/docs
### Servidor On-Cloud (Bono)
- Ruta para predicción: http://34.72.86.170/predict
- Ruta para fit: http://34.72.86.170/fit
- Puede también usar la interfaz de FastAPI para realizar las peticiones: http://34.72.86.170/docs
