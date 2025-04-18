import pytest
from crud_generator.config_parser import parse_config

def test_parse_config():
    config = parse_config("examples/example_config.yaml")
    assert "models" in config
    assert len(config["models"]) > 0

    user_model = config["models"][0]
    assert user_model["name"] == "User"
    assert len(user_model["fields"]) == 3
    assert user_model["fields"][0]["type"] == "Integer"
    assert user_model["fields"][0]["primary_key"] == True

def test_parse_config_invalid_db(tmp_path):
    # Write a config missing 'url'
    config_path = tmp_path / "bad.yaml"
    config_path.write_text("database:\n  type: sqlite\n")
    with pytest.raises(ValueError, match="Invalid database config"):
        parse_config(str(config_path))

def test_parse_config_valid_alembic(tmp_path):
    config_path = tmp_path / "valid_alembic.yaml"
    config_path.write_text("""
database:
  type: sqlite
  url: sqlite:///./test.db
alembic: true
""")
    config = parse_config(str(config_path))
    assert config["alembic"] is True

def test_parse_config_invalid_alembic(tmp_path):
    config_path = tmp_path / "invalid_alembic.yaml"
    config_path.write_text("""
database:
  type: sqlite
  url: sqlite:///./test.db
alembic: "yes"
""")
    with pytest.raises(ValueError, match="Invalid config: 'alembic' must be a boolean"):
        parse_config(str(config_path))

def test_parse_config_alembic_omitted(tmp_path):
    config_path = tmp_path / "no_alembic.yaml"
    config_path.write_text("""
database:
  type: sqlite
  url: sqlite:///./test.db
""")
    config = parse_config(str(config_path))
    assert "alembic" not in config
