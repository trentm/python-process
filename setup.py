#!/usr/bin/env python
# Copyright (c) 2002-2005 ActiveState Corp.
# See LICENSE.txt for license details.

"""Distutils setup script for 'process.py'."""

import sys
import os
import shutil
from distutils.core import setup


#---- support routines

def _getVersion():
    import process
    return process.__version__


#---- setup mainline

setup(name="process",
      version=_getVersion(),
      description="a Python module for cross-platform process control",
      author="Trent Mick",
      author_email="trentm@activestate.com",
      url="http://trentm.com/projects/process/",
      license="MIT License",
      platforms=["Windows", "Linux", "Mac OS X", "Unix"],
      long_description="""\
This is a cross-platform module for process control.

It allows you to launch processes on Windows, Linux and Mac OS X (and
other Un*ces) in a consistent way and enables many options and solves
some pains associated with existing mechanisms in Python, such as:
    os.system()
    os.popen(), os.popen2(), os.popen3(), os.popen4()
    os.exec*(), os.spanw*()

Note that Python 2.4's new subprocess module might be a better
alternative to this module in some cases.
""",
      keywords=["process", "popen", "system", "spawn"],

      py_modules=["process"],
     )

