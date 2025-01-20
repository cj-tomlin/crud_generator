import yaml
from typing import List, Dict, Any

def parse_config(file_path: str) -> Dict[str, Any]:
    with open(file_path, "r") as f:
        config = yaml.safe_load(f)
    return config
