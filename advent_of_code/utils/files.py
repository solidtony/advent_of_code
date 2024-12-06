from os import path
from pathlib import Path

def get_python_file_directory(module_path:str) -> Path:
    """Returns the directory of the python file that function is called from.

    Example: get_python_file_directory(__file__)
    """
    return Path(path.dirname(module_path))

def get_default_input_path(module_path) -> Path:
    """Returns the default input path.

    Example: get_default_input_path(__file__)
    """
    return Path(path.join(get_python_file_directory(module_path), 'input.txt'))
