import argparse
from crud_generator.config_parser import parse_config
from crud_generator.generator import generate_model


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
        help="Directory to save the generated models"
    )

    args = parser.parse_args()

    # Parse the configuration file
    print(f"Parsing configuration file: {args.config_path}")
    config = parse_config(args.config_path)

    # Generate the models
    print(f"Generating models in directory: {args.output_dir}")
    generate_model(config, output_dir=args.output_dir)
    print("Model generation complete.")


if __name__ == "__main__":
    main()
