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
# config MODULE
# --------------------------------------------------
"""
Configuration file for the Event-Driven System Simulator
Modify settings here to control simulation behaviour
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import os


BASE_DIR =  os.path.join(
        os.path.dirname(__file__), "..", ".."
    )
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "events.log")

SIMULATION_CONFIG = {
    # Options: "hospital", "queue", "traffic"
    "simulation_type": "queue",
    # For reproducibility
    "random_seed": 42,
    # Maximum number of events to process
    "amx_events": 1000,
    "log_file": LOG_FILE,
    # Print detailed event processing info
    "verbose": True,
}

# Example system-specific settings
QUEUE_SYSTEM_CONFIG = {
    "num_servers": 3,
    # average customers per minute
    "arrival_rate": 5,
    # average service time per minute
    "service_rate": 4,
}

TRAFFIC_SYSTEM_CONFIG = {
    "num_intersections": 3,
    # vehicles per minute
    "vehicle_spawn_rate": 10,
    # seconds per traffic light cycle
    "light_cycle": 60,
}
