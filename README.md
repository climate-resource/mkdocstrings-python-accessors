# mkdocstrings-python-accessors

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
