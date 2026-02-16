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
# test_event_queue MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import unittest
from simulator.event_queue import EventQueue
from events.custom_events import CustomEvent


# --------------------------------------------------
# test event queue
# --------------------------------------------------
class TestEventQueue(unittest.TestCase):

    def setUp(self):
        self.queue = EventQueue()
    
    def test_enqueue_dequeue_order(self):
        event1 = CustomEvent(name="Event1", timestamp=5)
        event2 = CustomEvent(name="Event2", timestamp=2)
        event3 = CustomEvent(name="Event3", timestamp=3)

        self.queue.add_event(event1)
        self.queue.add_event(event2)
        self.queue.add_event(event3)

        # Priority queue should dequeue by timestamp order
        first = self.queue.pop_event()
        second = self.queue.pop_event()
        thrid = self.queue.pop_event()

        self.assertEqual(first.name, "Event2")
        self.assertEqual(second.name, "Event3")
        self.assertEqual(thrid.name, "Event1")

    def test_empty_queue(self):
        self.assertIsNone(self.queue.pop_event())
        self.assertEqual(len(self.queue), 0)


if __name__ == "__main__":
    unittest.main()
