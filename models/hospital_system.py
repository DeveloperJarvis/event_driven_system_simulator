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
# hospital_system MODULE
# --------------------------------------------------
"""
Hospital simulation system
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from simulator.event import Event
from .generic_system import GenericSystem


# --------------------------------------------------
# hospital system
# --------------------------------------------------
class HospitalSystem(GenericSystem):
    def __init__(self, num_doctors=5):
        super().__init__("HospitalSystem")
        self.num_doctors = num_doctors
        self.patients_waiting = []
    
    def update(self, event: Event):
        print(f"[HospitalSystem] Event: {event.name}")
