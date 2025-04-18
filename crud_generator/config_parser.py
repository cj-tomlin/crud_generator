import yaml
from typing import List, Dict, Any

from .config_schema import validate_database_config, ConfigValidationError

def parse_config(file_path: str) -> Dict[str, Any]:
    with open(file_path, "r") as f:
        config = yaml.safe_load(f)
    # Validate database config if present
    if "database" in config:
        try:
            validate_database_config(config["database"])
        except ConfigValidationError as e:
            raise ValueError(f"Invalid database config: {e}")
    return config
