# Laboratorio_4<br>
Estas son las instrucciones para la instalación y la ejecución del servidor:

## Instrucciones<br>
1. Ejecutar el comando pip install -r requirements.txt
2. Ejecutar el comando uvicorn main:app --reload

## Rutas del API<br>
### Servidor local
- Ruta para predicción: http://127.0.0.1:8000/predict
- Ruta para fit: http://127.0.0.1:8000/fit
- Puede también usar la interfaz de FastAPI para realizar las peticiones: 127.0.0.1:8000/docs
- Si desea realizar pruebas de dconsumo desde postman puede utilizar la collection \assets\pruebaslaboratorio4.postman_collection.json con el environment assets\Lab4localhost.postman_environment.json, en esta collection encuentra pruebas de post correctas para usar el endpoint de predcción y una prueba de post para el endpoint de reentrenamiento.

### Servidor On-Cloud (Bono)
- Ruta para predicción: http://34.72.86.170/predict
- Ruta para fit: http://34.72.86.170/fit
- Puede también usar la interfaz de FastAPI para realizar las peticiones: http://34.72.86.170/docs
- Si desea realizar pruebas desde postman puede utilizar la collection \assets\pruebaslaboratorio4.postman_collection.json con el environment assets\Lab4servidor.postman_environment.json, en esta collection encuentra pruebas de post correctas para usar el endpoint de predcción y una prueba de post para el endpoint de reentrenamiento.