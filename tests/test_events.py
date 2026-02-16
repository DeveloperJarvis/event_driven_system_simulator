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
# test_events MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import unittest
from simulator.event import Event
from events.custom_events import CustomEvent


# --------------------------------------------------
# dummy engine
# --------------------------------------------------
class DummyEngine:
    """Mock engine for testing event processing"""
    def __init__(self):
        self.log = []


# --------------------------------------------------
# test events
# --------------------------------------------------
class TestEvents(unittest.TestCase):

    def test_custom_event_process(self):
        engine = DummyEngine()
        event = CustomEvent(
            name="DummyEvent",
            timestamp=0,
            data={"info": 123},
        )

        # Override print to capture output
        import io, sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        event.process(engine)
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Processing DummyEvent", output)
    
    def test_event_not_implemented(self):
        event = Event(name="BaseEvent", timestamp=0)
        with self.assertRaises(NotImplementedError):
            event.process(None)


if __name__ == "__main__":
    unittest.main()
