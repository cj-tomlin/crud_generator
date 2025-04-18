# CRUD App Generator

## Running the Generated FastAPI App

After generating your project (e.g., in `generated/MyGeneratedApp`):

```bash
cd generated/MyGeneratedApp
poetry run uvicorn main:app --reload
```

- The app will be available at http://127.0.0.1:8000
- Interactive API docs: http://127.0.0.1:8000/docs

## Database Configuration Examples

The generator supports SQLite, PostgreSQL, and MySQL. Specify your database settings in the config YAML:

### SQLite (default)
```yaml
# examples/example_config.yaml

# ... other config ...
database:
  type: sqlite
  url: sqlite:///./app.db
  connect_args:
    check_same_thread: false
  echo: false
```

### PostgreSQL
```yaml
# examples/postgres_config.yaml
database:
  type: postgresql
  url: postgresql://user:password@localhost:5432/mydb
  connect_args:
    sslmode: disable
  echo: true
```

### MySQL
```yaml
# examples/mysql_config.yaml
database:
  type: mysql
  url: mysql://user:password@localhost:3306/mydb
  connect_args:
    charset: utf8mb4
  echo: false
```

**Fields:**
- `type`: One of `sqlite`, `postgresql`, or `mysql` (required)
- `url`: SQLAlchemy DB URL (required)
- `connect_args`: Dictionary of connection options (optional)
- `echo`: Set SQLAlchemy engine echo (optional, boolean)

## Running the Generator CLI

From the project root:

```bash
poetry run python cli.py examples/example_config.yaml
```

You can specify a different config or output directory as needed.

## Running Tests

If you have tests in your generated or source project:

```bash
poetry run pytest --cov=crud_generator
```

Or, to run tests in the generated app (if tests/ exists):

```bash
cd generated/MyGeneratedApp
poetry run pytest
```
