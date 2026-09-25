1. create a project directory and navigate into it:
   ```bash
   mkdir fastapi_project
   cd fastapi_project
   ```

2. init uv:
    ```bash
    uv init
    ```

3. virtual env setup
   ```bash
   # create a virtual env
   uv venv .venv

   # activate venv
   source uv/bin/activate
   ```

4. install FastAPI and Uvicorn:
   ```bash
   uv add fastapi uvicorn
   ```

5. create a main.py file and add the following code:
   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def home():
       return "Homepage"
   ```

6. run the application:
   ```bash
   uv run uvicorn src.main:app --reload
   ```


# FastAPI docs

```bash
# Swagger UI
http://127.0.0.1:8000/docs

# ReDoc
http://127.0.0.1:8000/redoc

# OpenAPI Schema
http://127.0.0.1:8000/openapi.json
```

> Note: you can customize swagger `/docs` to any specific url i.e., `/documentation` by setting `FastAPI(docs_url="/documentation)"` and now url will be `http://127.0.0.1:8000/documentation`. You can also update `redoc` by adding parameter in `FastAPI` class `redoc_url`.


# Folder Structure

```txt
project/
├── pyproject.toml         # Dependencies & uv config (package = false)
├── uv.lock
├── .env                   # Environment variables
├── README.md
└── src/
    ├── __init__.py
    ├── main.py            # Entrypoint: initializes FastAPI & mounts routers
    │
    ├── core/              # Global configuration & security
    │   ├── __init__.py
    │   ├── config.py      # App settings (Pydantic BaseSettings, reads .env)
    │   └── security.py    # Password hashing, JWT token handling
    │
    ├── api/               # API endpoints (equivalent to Express routes)
    │   ├── __init__.py
    │   ├── deps.py        # Shared route dependencies (e.g., get_db, auth)
    │   └── v1/
    │       ├── __init__.py
    │       ├── router.py  # Consolidates all v1 sub-routers
    │       └── endpoints/
    │           ├── __init__.py
    │           ├── auth.py
    │           └── products.py
    │
    ├── models/            # Database ORM models (SQLAlchemy / SQLModel)
    │   ├── __init__.py
    │   └── product.py
    │
    ├── schemas/           # Pydantic schemas (Request & Response validation)
    │   ├── __init__.py
    │   └── product.py
    │
    ├── services/          # Business logic (equivalent to controllers / services)
    │   ├── __init__.py
    │   └── product_service.py
    │
    ├── middlewares/       # Custom ASGI / Starlette middlewares
    │   ├── __init__.py
    │   └── logging.py
    │
    └── utils/             # Helper functions & utilities
        ├── __init__.py
        └── helpers.py
```