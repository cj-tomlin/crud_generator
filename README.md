# CRUD App Generator

## Running the Generated FastAPI App

After generating your project (e.g., in `generated/MyGeneratedApp`):

```bash
cd generated/MyGeneratedApp
poetry run uvicorn main:app --reload
```

- The app will be available at http://127.0.0.1:8000
- Interactive API docs: http://127.0.0.1:8000/docs

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
