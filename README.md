# Proyecto Final UNIR

Este proyecto es una aplicación web sencilla desarrollada con Flask, pensada como ejemplo para demostrar cómo crear un entorno local de desarrollo reproducible, con tests unitarios y una base de datos local.

El objetivo principal es que cualquier persona pueda:
- Clonar el repositorio
- Seguir unos pocos pasos
- Ejecutar la aplicación en local
- Ejecutar los tests y validar cambios sin miedo a romper nada

---

## Arquitectura del software

El proyecto sigue una arquitectura simple y común en aplicaciones Flask pequeñas, basada en el patrón **Application Factory**.

### Estructura del proyecto

```
ProyectoFinalUNIR/
├── app/
│   ├── __init__.py      # Creación de la aplicación Flask (create_app)
│   ├── config.py        # Configuración de la aplicación
│   ├── models.py        # Modelos de base de datos (SQLAlchemy)
│   └── routes.py        # Endpoints / rutas de la API
│
├── tests/
│   ├── conftest.py      # Fixtures de pytest (app y cliente de test)
│   └── test_data.py     # Tests unitarios de los endpoints
│
├── manage.py            # Inicialización de la base de datos
├── run.py               # Arranque de la aplicación en local
├── requirements.txt     # Dependencias necesarias para la aplicación
├── requirements-dev.txt # Dependencias de desarrollo y testing
└── README.md
```

### Flujo de la aplicación

1. `run.py` llama a `create_app()` para crear la aplicación Flask.
2. Flask carga la configuración desde `config.py`.
3. SQLAlchemy inicializa la base de datos usando los modelos definidos en `models.py`.
4. Las rutas definidas en `routes.py` exponen los endpoints de la API.

Este enfoque permite crear múltiples instancias de la aplicación (por ejemplo, para tests), sin depender de un servidor en ejecución.

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
python -m venv venv
```

En Windows:
```bash
venv\Scripts\activate
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

## Ejecución de la aplicación en local

### 1. Inicializar la base de datos

```bash
python manage.py
```

Este paso crea la base de datos local y las tablas necesarias.

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

Meter datos
```bash
Invoke-RestMethod `
 -Method Post `
 -Uri "http://127.0.0.1:5000/data" `
 -Body (@{name="Mi Nombre"} | ConvertTo-Json) `
 -ContentType "application/json"
```

Consultar los datos
```bash
Invoke-RestMethod `
-Method Get `
-Uri "http://127.0.0.1:5000/data"
```

Eliminar datos
```bash
Invoke-RestMethod `
-Method Delete `
-Uri "http://127.0.0.1:5000/data/1"
```

---

## Ejecución de tests

NOTA: Los tests no requieren que la aplicación esté arrancada.

Desde la raíz del proyecto:

```bash
pytest
```

Para ejecutar solo un fichero de tests:

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

## Normas de colaboración

- La rama `main` contiene siempre código estable.
- El desarrollo de nuevas funcionalidades debe hacerse en ramas independientes:
  - `feature/nombre-feature`
  - `fix/nombre-fix`
- Todo cambio debe ir acompañado de tests.
- Los tests deben pasar antes de integrar los cambios en `main`.