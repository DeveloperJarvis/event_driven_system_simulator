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
# engine MODULE
# --------------------------------------------------
"""
Simulation engine
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from .event import Event
from .event_queue import EventQueue


# --------------------------------------------------
# simulation engine
# --------------------------------------------------
class SimulationEngine:
    def __init__(self):
        self.event_queue = EventQueue()
        self.current_time = 0
    
    def add_event(self, event: Event):
        self.event_queue.add_event(event)
    
    def run(self):
        while not self.event_queue.is_empty():
            event = self.event_queue.pop_event()
            self.current_time = event.timestamp
            event.process(self)
