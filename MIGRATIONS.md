# Database Migrations with Alembic

This project uses [Alembic](https://alembic.sqlalchemy.org/) for managing database schema migrations.

## Setup

Alembic is already configured in the project. The configuration is in:
- `alembic.ini` — main Alembic configuration
- `alembic/env.py` — environment setup (database connection, auto-detection of models)
- `alembic/versions/` — auto-generated migration scripts

Database connection details are read from environment variables:
- `DB_HOST`
- `DB_PORT`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`

If these are not set, Alembic defaults to SQLite (`sqlite:///./test.db`) for local development.

## Common Commands

### Create a new migration (auto-detect schema changes)

```bash
python -m alembic revision --autogenerate -m "description of change"
```

Example:
```bash
python -m alembic revision --autogenerate -m "add email column to cars"
```

Alembic will:
1. Compare the current database schema with your SQLAlchemy models (in `car/car_model.py`).
2. Generate a new migration file in `alembic/versions/`.
3. You should review the generated file for accuracy before applying it.

### Apply migrations to the database (upgrade)

```bash
python -m alembic upgrade head
```

This applies all pending migrations to bring the database up to date.

### Rollback the last migration (downgrade)

```bash
python -m alembic downgrade -1
```

This reverts the database to the previous state. You can also use specific revision IDs:
```bash
python -m alembic downgrade <revision_id>
```

### View current migration status

```bash
python -m alembic current
```

Shows which revision the database is currently at.

### View migration history

```bash
python -m alembic history --oneline
```

Lists all migrations in order.

## Using Migrations in Docker

If you run the app in Docker (via `docker compose`), add a migration step to your `docker-entrypoint.sh` or CI/CD pipeline to ensure the database is up-to-date before the app starts:

```bash
python -m alembic upgrade head
uvicorn main:app --host 0.0.0.0
```

Example `docker-entrypoint.sh`:
```bash
#!/bin/bash
set -e

# Run migrations
echo "Running database migrations..."
python -m alembic upgrade head

# Start the app
echo "Starting the application..."
exec uvicorn main:app --host 0.0.0.0 --port 8000
```

Then in your `Dockerfile`, use:
```dockerfile
ENTRYPOINT ["/app/docker-entrypoint.sh"]
```

## Adding a New Column (Example)

1. Edit `car/car_model.py` and add a new field to `CarModel`:
   ```python
   color: Mapped[str] = mapped_column()
   fuel_type: Mapped[str] = mapped_column(default="gasoline")  # NEW
   ```

2. Generate a migration:
   ```bash
   python -m alembic revision --autogenerate -m "add fuel_type column to cars"
   ```

3. Review the generated migration file in `alembic/versions/`.

4. Apply the migration:
   ```bash
   python -m alembic upgrade head
   ```

5. Update your Pydantic schemas in `car/car_interfaces.py` if needed to match.

## Important Notes

- **Always review auto-generated migrations** before applying them. Alembic is smart but not perfect.
- **Commit migration files to version control** (`alembic/versions/*.py`). Never generate migrations on-the-fly in production.
- **Test migrations locally** before deploying to production.
- If using PostgreSQL, set all `DB_*` environment variables. If testing locally with SQLite, migrations work out-of-the-box.

## Troubleshooting

### "Could not parse SQLAlchemy URL from given URL string"
Ensure all `DB_*` environment variables are set, or leave them unset to use SQLite.

### "No changes detected in table/column definitions"
This means Alembic doesn't see any schema differences. Common causes:
- You haven't modified any SQLAlchemy models.
- Models aren't properly imported in `alembic/env.py` (check the `from car.car_model import Base` line).

### Migration fails with "table 'cars' already exists"
This usually means the migration was already applied. Check the current revision:
```bash
python -m alembic current
```

---

For more details, see the [Alembic documentation](https://alembic.sqlalchemy.org/).
