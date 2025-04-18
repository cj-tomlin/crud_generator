from crud_generator.generator import generate_project_structure, generate_model, generate_routes, generate_app, generate_database
import os
import yaml

from tests.utils import remove_if_exists

def setup_module(module):
    # Clean up generated test output before running
    test_out = 'generated/TestApp'
    remove_if_exists(test_out)

def test_generate_full_project():
    # Use the example config
    with open('examples/example_config.yaml') as f:
        config = yaml.safe_load(f)
    project_path = generate_project_structure('TestApp')
    generate_database(project_path, database_config=config.get('database'))
    generate_model(config, project_path)
    generate_routes(config, project_path)
    generate_app(config, project_path)
    # Check that key files exist
    assert os.path.exists(os.path.join(project_path, 'database.py'))
    assert os.path.exists(os.path.join(project_path, 'models', 'user.py'))
    assert os.path.exists(os.path.join(project_path, 'routes', 'user_routes.py'))
    assert os.path.exists(os.path.join(project_path, 'main.py'))

    # Clean up generated test files after test
    remove_if_exists(project_path)

def test_generate_postgres_project():
    with open('examples/postgres_config.yaml') as f:
        config = yaml.safe_load(f)
    project_path = generate_project_structure('TestAppPG')
    generate_database(project_path, database_config=config.get('database'))
    generate_model(config, project_path)
    generate_routes(config, project_path)
    generate_app(config, project_path)
    assert os.path.exists(os.path.join(project_path, 'database.py'))
    # Clean up
    remove_if_exists(project_path)

def test_generate_mysql_project():
    with open('examples/mysql_config.yaml') as f:
        config = yaml.safe_load(f)
    project_path = generate_project_structure('TestAppMySQL')
    generate_database(project_path, database_config=config.get('database'))
    generate_model(config, project_path)
    generate_routes(config, project_path)
    generate_app(config, project_path)
    assert os.path.exists(os.path.join(project_path, 'database.py'))
    # Clean up
    remove_if_exists(project_path)