import os
from jinja2 import Environment, FileSystemLoader

def scaffold_alembic(project_path, database_config):
    """
    Scaffold Alembic migration environment in the generated project.
    """
    env = Environment(loader=FileSystemLoader("crud_generator/templates"))
    # alembic.ini
    alembic_ini_template = env.get_template("alembic.ini.j2")
    rendered_ini = alembic_ini_template.render(database=database_config)
    with open(os.path.join(project_path, "alembic.ini"), "w") as f:
        f.write(rendered_ini)
    # alembic/env.py
    os.makedirs(os.path.join(project_path, "alembic"), exist_ok=True)
    alembic_env_template = env.get_template("alembic_env.py.j2")
    rendered_env = alembic_env_template.render()
    with open(os.path.join(project_path, "alembic", "env.py"), "w") as f:
        f.write(rendered_env)
    # alembic/versions/.gitkeep
    versions_dir = os.path.join(project_path, "alembic", "versions")
    os.makedirs(versions_dir, exist_ok=True)
    gitkeep_template = env.get_template("alembic_versions_gitkeep.j2")
    with open(os.path.join(versions_dir, ".gitkeep"), "w") as f:
        f.write(gitkeep_template.render())
    # alembic/README.md
    alembic_readme_template = env.get_template("alembic_readme.md.j2")
    rendered_readme = alembic_readme_template.render()
    with open(os.path.join(project_path, "alembic", "README.md"), "w") as f:
        f.write(rendered_readme)
    print(f"Scaffolded Alembic migration environment in: {project_path}")

def generate_project_structure(project_name, output_dir="generated"):
    """
    Create the project structure inside the generated directory.
    """
    project_path = os.path.join(output_dir, project_name)
    os.makedirs(project_path, exist_ok=True)
    os.makedirs(os.path.join(project_path, "routes"), exist_ok=True)
    os.makedirs(os.path.join(project_path, "models"), exist_ok=True)
    return project_path

def generate_model(config, project_path):
    """
    Generate SQLAlchemy models from the given configuration.
    """
    env = Environment(loader=FileSystemLoader("crud_generator/templates"))
    model_template = env.get_template("model.py.j2")

    models_path = os.path.join(project_path, "models")
    for model in config["models"]:
        rendered_model = model_template.render(model=model)
        file_path = os.path.join(models_path, f"{model['name'].lower()}.py")
        with open(file_path, "w") as f:
            f.write(rendered_model)
        print(f"Generated model: {file_path}")

def generate_routes(config, project_path):
    """
    Generate FastAPI route files for each model.
    """
    env = Environment(loader=FileSystemLoader("crud_generator/templates"))
    route_template = env.get_template("crud_routes.py.j2")

    routes_path = os.path.join(project_path, "routes")
    for endpoint in config["endpoints"]:
        rendered_route = route_template.render(
            model_name=endpoint["model"], methods=endpoint["methods"]
        )
        route_file_path = os.path.join(routes_path, f"{endpoint['model'].lower()}_routes.py")
        with open(route_file_path, "w") as f:
            f.write(rendered_route)
        print(f"Generated route: {route_file_path}")

def generate_database(project_path, database_config=None):
    """
    Generate database.py for SQLAlchemy engine and session management.
    """
    env = Environment(loader=FileSystemLoader("crud_generator/templates"))
    db_template = env.get_template("database.py.j2")
    # Use provided config, or default to SQLite if missing
    if database_config is None:
        database_config = {
            "type": "sqlite",
            "url": "sqlite:///./app.db",
            "connect_args": {"check_same_thread": False},
            "echo": False,
        }
    rendered_db = db_template.render(database=database_config)
    db_file_path = os.path.join(project_path, "database.py")
    with open(db_file_path, "w") as f:
        f.write(rendered_db)
    print(f"Generated database: {db_file_path}")

def generate_app(config, project_path):
    """
    Generate the main FastAPI app entry point.
    """
    env = Environment(loader=FileSystemLoader("crud_generator/templates"))
    main_template = env.get_template("main.py.j2")

    rendered_main = main_template.render(config=config)
    app_file_path = os.path.join(project_path, "main.py")

    with open(app_file_path, "w") as f:
        f.write(rendered_main)
    print(f"Generated main app: {app_file_path}")
