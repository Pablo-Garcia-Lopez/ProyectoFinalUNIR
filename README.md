# ProyectoFinalUNIR

# COSAS QUE AÑADIR:
- Que reajuste las id al borrar algún dato (si hay 4, al borrar el id 1 tendría que haber 1-2-3, no 2-3-4)
- Que al borrar puedas pedirle que te muestre la lista de datos(?)
- Meter tests (pytest)
- Meter más funcionalidades, como editar (posiblemente mediante id)

- Empezar a explicar el funcionamiento del programa para arrancarlo y empezar a meter/sacar/consultar datos. También para hacer los tests.

# PASOS PARA ARRANCAR LA APLICACIÓN
- Crear el entorno virtual (en caso de que no lo tengas creado)
python -m venv venv

- Activar el entorno virtual en Windows
venv\Scripts\activate

- Instalar los requisitos
pip install -r requirements.txt
pip install -r requirements-dev.txt

- Crear la base de datos y añadir el registro de ejemplo
python manage.py

- Arrancar el servidor en http://0.0.0.0:5000
python run.py

# HACER PRUEBAS CON LA BASE DE DATOS
- Meter datos
Invoke-RestMethod `
 -Method Post `
 -Uri "http://127.0.0.1:5000/data" `
 -Body (@{name="Mi Nombre"} | ConvertTo-Json) `
 -ContentType "application/json"

- Consultar los datos
Invoke-RestMethod `
-Method Get `
-Uri "http://127.0.0.1:5000/data"

- Eliminar datos
Invoke-RestMethod `
-Method Delete `
-Uri "http://127.0.0.1:5000/data/1"