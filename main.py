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
# main MODULE
# --------------------------------------------------
"""
Main entry point for the Event-Driven System Simulator
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import sys
from simulator.engine import SimulationEngine
from scenarios.queue_simulation import run_queue_simulation
from scenarios.traffic_simulation import run_traffic_simulation
from config.config import SIMULATION_CONFIG


def main():
    print("=== Event-Driven System Simulator ===")
    
    simulation_type = SIMULATION_CONFIG.get(
        "simulation_type", "queue"
    )

    engine = SimulationEngine()

    if simulation_type == "queue":
        run_queue_simulation(engine)
    elif simulation_type == "traffic":
        run_traffic_simulation(engine)
    else:
        print(f"Unkown simulation type: {simulation_type}")
        sys.exit(1)

    print("Simulation completed successfully")


if __name__ == "__main__":
    main()
