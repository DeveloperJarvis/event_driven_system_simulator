# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the Event-Driven System Simulator Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Event-Driven System Simulator - Simulate real-world event systems (traffic, queues)
# Skills: simulation modeling, priority queues
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# test_runner MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import unittest
import os


def run_all_tests():
    # Discover all tests in the current directory and
    # subdirectories
    loader = unittest.TestLoader()
    tests = loader.discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
    )
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(tests)

    # Exit code 0 if all tests pass,
    # 1 otherwise (useful for CI/CD)
    if result.wasSuccessful():
        print("\n✅ All tests passed successfully!")
    else:
        print("\n❌ Some tests failed!")
        exit(1)


if __name__ == "__main__":
    run_all_tests()
