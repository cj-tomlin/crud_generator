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
