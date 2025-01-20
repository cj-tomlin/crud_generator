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
