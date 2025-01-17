"""
Implementation of python_accessors handler
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import griffe
from mkdocstrings.loggers import get_logger
from mkdocstrings_handlers.python_xref.handler import PythonRelXRefHandler

__all__ = ["PythonAccessorsHandler"]

logger = get_logger(__name__)


class PythonAccessorsHandler(PythonRelXRefHandler):
    """
    Extended version of mkdocstrings PythonRelXRefHandler handler

    Converts accessors into the namespace of the user's choosing.

    Could also be done with the standard Python handler I expect,
    but that's not what the project I'm working on needs.
    """

    def render(self, data: griffe.Object, config: Mapping[str, Any]) -> str:
        """
        Render the docs

        Parameters
        ----------
        data
            Data to render

        config
            Configuration

        Returns
        -------
        :
            Rendered docs
        """
        if not isinstance(data, griffe.Class):
            raise NotImplementedError(data)

        try:
            namespace = config["namespace"]
        except KeyError:
            msg = f"Please specify the namespace to use with {data.name}. {data.path=}"
            raise KeyError(msg)

        # Set overall name
        data.name = namespace

        # Then update names for individual members
        member_keys = list(data.members.keys())
        for name in member_keys:
            if name.startswith("_"):
                # Don't document hidden methods etc.
                # Could make this configuration instead
                # if real customisation was needed.
                data.del_member(name)
                continue

            data.members[name].name = f"{namespace}.{name}"

        return super().render(data, config)
