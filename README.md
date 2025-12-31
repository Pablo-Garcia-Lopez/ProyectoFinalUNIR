# ProyectoFinalUNIR

# COSAS QUE AÑADIR:
- Que reajuste las id al borrar algún dato (si hay 4, al borrar el id 1 tendría que haber 1-2-3, no 2-3-4)
- Que al borrar puedas pedirle que te muestre la lista de datos(?)
- Meter más funcionalidades, como editar (posiblemente mediante id)

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

# HACER PRUEBAS CON LA BASE DE DATOS MANUALMENTE
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

# CORRER LOS TESTS
Sin necesidad de arrancar venv ni la aplicación, hacer:
pytest -s tests/nombre_prueba.py (de momento solo está test_data.py)

# PARA AÑADIR NUEVAS FUNCIONALIDADES
Añadirlas al archivo routes.py y añadir instrucciones a la sección "Hacer pruebas con la base de datos manualmente"

# PARA AÑADIR NUEVOS TESTS
Añadirlos al archivo "test_data.py" o crear un fichero nuevo de ser necesario

# PYTEST-COV
Herramienta de asistencia para comprobar la cobertura del código en los tests.
En este proyecto se exige que al menos el 80% del código esté cubierto en los tests.
Con Pytest-cov (incluido en requirements-dev.txt) se puede comprobar el porcentaje de esto
Si se quiere comprobar, se puede ejecutar el siguiente comando dentro de venv:
pytest --cov=app (Para medir solo la aplicación)
pytest --cov (para medir todo el código)