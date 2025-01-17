"""Python handler for documenting accessors with mkdocstrings"""

from .handler import PythonAccessorsHandler

__all__ = ["get_handler"]

get_handler = PythonAccessorsHandler
