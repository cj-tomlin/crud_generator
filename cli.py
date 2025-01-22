import argparse
from crud_generator.config_parser import parse_config
from crud_generator.generator import (
    generate_project_structure,
    generate_model,
    generate_routes,
    generate_app,
)

def main():
    parser = argparse.ArgumentParser(description="CRUD Generator CLI")
    parser.add_argument(
        "config_path",
        type=str,
        help="Path to the configuration file (YAML format)"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="generated",
        help="Directory to save the generated project"
    )

    args = parser.parse_args()

    # Parse the configuration file
    print(f"Parsing configuration file: {args.config_path}")
    config = parse_config(args.config_path)

    # Get the project name
    project_name = config.get("project_name", "GeneratedProject")

    # Create the project structure
    project_path = generate_project_structure(project_name, output_dir=args.output_dir)

    # Generate the models, routes, and FastAPI app
    generate_model(config, project_path)
    generate_routes(config, project_path)
    generate_app(config, project_path)

    print(f"Project '{project_name}' generated successfully in {args.output_dir}")


if __name__ == "__main__":
    main()
