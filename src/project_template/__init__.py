"""Project template."""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("project-template")
except PackageNotFoundError:
    # Package is not installed
    __version__ = "unknown"

