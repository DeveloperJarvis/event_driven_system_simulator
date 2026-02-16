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
# test_scenarios MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import unittest
from scenarios.queue_simulation import run_queue_simulation
from scenarios.traffic_simulation import run_traffic_simulation


# --------------------------------------------------
# test scenarios
# --------------------------------------------------
class TestScenarios(unittest.TestCase):

    def test_queue_simulation_runs(self):
        # Should run without errors
        try:
            run_queue_simulation()
        except Exception as e:
            self.fail(f"Queue simulation failed {e}")
    
    def test_traffic_simulation_runs(self):
        # Should run without errors
        try:
            run_traffic_simulation()
        except Exception as e:
            self.fail(f"Traffic simulation failed {e}")


if __name__ == "__main__":
    unittest.main()
