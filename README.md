
# fastapi-demo

This is a small Python showcase project demonstrating a FastAPI application using SQLAlchemy for data access. It includes a minimal project structure to get you started with building REST APIs backed by a database.

**Quick start**

- **Run (development):** `uvicorn main:app --reload`

**Requirements**

- Python 3.10+ recommended
- `fastapi`, `uvicorn`, `sqlalchemy`, and optionally `alembic` for migrations

You can install the minimal dependencies with:

```bash
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn sqlalchemy
```

If you plan to use Alembic for migrations:

```bash
pip install alembic
```

**Run the app**

Start the development server with:

```bash
uvicorn main:app --reload
```

Open a browser to `http://127.0.0.1:8000/docs` to see the interactive OpenAPI (Swagger) docs.

**Project structure**

- `main.py` - FastAPI app entrypoint (where `app` is defined)
- `car/` - a small example domain module
	- `car_model.py` - SQLAlchemy models (entities)
	- `car_service.py` - business logic / service layer
	- `car_controller.py` - FastAPI routes / controllers
- `utils/` - helper utilities

Example tree:

```
main.py
car/
	car_controller.py
	car_model.py
	car_service.py
utils/
README.md
```

**Example API usage**

Assuming the project exposes a `cars` resource, here are sample requests.

- List cars (GET):

```bash
curl http://127.0.0.1:8000/cars
```

- Create a car (POST):

```bash
curl -X POST http://127.0.0.1:8000/cars \
	-H "Content-Type: application/json" \
	-d '{"make":"Toyota","model":"Corolla","year":2020}'
```

Adjust endpoints to match the actual routes implemented in `car/car_controller.py`.

**Database**

This project uses SQLAlchemy for ORM. For a simple development setup you can use SQLite (file or in-memory). If you use a different RDBMS (Postgres, MySQL), update the connection URL accordingly in your DB setup code.

**Development notes**

- Keep business logic in `car_service.py` and keep `car_controller.py` minimal (only request/response handling).
- Use Pydantic models for request validation and response schemas.

**Next steps / enhancements**

- Add `requirements.txt` or `pyproject.toml` for reproducible installs.
- Add Alembic for migrations if using a persistent DB.
- Add tests (pytest) and a CI workflow.

If you'd like, I can:

- generate a `requirements.txt` for you,
- add a minimal DB config (SQLite) and connection helper in `utils/`, or
- scaffold Pydantic schemas and example endpoints inside `car_controller.py`.

---
Generated for a FastAPI + SQLAlchemy showcase project. Run `uvicorn main:app --reload` to start.
