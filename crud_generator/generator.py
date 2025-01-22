import os
from jinja2 import Environment, FileSystemLoader

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
