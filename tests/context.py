#! /usr/bin/python3
# -*- coding: utf-8 -*-

##############################################################################
# Copyright 2020 AlexPDev
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################
"""Setup and Teardown functions and fixtures used for Unit Tests."""

import atexit
import os
import shutil
import string
import time

TESTS = os.path.dirname(os.path.abspath(__file__))
TESTDIR = os.path.join(TESTS, "TESTDIR")
ROOT = os.path.join(TESTDIR, "Root")


def rmpath(path):
    """Remove File or Folder.

    Args:
        path (`str`): File or Folder to delete.
    """
    while os.path.exists(path):
        if os.path.isfile(path):
            try:
                os.remove(path)
            except PermissionError:
                time.sleep(0.5)
        elif os.path.isdir(path):
            try:
                shutil.rmtree(path)
            except PermissionError:
                time.sleep(0.5)


def tstDir(func):
    """Create root testing directory partial function.

    Args:
        func (function): The function to execute in the body.

    Returns:
        wrapper (function): This callable.
    """

    def wrapper(*args, **kwargs):
        """Wrapper for testDir function."""
        if not os.path.exists(TESTDIR):
            os.mkdir(TESTDIR)
        return func(*args, **kwargs)

    return wrapper


def fill(path, exp=21):
    """Fill file paths with meaningless bytes for testing purposes.

    Args:
        path (`str`):  The path to file destination.
        exp (`int`):  Number indicating the power of 2 for the file size.

    Returns:
        path (`str`): the root path.
    """
    text = (string.printable + string.whitespace + string.hexdigits) * 8
    btext = text.encode("utf-8")
    btextlen = len(btext)
    size = 2 ** exp
    with open(path, "wb") as fd:
        while size >= 0:
            fd.write(btext)
            size -= btextlen
    return path


@tstDir
def tstfile(val=20):
    root = os.path.join(TESTDIR, "file1")
    fill(root, exp=val)
    return root


@tstDir
def tstdir():
    root = ROOT
    dir1 = os.path.join(root, "dir1")
    file1 = os.path.join(root, "file1")
    file2 = os.path.join(root, "file2")
    file3 = os.path.join(dir1, "file3")
    file4 = os.path.join(dir1, "file4")
    for folder in [root, dir1]:
        rmpath(folder)
        os.mkdir(folder)
    for file in [file1, file2, file3, file4]:
        fill(file, 26)
    return root


@tstDir
def tstdir3():
    root = ROOT
    dir1 = os.path.join(root, "dir1")
    file3 = os.path.join(dir1, "file3")
    file4 = os.path.join(dir1, "file4")
    dir2 = os.path.join(dir1, "dir2")
    file1 = os.path.join(dir2, "file1")
    file2 = os.path.join(dir2, "file2")
    for folder in [root, dir1, dir2]:
        rmpath(folder)
        os.mkdir(folder)
    for file in [file1, file2, file3, file4]:
        fill(file, 22)
    return root


@tstDir
def tstdir2():
    root = ROOT
    dir1 = os.path.join(root, "dir1")
    dir2 = os.path.join(dir1, "dir2")
    file1 = os.path.join(dir2, "file1")
    file2 = os.path.join(dir2, "file2")
    file3 = os.path.join(dir1, "file3")
    file4 = os.path.join(dir1, "file4")
    for folder in [root, dir1, dir2]:
        rmpath(folder)
        os.mkdir(folder)
    for file in [file1, file2, file3, file4]:
        fill(file, 26)
    return root


@atexit.register
def teardown():  # pragma: no cover
    try:
        rmpath(TESTDIR)
        return True
    except PermissionError:
        time.sleep(1.5)
        teardown()
