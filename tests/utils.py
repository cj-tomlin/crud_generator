import shutil
from pathlib import Path

def remove_if_exists(path):
    """
    Remove a file or directory if it exists.
    Args:
        path (str or Path): The path to remove.
    """
    path = Path(path)
    if path.is_dir():
        shutil.rmtree(path)
    elif path.is_file():
        path.unlink()
