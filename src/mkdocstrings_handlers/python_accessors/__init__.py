"""Python handler for documenting accessors with mkdocstrings"""

import importlib.metadata

from .handler import PythonAccessorsHandler

__version__ = importlib.metadata.version("mkdocstrings_python_accessors")
__all__ = ["get_handler"]

get_handler = PythonAccessorsHandler
