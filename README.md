# Proyecto Final Integrador — Orders API

Servicio para la gestión de órdenes, desarrollado con Python, FastAPI y una arquitectura basada en separación de dominio, aplicación, infraestructura y API.

## 🔧 Tecnologías

* Python 3.12
* FastAPI
* SQLAlchemy
* Alembic
* SQLite
* Pydantic
* JWT
* Pytest
* Ruff
* MyPy
* Poetry
* Docker
* GitHub Actions
* pip-audit

## ✨ Arquitectura

El proyecto separa las responsabilidades en diferentes capas:

* **Domain:** con la entidad `Order` y sus reglas de negocio.
* **Application:** con los casos de uso y el puerto `OrderRepository`.
* **Infrastructure:** con SQLAlchemy, el modelo de persistencia y el adaptador del repositorio.
* **API:** con los endpoints FastAPI, esquemas Pydantic y autenticación meidante JWT.


## ☁️ API

### Health check

```http
GET /health
```

Respuesta:

```json
{
  "status": "ok"
}
```

### Autenticación

```http
POST /auth/login
```

Credenciales para demostración:

```text
username: admin
password: admin123
```

El endpoint devuelve un token JWT que debe utilizarse como `Bearer Token` para acceder a los endpoints de órdenes.

### Crear orden

```http
POST /orders
```

Requiere autenticación.

Ejemplo:

```json
{
  "customer_name": "Karla",
  "product": "Laptop",
  "quantity": 2,
  "unit_price": "1500.00"
}
```

### Consultar órdenes

```http
GET /orders
```

Requiere autenticación.

### Consultar una orden

```http
GET /orders/{order_id}
```

Requiere autenticación.

## 🛢️ Base de datos y migraciones

La aplicación utiliza SQLite y SQLAlchemy.

Las migraciones se gestionan mediante Alembic.

Ejecutar migraciones:

```bash
poetry run alembic upgrade head
```

Crear una nueva migración:

```bash
poetry run alembic revision --autogenerate -m "descripcion"
```

## 🔩 Ejecución local

Instalar dependencias:

```bash
poetry install
```

Ejecutar la aplicación:

```bash
poetry run uvicorn proyecto_final_integrador.main:app --reload
```

La documentación interactiva estará disponible en:

```text
http://127.0.0.1:8000/docs
```

## ✅ Pruebas y calidad

Ejecutar todas las pruebas:

```bash
poetry run pytest
```

Ejecutar pruebas con cobertura:

```bash
poetry run pytest --cov=proyecto_final_integrador --cov-report=term-missing
```

Resultado actual: **10 pruebas aprobadas y 91% de cobertura**.

Verificar lint:

```bash
poetry run ruff check src/ tests/
```

Verificar formato:

```bash
poetry run ruff format --check src/ tests/
```

Verificar tipado:

```bash
poetry run mypy src/
```

Auditar dependencias:

```bash
poetry run pip-audit
```

La auditoría actual no reporta vulnerabilidades conocidas en las dependencias auditables.

## 🐳 Docker

El proyecto incluye un `Dockerfile` multistage para separar la instalación de dependencias de la imagen final.

Construcción:

```bash
docker build -t orders-api .
```

Ejecución:

```bash
docker run -p 8000:8000 orders-api
```

> La construcción local de la imagen depende de que Docker Desktop tenga habilitada la virtualización/WSL 2.

## ♾️ CI/CD

El proyecto incluye un workflow de GitHub Actions en:

```text
.github/workflows/ci.yml
```

El pipeline ejecuta:

* Ruff
* Verificación de formato
* MyPy
* Pytest y cobertura
* pip-audit

## 🔼 Estructura principal

```text
proyecto_final_integrador/
├── .github/
│   └── workflows/
│       └── ci.yml
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
├── diagrams/
├── src/
│   └── proyecto_final_integrador/
│       ├── api/
│       ├── application/
│       ├── domain/
│       ├── infrastructure/
│       └── main.py
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── contract/
│   └── e2e/
├── .dockerignore
├── Dockerfile
├── alembic.ini
├── pyproject.toml
└── README.md
```

## 📝 Evidencia de pruebas

El proyecto incluye:

* **Pruebas unitarias:** dominio y casos de uso.
* **Pruebas de integración:** repositorio SQLAlchemy.
* **Pruebas de contrato:** estructura OpenAPI.
* **Pruebas E2E:** autenticación y flujo de creación/consulta de órdenes.

### Auditoría de dependencias:
![captura terminal](evidencias/auditoria_dependencias.png)
