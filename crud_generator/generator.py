import os
from jinja2 import Environment, FileSystemLoader

def generate_model(config, output_dir="generated"):
    """
    Generate SQLAlchemy models from the given configuration.

    Args:
        config (dict): The parsed configuration file.
        output_dir (str): The directory where generated files will be saved.
    """
    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader("crud_generator/templates"))
    template = env.get_template("model.py.j2")

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Generate a model file for each model in the configuration
    for model in config["models"]:
        rendered_code = template.render(model=model)
        file_path = os.path.join(output_dir, f"{model['name'].lower()}.py")

        # Write the rendered code to a file
        with open(file_path, "w") as f:
            f.write(rendered_code)
        print(f"Generated: {file_path}")
