# PYTHON_ARGCOMPLETE_OK
"""
pytest: unit and functional testing with Python.
"""
__all__ = [
    'main',
    'UsageError',
    'cmdline',
    'hookspec',
    'hookimpl',
    '__version__',
    'register_assert_rewrite',
    'freeze_includes',
]

if __name__ == '__main__': # if run as a script or by 'python -m pytest'
    # we trigger the below "else" condition by the following import
    import pytest
    raise SystemExit(pytest.main())

# else we are imported

from _pytest.config import (
    main, UsageError, _preloadplugins, cmdline,
    hookspec, hookimpl
)
from _pytest.assertion import register_assert_rewrite
from _pytest.freeze_support import freeze_includes
from _pytest import __version__


_preloadplugins() # to populate pytest.* namespace so help(pytest) works

