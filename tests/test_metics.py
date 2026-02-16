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
# test_metics MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import unittest
from simulator.metrics import Metrics
from events.custom_events import CustomEvent


# --------------------------------------------------
# test metrics
# --------------------------------------------------
class TestMetrics(unittest.TestCase):

    def test_record_and_report(self):
        metrics = Metrics()
        event1 = CustomEvent(name="EventA", timestamp=0)
        event2 = CustomEvent(name="EventB", timestamp=0)

        metrics.record_event(event1)
        metrics.record_event(event1)
        metrics.record_event(event2)

        self.assertEqual(metrics.data["EventA"], 2)
        self.assertEqual(metrics.data["EventB"], 1)

        # Override print to test report output
        import io, sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        metrics.report()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("EventA: 2", output)
        self.assertIn("EventB: 1", output)


if __name__ == "__main__":
    unittest.main()
