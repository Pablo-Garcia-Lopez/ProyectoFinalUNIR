# Proyecto Final UNIR

Este proyecto es una aplicación web sencilla desarrollada con Flask, pensada como ejemplo para demostrar cómo crear un entorno local de desarrollo reproducible, con tests unitarios y una base de datos local.

Objetivos principales:
- Clonar el repositorio y arrancar la app localmente
- Ejecutar tests y comprobar cobertura
- Entender cómo configurar la base de datos en diferentes entornos

---

## Estructura del proyecto

```
ProyectoFinalUNIR/
├── app/
│   ├── __init__.py      # Creación de la aplicación Flask (create_app)
│   ├── config.py        # Configuración por entornos (dev/testing/prod)
│   ├── models.py        # Modelos de base de datos (SQLAlchemy)
│   └── routes.py        # Endpoints / rutas de la API
│
├── tests/
│   ├── conftest.py      # Fixtures de pytest (app y cliente de test)
│   └── test_data.py     # Tests de los endpoints
│
├── manage.py            # Inicialización de la base de datos (dev)
├── run.py               # Arranque de la aplicación en local
├── user_app.py          # Cliente CLI para probar la API
├── requirements.txt     # Dependencias de la aplicación
├── requirements-dev.txt # Dependencias para desarrollo y testing
└── README.md
```

### Flujo de la aplicación

1. `run.py` llama a `create_app()` para crear la aplicación Flask.
2. Flask carga la configuración desde `config.py`.
3. SQLAlchemy inicializa la base de datos usando los modelos definidos en `models.py`.
4. Las rutas definidas en `routes.py` exponen los endpoints de la API.

---

## Requisitos previos

- Python 3.9 o superior
- Git

No es necesario tener ninguna base de datos externa instalada.

---

## Entorno local de desarrollo

### 1. Clonar el repositorio

```bash
git clone https://github.com/Pablo-Garcia-Lopez/ProyectoFinalUNIR.git
cd ProyectoFinalUNIR
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv .venv
```

En Windows:
Si te da problemas para inicializar el venv, usa:
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
```
Para permitir en ese terminal la activación del entorno virtual. Luego usa:
```bash
.venv\Scripts\activate
```

En Linux / macOS:
```bash
source venv/bin/activate
```

### 3. Instalar dependencias

Para desarrollo y tests:

```bash
pip install -r requirements-dev.txt
```

---

## Variables de entorno / Configuración

- En desarrollo la app usa por defecto SQLite (`sqlite:///data.db`).
- Para producción la aplicación espera que `DATABASE_URI` esté definida y apunte a una base de datos adecuada


### 1. Inicializar la base de datos

```bash
python manage.py
```

Esto creará la base de datos local (por defecto `data.db`) y añadirá un registro de ejemplo.

---

### 2. Arrancar la aplicación

```bash
python run.py
```

La aplicación quedará disponible en:

```
http://127.0.0.1:5000
```

---

## Probar funcionalidades

- Con CLI (cliente incluido):
```bash
python user_app.py
```

## Probar funcionalidades (manualmente)

POST (añadir):
```bash
Invoke-RestMethod `
 -Method Post `
 -Uri "http://127.0.0.1:5000/data" `
 -Body (@{name="Mi Nombre"} | ConvertTo-Json) `
 -ContentType "application/json"
```

GET (listar):
```bash
Invoke-RestMethod `
-Method Get `
-Uri "http://127.0.0.1:5000/data"
```

DELETE (borrar por id):
```bash
Invoke-RestMethod `
-Method Delete `
-Uri "http://127.0.0.1:5000/data/1"
```

PUT (modificar datos por id)
```bash
Invoke-RestMethod `
-Method Put `
-Uri "http://127.0.0.1:5000/data/1" `
-Body (@{ name = "Nombre actualizado" } | ConvertTo-Json) `
-ContentType "application/json"
```

---

## Ejecución de tests

NOTA: Los tests no requieren que la aplicación esté arrancada.

Activar el venv y ejecutar:

```bash
pytest (o pytest -s para ver los prints)
```

Para ejecutar un fichero concreto:

```bash
pytest tests/test_data.py
```

---

## Cobertura de código

El proyecto utiliza `pytest-cov` para medir la cobertura de tests.

Para obtener un informe de cobertura:

```bash
pytest --cov=app
```

---

## Colaboración

- La rama `main` contiene el código estable.
- Desarrolla nuevas funcionalidades en ramas tipo:
  - `feature/nombre-feature`
  - `fix/nombre-fix`
- Acompaña los cambios con tests. Los tests deben pasar antes de integrar en `main`.
