# system76-driver: Universal driver for System76 computers
# Copyright (C) 2005-2013 System76, Inc.
#
# This file is part of `system76-driver`.
#
# `system76-driver` is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# `system76-driver` is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with `system76-driver`; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
Unit test for the `system76driver` package.
"""

from unittest import TestCase
from os import path
from subprocess import check_call

import system76driver


TREE = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
IN_TREE = path.isfile(path.join(TREE, 'setup.py'))


class TestConstants(TestCase):
    def test_version(self):
        self.assertIsInstance(system76driver.__version__, str)
        (year, month, rev) = system76driver.__version__.split('.')
        self.assertEqual(year, str(int(year)))
        self.assertGreaterEqual(int(year), 13)
        self.assertIn(month, ['04', '10'])
        self.assertEqual(rev, str(int(rev)))
        self.assertGreaterEqual(int(rev), 0) 


class TestScripts(TestCase):
    def setUp(self):
        if not IN_TREE:
            self.skipTest('not running tests in-tree')

    def check_script(self, name):
        script = path.join(TREE, name)
        self.assertTrue(path.isfile(script))
        # All the scripts need to be run as root, but you should always be able
        # to do a -h as a normal user:
        check_call([script, '-h'])

    def test_system76_driver(self):
        """
        Test the `system76-driver` Gtk UI script.
        """
        self.check_script('system76-driver')

    def test_system76_driver_cli(self):
        """
        Test the `system76-driver-cli` CLI script.
        """
        self.check_script('system76-driver-cli')

    def test_system76_daemon(self):
        """
        Test the `system76-daemon` CLI script.
        """
        self.check_script('system76-daemon')
