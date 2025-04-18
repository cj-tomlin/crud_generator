import pytest
from crud_generator.config_schema import validate_database_config, ConfigValidationError

def test_missing_type():
    cfg = {"url": "sqlite:///./app.db"}
    with pytest.raises(ConfigValidationError, match="Missing required database config field: 'type'"):
        validate_database_config(cfg)

def test_missing_url():
    cfg = {"type": "sqlite"}
    with pytest.raises(ConfigValidationError, match="Missing required database config field: 'url'"):
        validate_database_config(cfg)

def test_unsupported_type():
    cfg = {"type": "oracle", "url": "oracle://user:pass@host/db"}
    with pytest.raises(ConfigValidationError, match="Unsupported database type"):
        validate_database_config(cfg)

def test_invalid_sqlite_url():
    cfg = {"type": "sqlite", "url": "sqlite://wrong"}
    with pytest.raises(ConfigValidationError, match="Invalid URL for sqlite"):
        validate_database_config(cfg)

def test_valid_postgres_without_user_pass():
    cfg = {"type": "postgresql", "url": "postgresql://host/db"}
    validate_database_config(cfg)  # Should not raise

def test_connect_args_not_dict():
    cfg = {"type": "sqlite", "url": "sqlite:///./app.db", "connect_args": "not_a_dict"}
    with pytest.raises(ConfigValidationError, match="connect_args.*dictionary"):
        validate_database_config(cfg)

def test_echo_not_bool():
    cfg = {"type": "sqlite", "url": "sqlite:///./app.db", "echo": "yes"}
    with pytest.raises(ConfigValidationError, match="echo.*boolean"):
        validate_database_config(cfg)

def test_valid_sqlite():
    cfg = {"type": "sqlite", "url": "sqlite:///./app.db"}
    validate_database_config(cfg)  # Should not raise

def test_valid_postgres():
    cfg = {"type": "postgresql", "url": "postgresql://user:pass@localhost:5432/db"}
    validate_database_config(cfg)  # Should not raise
