<!--- --8<-- [start:description] -->
# mkdocstrings-python-accessors

Support for documenting accessors with mkdocstrings.

**Key info :**
[![Main branch: supported Python versions](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fclimate-resource%2Fmkdocstrings-python-accessors%2Fmain%2Fpyproject.toml)](https://github.com/climate-resource/mkdocstrings-python-accessors/blob/main/pyproject.toml)
[![Licence](https://img.shields.io/pypi/l/mkdocstrings-python-accessors?label=licence)](https://github.com/climate-resource/mkdocstrings-python-accessors/blob/main/LICENCE)

**PyPI :**
[![PyPI](https://img.shields.io/pypi/v/mkdocstrings-python-accessors.svg)](https://pypi.org/project/mkdocstrings-python-accessors/)

**Tests :**
[![CI](https://github.com/climate-resource/mkdocstrings-python-accessors/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/climate-resource/mkdocstrings-python-accessors/actions/workflows/ci.yaml)
[![Coverage](https://codecov.io/gh/climate-resource/mkdocstrings-python-accessors/branch/main/graph/badge.svg)](https://codecov.io/gh/climate-resource/mkdocstrings-python-accessors)

**Other info :**
[![Last Commit](https://img.shields.io/github/last-commit/climate-resource/mkdocstrings-python-accessors.svg)](https://github.com/climate-resource/mkdocstrings-python-accessors/commits/main)
[![Contributors](https://img.shields.io/github/contributors/climate-resource/mkdocstrings-python-accessors.svg)](https://github.com/climate-resource/mkdocstrings-python-accessors/graphs/contributors)
## Status

<!---

We recommend having a status line in your repo
to tell anyone who stumbles on your repository where you're up to.
Some suggested options:

- prototype: the project is just starting up and the code is all prototype
- development: the project is actively being worked on
- finished: the project has achieved what it wanted
  and is no longer being worked on, we won't reply to any issues
- dormant: the project is no longer worked on
  but we might come back to it,
  if you have questions, feel free to raise an issue
- abandoned: this project is no longer worked on
  and we won't reply to any issues
-->

- development: the project is actively being worked on

<!--- --8<-- [end:description] -->

## Installation

<!--- --8<-- [start:installation] -->

The latest version of mkdocstrings-python-accessors can be installed with

=== "pip"
    ```sh
    pip install mkdocstrings-python-accessors
    ```

### For developers

This package isn't maintained in our usual way.
It's super thin and not subject to any of our usual tests etc.
Hence there are no installation instructions here.

<!--- --8<-- [end:installation] -->

Python handler for [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)
supporting documentation of accessors.
Takes inspiration from [sphinx-autosummary-accessors](https://github.com/xarray-contrib/sphinx-autosummary-accessors).

This package extends [mkdocstrings-python](https://github.com/mkdocstrings/python)
(well, technically, [mkdocstrings-python-xref](https://github.com/analog-garage/mkdocstrings-python-xref))
to support more desirable documentation of accessors.

The accessors pattern is normally something like the following.
Let's take [`pandas`](https://pandas.pydata.org/docs/development/extending.html#registering-custom-accessors).
It is possible to register custom accessors, so you can do operations via that namespace.
For example, `pd.DataFrame.custom_namespace.operation()`.
When implemented, this is usually done via some sub-class,
which is then registered with the upstream package (in this case pandas).
The pattern normally looks something like the below

```python
@pd.register_accessor("custom_namespace")
class CustomNamespaceAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def operation(self):
        # Normally you do a more elaborate operation than this,
        # but you get the idea.
        return self._obj * 2
```

When you come to document this,
you normally get just the documentation for the class `CustomNamespaceAccessor`.
For example, if you include the following in your docs.

```md
::: CustomNamespaceAccessor
    handler: python
```

Then you will get documentation for `CustomNamespaceAccessor`.

This package introduces the following options.

```md
::: CustomNamespaceAccessor
    handler: python_accessors
    options:
        namespace: "pd.DataFrame.custom_namespace"
```

With this, the documentation will be transformed.
Instead of creating docs for `CustomNamespaceAccessor`,
you will instead get docs for `pd.DataFrame.custom_namespace`.

The configuration we have found works best is the below,
but you can use all the normal options that can be passed to
[mkdocstrings-python](https://github.com/mkdocstrings/python)
and [mkdocstrings-python-xref](https://github.com/analog-garage/mkdocstrings-python-xref)
to modify the appearance as you wish.

```md
::: CustomNamespaceAccessor
    handler: python_accessors
    options:
        namespace: "pd.DataFrame.custom_namespace"
        show_root_full_path: false
        show_root_heading: true
```

## Original template

This project was generated from this template:
[copier core python repository](https://gitlab.com/znicholls/copier-core-python-repository).
[copier](https://copier.readthedocs.io/en/stable/) is used to manage and
distribute this template.
