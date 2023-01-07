"""{{cookiecutter.description}}"""

__version__ = "0.0.1"

from typeguard.importhook import install_import_hook  # isort:skip

install_import_hook("{{cookiecutter.package_name}}")  # isort:skip