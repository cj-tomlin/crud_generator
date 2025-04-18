from typing import Any, Dict

class ConfigValidationError(Exception):
    pass

import re

def validate_database_config(database: Dict[str, Any]):
    """
    Validate the database config section. Raise ConfigValidationError if invalid.
    """
    required_fields = ["type", "url"]
    for field in required_fields:
        if field not in database or not database[field]:
            raise ConfigValidationError(f"Missing required database config field: '{field}'")
    supported_types = {"sqlite", "postgresql", "mysql"}
    db_type = database["type"]
    if db_type not in supported_types:
        raise ConfigValidationError(f"Unsupported database type: {db_type}. Supported types: {supported_types}")
    url = database["url"]
    # Basic URL regex checks by type
    url_patterns = {
        "sqlite": r"^sqlite:\/\/\/[^\s]+$",
        "postgresql": r"^postgresql:\/\/(.+:.+@)?[\w\-\.]+(:\d+)?\/.+$",
        "mysql": r"^mysql:\/\/(.+:.+@)?[\w\-\.]+(:\d+)?\/.+$",
    }
    if not re.match(url_patterns[db_type], url):
        raise ConfigValidationError(
            f"Invalid URL for {db_type}: '{url}'. Example: '{db_type}://user:pass@host/db'"
        )
    # connect_args should be a dict if present
    connect_args = database.get("connect_args")
    if connect_args is not None and not isinstance(connect_args, dict):
        raise ConfigValidationError("'connect_args' must be a dictionary if provided.")
    # echo should be a boolean if present
    echo = database.get("echo")
    if echo is not None and not isinstance(echo, bool):
        raise ConfigValidationError("'echo' must be a boolean if provided.")

# Validate alembic field at the top-level config
def validate_alembic_field(config: Dict[str, Any]):
    alembic = config.get("alembic")
    if alembic is not None and not isinstance(alembic, bool):
        raise ConfigValidationError("'alembic' must be a boolean if provided at the root level.")

