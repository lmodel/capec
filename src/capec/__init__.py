"""capec.

Common Attack Pattern Enumeration and Classification (CAPEC) 3.9 (LinkML)
"""

try:
    from capec._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
