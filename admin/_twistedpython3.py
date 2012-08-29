# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Provide lists of modules ported to Python 3.

Modules listed below have been ported to Python 3. The port may be partial,
with only some functionality available.

run-python3-tests uses this, and in the future it may be used by setup.py and
pydoctor.
"""

from __future__ import division

# A list of modules that have been ported, e.g. "twisted.python.versions"; a
# package name (e.g. "twisted.python") indicates the corresponding __init__.py
# file has been ported (e.g. "twisted/python/__init__.py"). To reduce merge
# conflicts, add new lines in alphabetical sort.
modules = [
    "twisted",
    "twisted.python",
    "twisted.python.compat",
    "twisted.python.monkey",
    "twisted.python._reflectpy3",
    "twisted.python._utilpy3",
    # filepaths depends on twisted.python.win32 and twisted.python.runtime,
    # which haven't yet been ported, but work well enough to be imported:
    "twisted.python.filepath",
    "twisted.python.versions",
    "twisted.test",
    ]


# A list of test modules that have been ported, e.g
# "twisted.python.test.test_versions". To reduce merge conflicts, add new
# lines in alphabetical sort.
testModules = [
    "twisted.python.test.test_reflectpy3",
    "twisted.python.test.test_utilpy3",
    "twisted.python.test.test_versions",
    "twisted.test.test_compat",
    "twisted.test.test_monkey",
    "twisted.test.test_paths",
    ]