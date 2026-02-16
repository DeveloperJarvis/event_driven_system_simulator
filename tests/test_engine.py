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
# test_engine MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import unittest
from simulator.engine import SimulationEngine
from events.custom_events import CustomEvent


# --------------------------------------------------
# test simulation engine
# --------------------------------------------------
class TestSimulationEngine(unittest.TestCase):

    def setUp(self):
        self.engine = SimulationEngine()
    
    def test_add_and_run_event(self):
        event = CustomEvent(
            name="TestEvent",
            timestamp=1,
            data={"key": "value"}
        )
        self.engine.add_event(event)
        self.engine.run()
        # Test that the current time updated correctly
        self.assertEqual(self.engine.current_time, 1)
    
    def test_empty_queue(self):
        # Running an engine with no events should not 
        # raise exceptions
        try:
            self.engine.run()
        except Exception as e:
            self.fail(
                f"Engine run failed with empty queue: {e}"
            )


if __name__ == "__main__":
    unittest.main()
